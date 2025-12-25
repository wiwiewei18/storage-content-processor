## 🛠️ Storage Content Processor

[English](./README.md) | [日本語](./README.ja.md)

---

### 🔍 Overview

**storage-content-processor** is a **background worker** for the Storage System.

Its primary job is to **extract text content from uploaded files** using OCR and make it **searchable**.

This worker operates asynchronously and integrates with the backend via **RabbitMQ**.

---

### 🎯 Responsibilities

- 📄 **Extract text** from files (PDFs, images, scans) using **pytesseract (OCR)**
- 🗄️ **Download files** from **Cloudflare R2 (S3-compatible)** using **boto3**
- 🐇 **Consume jobs** from **RabbitMQ queues** (pika)
- 🧠 Send extracted text back to **backend** for indexing and search
- ✅ Fully **automated and scalable** to handle large volumes of documents

---

### 🧱 Architecture

```
Client → Cloudflare R2
       ↘ storage-be → RabbitMQ → storage-content-processor
```

- Backend publishes a **job message** to RabbitMQ when a file is uploaded
- Worker consumes the message, downloads the file, extracts text, and sends results back

---

### ⚙️ Tech Stack

- **Language:** Python
- **OCR:** pytesseract
- **Storage Access:** boto3 (S3-compatible, Cloudflare R2)
- **Message Queue:** RabbitMQ (pika)

---

### 🔄 High-Level Flow

1. 📤 Client uploads file **directly to R2**
2. ⚙️ Backend publishes a **processing job** to RabbitMQ
3. 🐇 Content processor consumes the job
4. 📄 File is downloaded and **OCR is performed**
5. 🧠 Extracted text is sent back to **backend** for **indexing/search**
6. 🔍 Text becomes searchable via API

---

### 🧪 Testing Strategy

- **Unit tests**: OCR processing, file handling, job parsing
- **Integration tests**: Worker → R2 → Backend message flow
- **Python testing tools:** pytest + unittest

---

### 🎯 Goals

- Automate **text extraction from all uploaded files**
- Enable **search by file content**
- Support **high throughput** and **scalable background processing**

---

### 📚 Related Repositories

- [`storage-system`](https://github.com/wiwiewei18/storage-system)
- [`storage-domain`](https://github.com/wiwiewei18/storage-domain)
- [`storage-be`](https://github.com/wiwiewei18/storage-be)
- [`storage-fe`](https://github.com/wiwiewei18/storage-fe)

---

### 🌍 Language

- 🇬🇧 English (current)
- 🇯🇵 Japanese → [README.ja.md](./README.ja.md)
