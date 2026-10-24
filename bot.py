import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# 130 ta savol joylashgan fayl
from questions import QUESTIONS  

TOKEN = "8942962838:AAHtNwK-BGmAiNSWDmPKV0vZ05Jbiwb6HY" 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

WEBHOOK_HOST = "https://django-quiz-bot-1.onrender.com"
WEBHOOK_PATH = f"/bot/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

class QuizState(StatesGroup):
    current_question = State()
    score = State()

@dp.message(Command("start"))
async def start_quiz(message: types.Message, state: FSMContext):
    await state.clear()
    await state.update_data(current_question=0, score=0)
    await message.answer(f"Salom! Imtihonga tayyorgarlik uchun {len(QUESTIONS)} ta savoldan iborat test boshlandi. Omad! ❤️")
    
    # 1-savolni yuboramiz
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

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)

def main():
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    dp.startup.register(on_startup)
    
    port = int(os.environ.get("PORT", 10000))
    web.run_app(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main() 