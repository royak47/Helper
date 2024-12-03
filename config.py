from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("Error: No token found. Please set the TELEGRAM_BOT_TOKEN environment variable.")
    exit()  # Exit if no token found
else:
    print(f"Bot token is loaded: {TOKEN[:10]}...")  # Print part of the token for verification
