import datetime
import time
import pytz
import requests
import tempfile

class User():

  def __init__(self, bot):
    self.bot = bot
    self.id_pribadi = ''
    self.id_log = ''

  def log(self, message, perintah):
    log = f"""{ datetime.datetime.now( pytz.timezone('Asia/Jakarta') ).strftime('%Y-%m-%d %H:%M:%S') } > 
    {message.from_user.first_name} {message.from_user.last_name} > {perintah}"""
    self.bot.send_message(self.id_log, log)

  def get_api(self, url):
    response = requests.get("https://tiktok-api.qadrillahstorag.repl.co/Tiktok?url=" + url)
    return response.json()

  def download_video(self, url):
    response = requests.get(url, stream=True)
    with tempfile.NamedTemporaryFile() as fp:
      with open(fp.name + '.mp4', 'wb') as file:
        file.write(response.content)
      return fp.name + '.mp4'

# user = User('asf')
# file = user.download_video('https://s1.ssstik.top/ssstik/2edd0119ec30149ea118468d80c74e6e')
# print(file)


