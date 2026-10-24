import os
import asyncio
import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from questions import QUESTIONS  # 130 ta savol joylashgan fayl

# Tokeningizni shu yerga yozing
TOKEN = "7835154388:AAH8N_153hUqP1C8Vp4uFj1JvW_X2Z1K3u0"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Render port talab qilgani uchun soxta HTTP server (Port 10000)
class SimpleHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot ishlayapti va port ochiq!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# Serverni orqa fonda (background) ishga tushiramiz
threading.Thread(target=run_dummy_server, daemon=True).start()


# Bot komandalari
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Salom! Imtihonga tayyorgarlik uchun 130 ta savol botiga xush kelibsiz. Testni boshlaymiz!")
    # Savollarni yuborish logikasini shu yerga qo'shishingiz mumkin
    await message.answer(f"Jami yuklangan savollar soni: {len(QUESTIONS)} ta")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main()) 