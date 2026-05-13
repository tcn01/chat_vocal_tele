import os
import asyncio
from dotenv import load_dotenv
from src.ai import AIEngine
from src.bot import TelegramBot

# Load env variables if running locally
load_dotenv()

async def run_daily_task():
    # 1. Configuration
    openai_key = os.getenv("OPENAI_API_KEY")
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not all([openai_key, telegram_token, chat_id]):
        print("Missing environment variables!")
        return

    # 2. Initialize engines
    ai_engine = AIEngine(api_key=openai_key)
    bot = TelegramBot(token=telegram_token)

    # 3. Generate content
    print("Generating word of the day...")
    word_data = ai_engine.generate_daily_word(level="Intermediate")

    # 4. Send to Telegram
    print(f"Sending word '{word_data.word}' to Telegram...")
    await bot.send_word_of_the_day(chat_id=chat_id, word_data=word_data)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(run_daily_task())
