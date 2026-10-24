import os
import asyncio
import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# 130 ta savol joylashgan faylingizni chaqirib olamiz
from questions import QUESTIONS  

# BotFather'dan olgan tokeingizni shu qo'shtirnoq ichiga yozasiz
TOKEN = "8942962838:AAFEsKgf3h0FJ8LpSlvl97jYBDFg3266xfU"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Render o'chib qolmasligi uchun 10000-portda ishlaydigan oddiy HTTP server
class DummyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot ishlayapti va port ochiq!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

# Serverni orqa fonda alohida oqimda (thread) ishga tushiramiz
threading.Thread(target=run_dummy_server, daemon=True).start()

# FSM (Test jarayonini boshqarish uchun holatlar)
class QuizState(StatesGroup):
    current_question = State()
    score = State()

# Savollarni ketma-ket yuborish funksiyasi
async def send_next_question(event, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_question", 0)
    
    if index < len(QUESTIONS):
        q = QUESTIONS[index]
        # Agar xabar kelgan bo'lsa (masalan /start)
        if isinstance(event, types.Message):
            await event.answer_poll(
                question=f"{index+1}-savol:\n{q['question']}",
                options=q['options'],
                correct_option_id=q['correct_option_id'],
                type="quiz",
                is_anonymous=False
            )
        # Agar foydalanuvchi javob bergan bo'lsa (poll_answer)
        elif isinstance(event, types.PollAnswer):
            await bot.send_poll(
                chat_id=event.user.id,
                question=f"{index+1}-savol:\n{q['question']}",
                options=q['options'],
                correct_option_id=q['correct_option_id'],
                type="quiz",
                is_anonymous=False
            )
    else:
        # 130 ta savol tugaganda natijani chiqarish
        score = data.get("score", 0)
        total = len(QUESTIONS)
        percentage = round((score / total) * 100, 1) if total > 0 else 0
        
        chat_id = event.chat.id if isinstance(event, types.Message) else event.user.id
        await bot.send_message(
            chat_id=chat_id,
            text=f"🏁 **Test yakunlandi!**\n\n"
                 f"📊 Sizning natijangiz:\n"
                 f"✅ To'g'ri javoblar: **{score} ta**\n"
                 f"❌ Xato javoblar: **{total - score} ta**\n"
                 f"📈 Umumiy ko'rsatkich: **{percentage}%**"
        )
        await state.clear()

# /start buyrug'i bosilganda testni boshlash
@dp.message(Command("start"))
async def start_quiz(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(current_question=0, score=0)
    await message.answer(f"Salom! Imtihonga tayyorgarlik uchun {len(QUESTIONS)} ta savoldan iborat test boshlandi. Omad!")
    await send_next_question(message, state)

# Foydalanuvchi test savoliga javob berganda ishlaydigan qism
@dp.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_question", 0)
    score = data.get("score", 0)
    
    if index < len(QUESTIONS):
        q = QUESTIONS[index]
        # To'g'ri javobni tekshirish
        if poll_answer.option_ids[0] == q['correct_option_id']:
            score += 1
        
        index += 1
        await state.update_data(current_question=index, score=score)
        await send_next_question(poll_answer, state)

async def main():
    await dp.start_polling(bot, drop_pending_updates=True) 