#  Telegram QR Code Decoder Bot

> ⚠️ **[ARCHIVED] - Beginner Python Project (2023)**
> 
> *This is an early learning project. It is preserved here to show my journey and progression in Python development. The architecture and practices in this code do not reflect my current engineering standards.*

## About
A simple Telegram bot built with **Telethon** (asyncio) and `pyzbar`. The bot receives images containing QR codes, downloads them, decodes the content, and sends the extracted text back to the user.

## Architectural Flaws & Lessons Learned
While this bot works functionally, analyzing it with a Software Engineering mindset reveals several architectural issues that I have since learned to avoid:

*   **Blocking the Event Loop:** The bot uses an asynchronous framework (`telethon`), but processes the images synchronously using CPU-bound libraries (`PIL` and `pyzbar`). In a production environment, this blocks the async event loop, preventing the bot from responding to other users concurrently. Today, I would offload such tasks to a separate thread/process or use a task queue like **Celery/RabbitMQ**.
*   **Storage Leaks:** The script downloads media to the server's disk but fails to clean up (`os.remove()`) after processing. Over time, this would lead to a completely full disk and server crashes.
*   **Hardcoded Secrets:** API credentials (`api_id`, `api_hash`) were hardcoded in the script. Modern deployments dictate that secrets should be securely injected via environment variables (`.env`) or secret managers.

Building this bot was a fun milestone in my early programming days, but my current expertise lies in designing robust, secure, and non-blocking backend services.
