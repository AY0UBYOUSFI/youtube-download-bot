import logging
import yt_dlp
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your Telegram Bot Token
TOKEN = '7423852571:AAFffx0oc9P0hqEagwMYwCVACSpkNyRL2nQ'

# Function to download the video using yt-dlp
def download_video(url: str):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'best',
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return filename
    except Exception as e:
        logger.error(f"Error downloading video: {e}")
        return None

# Command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a YouTube link to download the video.')

# Command handler for downloading the video
def download(update: Update, context: CallbackContext) -> None:
    if context.args:
        url = context.args[0]
        update.message.reply_text('Downloading your video, please wait...')
        video_file = download_video(url)
        
        if video_file:
            update.message.reply_text(f'Video downloaded successfully! You can find it here: {video_file}')
        else:
            update.message.reply_text('Failed to download the video. Please check the URL or try again later.')
    else:
        update.message.reply_text('Please provide a YouTube video URL.')

# Main function to set up the bot
def main():
    # Create an Updater object and attach the dispatcher
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
