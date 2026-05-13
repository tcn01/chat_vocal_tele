import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from src.ai import EnglishWord

class TelegramBot:
    def __init__(self, token: str):
        self.bot = Bot(token=token)

    async def send_word_of_the_day(self, chat_id: str, word_data: EnglishWord):
        message = (
            f"🌟 *WORD OF THE DAY* 🌟\n\n"
            f"🔤 *Word:* `{word_data.word}` ({word_data.word_type})\n"
            f"🔊 *IPA:* /{word_data.ipa}/\n"
            f"🇻🇳 *Nghĩa:* {word_data.meaning_vi}\n\n"
            f"📝 *Ví dụ:*\n" + "\n".join([f"• {ex}" for ex in word_data.examples]) + "\n\n"
            f"💡 *Ngữ cảnh:* {word_data.usage_context}\n\n"
            f"🧠 *Tư duy sử dụng:* {word_data.mindset}"
        )
        
        await self.bot.send_message(
            chat_id=chat_id,
            text=message,
            parse_mode=ParseMode.MARKDOWN
        )

async def main():
    # Test block
    pass

if __name__ == "__main__":
    asyncio.run(main())
