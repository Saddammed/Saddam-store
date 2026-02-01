from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 ضع توكن البوت هنا
TOKEN = "8179576448:AAGR15urYreu8zooAF4eXyguRNn7nqkkank"

# 📢 ضع معرف القناة هنا (يجب أن يكون البوت أدمن)
CHANNEL = "https://t.me/Online_store485353"

WELCOME_TEXT = """
🔥 مرحبًا بك في متجر صدام 👋

⚠️ لاستخدام البوت يجب الاشتراك في القناة أولًا

👇 بعد الاشتراك اضغط الزر:
"""

SERVICES_TEXT = """
🎉 تم التحقق بنجاح!

🕹️ شحن الألعاب:
- PUBG Mobile
- Free Fire
- eFootball
- TikTok Coins

📱 اشتراكات:
- Netflix
- Google Play
- Apple Store

📞 واتساب:
https://wa.me/message/REDKIHRAVCUEB1

💬 تيليجرام:
https://t.me/Saddammed
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ تم الاشتراك", callback_data="check")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def check_sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text(SERVICES_TEXT)
        else:
            await query.edit_message_text("❌ يجب الاشتراك في القناة أولًا ثم الضغط على الزر")
    except:
        await query.edit_message_text("⚠️ تأكد أن البوت أدمن في القناة")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_sub))
    app.run_polling()

if __name__ == "__main__":
    main()

