import os
import asyncio
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from telegram.ext import Application
import features

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8000))

# Simple health-check handler
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"NovaX is alive!")
    def log_message(self, format, *args):
        pass  # quiet logging

def run_http_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    logger.info(f"Health server running on port {PORT}")
    server.serve_forever()

async def main():
    # Bot application
    app = Application.builder().token(TOKEN).build()
    features.register_all(app)

    # HTTP server ko alag thread mein daalo
    Thread(target=run_http_server, daemon=True).start()

    # Polling shuru karo
    logger.info("NovaX is booting up... 🚀")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    logger.info("NovaX is alive and kicking! ⚡")

    # Run forever
    stop_signal = asyncio.get_event_loop().create_future()
    await stop_signal

if __name__ == "__main__":
    asyncio.run(main())
