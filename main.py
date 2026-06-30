import os
import asyncio
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler
import features  # ye features/__init__.py ko load karega

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    logger.error("BOT_TOKEN environment variable not set!")
    exit(1)

async def main():
    # Application banayein
    app = Application.builder().token(TOKEN).build()

    # Features folder ke saare handlers register karein
    features.register_all(app)

    # Bot ko start karein (polling)
    logger.info("NovaX is booting up... 🚀")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    logger.info("NovaX is alive and kicking! ⚡")

    # Graceful shutdown ke liye
    stop_signal = asyncio.Future()
    try:
        await stop_signal
    except asyncio.CancelledError:
        pass
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())