import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
INVITE_LINK = "https://t.me/+emecsqCA8IJhZGVk"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""
👋 Hello {user.first_name}!

Welcome! Here is my invite link:

{INVITE_LINK}

Click the link above to join our community!
    """
    await update.message.reply_text(welcome_message.strip())

def main():
    """Start the bot."""
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN environment variable is not set!")
        return
    
    try:
        # Create the Application
        application = Application.builder().token(BOT_TOKEN).build()

        # Add command handler
        application.add_handler(CommandHandler("start", start_command))

        # Start the Bot with polling
        logger.info("🚀 Bot is starting with polling...")
        application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES
        )
        
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")
        raise

if __name__ == '__main__':
    main()
