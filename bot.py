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

# 130 ta savol joylashgan fayl
from questions import QUESTIONS  

TOKEN = "8942962838:AAHtNwK-BGmAiNSWDmPKV0vZ05Jbiwb6HY" 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Render port talabini qondirish uchun oddiy HTTP server
class DummyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot ishlayapti!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

class QuizState(StatesGroup):
    current_question = State()
    score = State()

@dp.message(Command("start"))
async def start_quiz(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(current_question=0, score=0)
    await message.answer(f"Salom! Imtihonga tayyorgarlik uchun {len(QUESTIONS)} ta savoldan iborat test boshlandi. Omad! ❤️")
    
    q = QUESTIONS[0]
    await message.answer_poll(
        question=f"1-savol:\n{q['question']}",
        options=q['options'],
        correct_option_id=q['correct_option_id'],
        type="quiz",
        is_anonymous=False
    )

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
        
        if index < len(QUESTIONS):
            next_q = QUESTIONS[index]
            await bot.send_poll(
                chat_id=poll_answer.user.id,
                question=f"{index+1}-savol:\n{next_q['question']}",
                options=next_q['options'],
                correct_option_id=next_q['correct_option_id'],
                type="quiz",
                is_anonymous=False
            )
        else:
            total = len(QUESTIONS)
            percentage = round((score / total) * 100, 1) if total > 0 else 0
            await bot.send_message(
                chat_id=poll_answer.user.id,
                text=f"🏁 **Test yakunlandi!**\n\n"
                     f"📊 Sizning natijangiz:\n"
                     f"✅ To'g'ri javoblar: **{score} ta**\n"
                     f"❌ Xato javoblar: **{total - score} ta**\n"
                     f"📈 Umumiy ko'rsatkich: **{percentage}%**"
            )
            await state.clear()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 