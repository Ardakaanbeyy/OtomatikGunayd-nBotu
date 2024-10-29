import pywhatkit
import datetime
import time
import random
import pyautogui

zamanlar = ["07:35", "07:46" "07:52"]
guno = ["Gunaydınnn", "Gunaydınn", "gunaydınn"]
WIDTH, HEIGHT = pyautogui.size()
send_time = random.choice(zamanlar)
msg = (random.choices(guno))
to_number = "+90xxxcccbbbb"

send_time_hour = int(send_time.split(":")[0])
send_time_minute = int(send_time.split(":")[1])

send_time_ = datetime.datetime.now().replace(hour=send_time_hour, minute=send_time_minute, second=0, microsecond=0)

if send_time_ < datetime.datetime.now():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    send_time_ = datetime.datetime.combine(tomorrow, datetime.time(send_time_hour, send_time_minute))

later_1min = send_time_ + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    if now.hour == send_time_hour and now.minute == send_time_minute and now.day == send_time_.day:
        deneme = random.choice(guno)
        pywhatkit.sendwhatmsg(to_number, deneme, send_time_hour, send_time_minute + 1)
        print("mesaj gönderildi - {now}")

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        send_time = send_time_ + datetime.timedelta(minutes = 1)
        pyautogui.click(WIDTH / 2, HEIGHT / 2 + 15)
    time.sleep(60)