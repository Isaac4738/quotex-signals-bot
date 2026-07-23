from telegram import Bot
import asyncio
from config import BOT_TOKEN, CHAT_ID

async def main():
    bot = Bot(token=BOT_TOKEN)

    if CHAT_ID:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="✅ Quotex Signals Bot is running!"
        )
    else:
        print("CHAT_ID is empty")

if __name__ == "__main__":
    asyncio.run(main())
