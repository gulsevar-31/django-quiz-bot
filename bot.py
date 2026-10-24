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

# 130 ta savolingiz joylashgan fayl
from questions import QUESTIONS  

TOKEN = "7835154388:AAH8N_153hUqP1C8Vp4uFj1JvW_X2Z1K3u0"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

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

threading.Thread(target=run_dummy_server, daemon=True).start()

# Test holatlarini saqlash
class QuizState(StatesGroup):
    current_question = State()
    score = State()

async def send_next_question(message_or_poll_answer, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_question", 0)
    
    if index < len(QUESTIONS):
        q = QUESTIONS[index]
        # Poll (savol) yuborish
        if isinstance(message_or_poll_answer, types.Message):
            await message_or_poll_answer.answer_poll(
                question=f"{index+1}-savol:\n{q['question']}",
                options=q['options'],
                correct_option_id=q['correct_option_id'],
                type="quiz",
                is_anonymous=False
            )
        elif isinstance(message_or_poll_answer, types.PollAnswer):
            await bot.send_poll(
                chat_id=message_or_poll_answer.user.id,
                question=f"{index+1}-savol:\n{q['question']}",
                options=q['options'],
                correct_option_id=q['correct_option_id'],
                type="quiz",
                is_anonymous=False
            )
    else:
        # Test yakunlanganda
        score = data.get("score", 0)
        total = len(QUESTIONS)
        percentage = round((score / total) * 100, 1)
        
        chat_id = message_or_poll_answer.chat.id if isinstance(message_or_poll_answer, types.Message) else message_or_poll_answer.user.id
        await bot.send_message(
            chat_id=chat_id,
            text=f"🏁 **Test yakunlandi!**\n\n"
                 f"📊 Sizning natijangiz:\n"
                 f"✅ To'g'ri javoblar: **{score} ta**\n"
                 f"❌ Xato javoblar: **{total - score} ta**\n"
                 f"📈 Umumiy ko'rsatkich: **{percentage}%**"
        )
        await state.clear()

@dp.message(Command("start"))
async def start_quiz(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(current_question=0, score=0)
    await message.answer(f"Salom! Imtihonga tayyorgarlik uchun {len(QUESTIONS)} ta savoldan iborat test boshlandi. Omad!")
    await send_next_question(message, state)

@dp.poll_answer()
async def handle_poll_answer(poll_answer: types.PollAnswer, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_question", 0)
    score = data.get("score", 0)
    
    if index < len(QUESTIONS):
        q = QUESTIONS[index]
        if poll_answer.option_ids[0] == q['correct_option_id']:
            score += 1
        
        index += 1
        await state.update_data(current_question=index, score=score)
        await send_next_question(poll_answer, state)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 