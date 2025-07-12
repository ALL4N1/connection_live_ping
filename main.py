from time import sleep
import requests
from datetime import datetime
from notifypy import Notify
import sys
import os

def resource_path(relative_path):
    try:
        # noinspection PyUnresolvedReferences
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def now():
    date = datetime.now()
    min = f'0{date.minute}' if date.minute < 10 else str(date.minute)
    hour = f'0{date.hour}' if date.hour < 10 else str(date.hour)
    second = f'0{date.second}' if date.second < 10 else str(date.second)
    return f'{hour}:{min}:{second}'

def send_notif(title, message, icon_path):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.icon = resource_path(icon_path)
    notification.send(block=False)

def test_connection():
    url = "https://www.google.com"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

starting_time = ""
ending_time = ""

if (test_connection()):
    starting_time = now()
    send_notif("Connection established", "Connection established at " + starting_time, "ok_icon.png")
    print("Connection established at " + starting_time)
else:
    send_notif("No Connection", "No Connection established", "error_icon.png")
    sys.exit()

conn = True
while conn:
    conn = test_connection()
    ending_time = now()
    if not conn:
        print("Connection failed at " + ending_time)
        send_notif("No Connection", "Started at " + starting_time + "\nFailed at " + ending_time, "error_icon.png")
        sys.exit()
    print("Connection good at " + ending_time)
    sleep(30) # sleep for X seconds