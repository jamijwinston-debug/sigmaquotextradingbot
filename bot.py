import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Image URL
IMAGE_URL = "https://freeimage.host/i/KsDHE8l"

# Main message content
MAIN_MESSAGE = """🌐 if You Are A Trader and want To Make Profit Then Welcome To Our Community! 🔥

We will help You To Recover Your Losses, Just Join our 20$ To 2000$ Compounding Session Daily 💵

🔷 99% Accuracy
🔷 Loss Recovery
🔷 Non Mtg Signals
🔷 Daily 10 to 15 Sureshot Signals
🔷 Expert Trading Signals
🔷 Community Support
🔷 24/7 Assistance
🙋‍♂️ Let's make profitable trades together!

💥 Join the Winning Team NOW! 💥
⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
