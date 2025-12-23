from dataclasses import dataclass
from typing import Literal
from datetime import datetime

@dataclass
class FileUploadedIntegrationEvent:
    eventName: Literal["FileUploaded"]
    payload: dict
    occurredAt: str


@dataclass
class TextExtractedIntegrationEvent:
    eventName: Literal["TextExtracted"]
    payload: dict
    occurredAt: str
