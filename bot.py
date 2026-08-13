

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7112530098:AAEiePhA_dVdhWMp-IrbAnZ-5jh4DO08_nQ"
CHAT_ID = 5955485014

async def branco_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="⚪"
    )

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    print(f"CHAT ID: {chat.id}")
    print(f"CHAT: {chat.title}")

    await update.message.reply_text(
        f"ID deste grupo: {chat.id}"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("branco", branco_command))
    app.add_handler(CommandHandler("id", id_command))

    print("BOT RODANDO...")
    app.run_polling()

if __name__ == "__main__":
        main()
    
