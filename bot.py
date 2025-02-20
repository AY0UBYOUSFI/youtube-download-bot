from yt_dlp import YoutubeDL, DownloadError
import telebot



TOKEN = "7423852571:AAFffx0oc9P0hqEagwMYwCVACSpkNyRL2nQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: 'youtube.com' in message.text or 'youtu.be' in message.text)
def handle_youtube_link(message):
    url = message.text
    bot.reply_to(message, "Downloading your video, please wait...")

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4'
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open('video.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)

    except DownloadError as e:
        bot.reply_to(message, f"Failed to download video: {e}")

bot.polling()