from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Your bot token
TOKEN = "7423852571:AAFffx0oc9P0hqEagwMYwCVACSpkNyRL2nQ"

# Command handler function
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello, I am your bot!")

def main() -> None:
    # Create the Updater object (without use_context)
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == "__main__":
    main()
