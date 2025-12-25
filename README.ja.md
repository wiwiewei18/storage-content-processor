## 🛠️ ストレージコンテンツプロセッサ

[English](./README.md) | [日本語](./README.ja.md)

---

### 🔍 概要

**storage-content-processor** は、ストレージシステムの **バックグラウンドワーカー** です。

主な役割は **アップロードされたファイルからテキストを抽出** し、**検索可能にする** ことです。

このワーカーは非同期で動作し、**RabbitMQ** を通じてバックエンドと連携します。

---

### 🎯 責務

- 📄 **ファイルからテキストを抽出**（PDF、画像、スキャン文書） **pytesseract (OCR) 使用**
- 🗄️ **Cloudflare R2 (S3 互換) からファイルをダウンロード**（boto3 使用）
- 🐇 **RabbitMQ キュー (pika) からジョブを取得**
- 🧠 抽出したテキストを **バックエンドへ送信** してインデックス化・検索可能に
- ✅ 大量のドキュメント処理に対応した **自動化・スケーラブル設計**

---

### 🧱 アーキテクチャ

```
Client → Cloudflare R2
       ↘ storage-be → RabbitMQ → storage-content-processor
```

- バックエンドは **ファイルアップロード時に処理ジョブを RabbitMQ に発行**
- ワーカーはジョブを取得 → ファイルをダウンロード → OCR → 結果をバックエンドへ送信

---

### ⚙️ 技術スタック

- **言語:** Python
- **OCR:** pytesseract
- **ストレージアクセス:** boto3 (S3 互換, Cloudflare R2)
- **メッセージキュー:** RabbitMQ (pika)

---

### 🔄 高レベルフロー

1. 📤 クライアントが **R2 に直接ファイルをアップロード**
2. ⚙️ バックエンドが **処理ジョブを RabbitMQ に発行**
3. 🐇 コンテンツプロセッサがジョブを取得
4. 📄 ファイルをダウンロードし **OCR 処理**
5. 🧠 抽出したテキストを **バックエンドに送信**
6. 🔍 API を通じて **テキスト検索可能**

---

### 🧪 テスト戦略

- **ユニットテスト:** OCR 処理、ファイル操作、ジョブ解析
- **統合テスト:** ワーカー → R2 → バックエンドのメッセージフロー
- **テストツール:** pytest + unittest

---

### 🎯 目的

- すべてのアップロードファイルから **テキスト抽出を自動化**
- **ファイル内容による検索を可能** に
- **高スループット & スケーラブルなバックグラウンド処理** に対応

---

### 📚 関連リポジトリ

- [`storage-system`](https://github.com/wiwiewei18/storage-system/blob/main/README.ja.md)
- [`storage-domain`](https://github.com/wiwiewei18/storage-domain/blob/main/README.ja.md)
- [`storage-be`](https://github.com/wiwiewei18/storage-be/blob/main/README.ja.md)
- [`storage-fe`](https://github.com/wiwiewei18/storage-fe/blob/main/README.ja.md)

---

### 🌍 言語

- 🇬🇧 English → [README.md](./README.md)
- 🇯🇵 日本語（本ドキュメント）
