from yt_dlp import YoutubeDL, DownloadError
import telebot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



TOKEN = "7423852571:AAFffx0oc9P0hqEagwMYwCVACSpkNyRL2nQ"



# Function to handle the /start command
def start(update, context):
    update.message.reply_text("Send me a YouTube URL to download the video.")

# Function to download the video
def download_video(update, context):
    # Get the URL from the message
    url = update.message.text

    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best',  # Download the best quality video
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save video to the 'downloads' folder with the title as filename
        'quiet': True,  # Suppress unnecessary output
    }

    try:
        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'video')
            video_file = f"downloads/{video_title}.mp4"  # Set the file name of the downloaded video
            update.message.reply_text(f"Video downloaded: {video_title}")

            # Send the downloaded video to the user
            with open(video_file, 'rb') as f:
                update.message.reply_video(f)

    except Exception as e:
        update.message.reply_text(f"Failed to download video: {e}")

# Set up the bot
def main():
    # Create an Updater object using your bot's token
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers for commands and messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))  # Handle any message that is not a command

    # Start polling for new messages
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
