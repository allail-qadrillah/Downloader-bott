from telebot import telebot, types
import os
from dotenv import load_dotenv
from models import User

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN_BOT'))
user = User(bot)
user.id_pribadi = os.getenv('ID_PRIBADI')
user.id_log = os.getenv('ID_LOG')

@bot.message_handler(commands=['start'])
def downloadvidtiktok(message):
    user.log(message, 'start')
    bot.send_message(message.chat.id, 
    f'''Halo {message.from_user.first_name} 🙌
saya Downloader_bot yang akan membantu anda mengunduh konten social media, berikut command yang tersedia :
1️⃣ Tiktok
1. download video tiktok nowm = paste url di chat 
kalo mau unduh musik click button yakk''')
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton(
        'Message Developer 🧑🏻‍💻', url='https://telegram.me/Qadrillah')
    markup.row(item)
    bot.send_message(
        message.chat.id, 'jika ada fitur yang ingin ditambahkan ataupun bot terdapat masalah, bisa klik button dibawah sobb 👇', reply_markup=markup)
    bot.send_message(user.id_pribadi, f"{message.from_user.first_name} {message.from_user.last_name} - {message.chat.id}")

callbackOriTiktok =[]
callbackVidTiktok =[]
@bot.message_handler(regexp='https://vt.tiktok.com/')
def downloadvidtiktok(message):

  bot.send_chat_action(message.chat.id, "upload_video")
  response = user.get_api(message.text)
  if response['status'] == True:
    try:
      url_nowm = response['data'][0]['Without watermark']
      # url_music = response['data'][4]['Without watermark']

      video = user.download_video(url_nowm)
      bot.send_chat_action( message.chat.id, "upload_video" )
      bot.send_video( message.chat.id, open(video, 'rb') )
      user.log(message, f'Download video Tiktok {message.text}')
    except as e:
      bot.send_message(message.chat.id, 'gabisa mendownload 😢')

  else :
    bot.send_message(message.chat.id, 'url tidak valid?')



bot.send_message(user.id_pribadi, "bot starting!")
print("bot  running...!! ")
bot.polling() 