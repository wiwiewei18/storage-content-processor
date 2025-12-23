import pika
from src.config import settings
from src.subscriber import FileUploadedSubscriber
from src.ocr.service import OCRService
from src.storage.object_storage import ObjectStorage
from src.publisher import EventPublisher

connection = pika.BlockingConnection(
    pika.URLParameters(settings.RABBITMQ_URI)
)
channel = connection.channel()

channel.exchange_declare(
    exchange="ocr.exchange",
    exchange_type="topic",
    durable=True,
)

channel.queue_declare(queue="ocr.extract-text", durable=True)

channel.queue_bind(
    exchange="storage.exchange",
    routing_key="file.uploaded",
    queue="ocr.extract-text",
)

storage = ObjectStorage(
    region=settings.R2_REGION,
    bucket=settings.R2_BUCKET
)

publisher = EventPublisher(
    channel,
    exchange="ocr.exchange",
    routing_key="text.extracted"
)

consumer = FileUploadedSubscriber(
    storage=storage,
    ocr_service=OCRService(),
    publisher=publisher
)

def callback(ch, method, properties, body):
    consumer.handle(body)
    ch.basic_ack(method.delivery_tag)

channel.basic_consume(
    queue="ocr.extract-text",
    on_message_callback=callback
)

print("OCR Worker running...")
channel.start_consuming()
