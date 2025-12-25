import json
import tempfile
from datetime import datetime
from src.events import FileUploadedIntegrationEvent, TextExtractedIntegrationEvent

class FileUploadedSubscriber:
    def __init__(self, storage, ocr_service, publisher):
        self.storage = storage
        self.ocr = ocr_service
        self.publisher = publisher

    def handle(self, message: bytes):
        data = json.loads(message)

        event = FileUploadedIntegrationEvent(**data)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            self.storage.download(
                event.payload["objectKey"],
                tmp.name
            )

            text = self.ocr.extract_text(
                tmp.name,
                event.payload["mimeType"]
            )

        extracted_event = TextExtractedIntegrationEvent(
            eventName="TextExtracted",
            payload={
                "fileId": event.payload["fileId"],
                "text": text,
                "language": "unknown",
            },
            occurredAt=datetime.utcnow().isoformat()
        )

        self.publisher.publish(extracted_event)
