import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

# Get bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')
INVITE_LINK = "https://t.me/+emecsqCA8IJhZGVk"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Create Flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
        logger.error("BOT_TOKEN environment variable is not set!")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handler
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    # This runs when executed directly (for local testing)
    main()
