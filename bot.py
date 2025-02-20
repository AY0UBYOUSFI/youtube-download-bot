from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Your bot token
TOKEN = "7423852571:AAFffx0oc9P0hqEagwMYwCVACSpkNyRL2nQ"

# Command handler function
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello, I am your bot!")

def main() -> None:
    # Create the Application object
    application = Application.builder().token(TOKEN).build()

    # Register a command handler
    application.add_handler(CommandHandler("start", start))

    # Start the Bot
    application.run_polling()

if __name__ == "__main__":
    main()
