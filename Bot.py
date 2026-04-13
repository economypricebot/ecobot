import re
from telethon import TelegramClient
from telegram import Bot

# اطلاعات خودت
api_id = 123456
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"
channel_username = "@your_channel"
source_channel = "dollar_tehran3bze"

bot = Bot(token=bot_token)

async def main():
    async with TelegramClient("session", api_id, api_hash) as client:
        messages = await client.get_messages(source_channel, limit=1)
        
        if not messages:
            return
        
        text = messages[0].text
        
        # استخراج عدد
        price = re.search(r'\d[\d,]*', text)
        
        if price:
            price = price.group()
            
            message = f"💵 دلار: {price}"
            
            bot.send_message(chat_id=channel_username, text=message)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
