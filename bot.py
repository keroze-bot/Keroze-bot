import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 KEROZE_BOT está funcionando!"
    )

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos disponíveis:\n/start\n/ajuda"
    )

def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_TOKEN não configurado")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))

    print("KEROZE_BOT iniciado!")
    app.run_polling()

if __name__ == "__main__":
    main()
