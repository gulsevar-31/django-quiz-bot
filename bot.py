import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, PollAnswer
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from questions import QUESTIONS

TOKEN = "8942962838:AAFEsKgf3h0FJ8LpSlvl97jYBDFg3266xfU" # O'zingizning to'liq tokeningizni yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Har bir poll_id va uning to'g'ri javobini saqlash
poll_data = {}

# Foydalanuvchilarning to'g'ri va xato javoblari
user_results = {}

class QuizState(StatesGroup):
    playing = State()

@dp.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(QuizState.playing)
    await state.update_data(current_index=0)
    
    # Natijalarni nolga tenglaymiz
    user_results[message.from_user.id] = {"correct": 0, "wrong": 0}
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="▶️ Viktorinani boshlash", callback_data="next_poll")]
    ])
    await message.answer("Salom! Django bo'yicha to'liq avtomatlashgan test botiga xush kelibsiz.", reply_markup=keyboard)

# Foydalanuvchi variantni bosganda ishlaydigan handler
@dp.poll_answer()
async def handle_poll_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id
    
    if poll_id in poll_data:
        correct_option = poll_data[poll_id]
        selected_option = poll_answer.option_ids[0] if poll_answer.option_ids else None
        
        if user_id not in user_results:
            user_results[user_id] = {"correct": 0, "wrong": 0}
            
        if selected_option == correct_option:
            user_results[user_id]["correct"] += 1
        else:
            user_results[user_id]["wrong"] += 1

@dp.callback_query(F.data == "next_poll")
async def send_quiz_poll(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await run_quiz(callback.message.chat.id, callback.from_user.id, callback.bot, state)

async def run_quiz(chat_id, user_id, bot_instance, state):
    data = await state.get_data()
    index = data.get("current_index", 0)
    
    if index < len(QUESTIONS):
        q = QUESTIONS[index]
        
        # Poll yuborish
        msg = await bot_instance.send_poll(
            chat_id=chat_id,
            question=f"{q['id']}-savol:\n{q['question']}",
            options=q['options'],
            type='quiz',
            correct_option_id=q['correct'],
            open_period=30,
            is_anonymous=False  # JAXON/MAMNUNIYAT: Foydalanuvchi kimligini bilish uchun anonimlikni o'chiramiz!
        )
        
        # Poll ID sini xotirada saqlaymiz
        poll_data[msg.poll.id] = q['correct']
        
        await state.update_data(current_index=index + 1)
        
        # 30 soniya kutamiz
        await asyncio.sleep(30)
        
        if index + 1 < len(QUESTIONS):
            await run_quiz(chat_id, user_id, bot_instance, state)
        else:
            # Biroz kutib, natijani hisoblaymiz (oxirgi javob yetib kelishi uchun)
            await asyncio.sleep(2)
            
            stats = user_results.get(user_id, {"correct": 0, "wrong": 0})
            correct_count = stats["correct"]
            wrong_count = stats["wrong"]
            total = correct_count + wrong_count if (correct_count + wrong_count) > 0 else len(QUESTIONS)
            
            percentage = round((correct_count / len(QUESTIONS)) * 100, 1)
            
            result_text = (
                f"🏁 <b>Test yakunlandi!</b>\n\n"
                f"📊 <b>Sizning natijangiz:</b>\n"
                f"✅ To'g'ri javoblar: <b>{correct_count} ta</b>\n"
                f"❌ Xato javoblar: <b>{wrong_count} ta</b>\n"
                f"📈 Umumiy ko'rsatkich: <b>{percentage}%</b>"
            )
            
            await bot_instance.send_message(chat_id, result_text, parse_mode="HTML")
            await state.clear()
    else:
        await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())