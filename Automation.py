from Credentials import mobileno, token, messages
import random
import requests
import schedule
import time
print("Automation Script Running...")

url = "https://api.ultramsg.com/instance167125/messages/chat"

def send_sms():

    message = random.choice(messages)

    data = {
        "token": "nt0z0phkp8ogjc59",
        "to": mobileno,
        "body":f"Hey, Aaisha! 🧚🏻\\n{message}",
        "priority": "10"
    }

    try:
        response = requests.post(url, data=data)
        print(f"Sent: '{message}' | Response: {response.text}")
        print(f"Status: {response.json().get('sent', 'False')}")

    except Exception as e:
        print(f"Error: {e}")

schedule.every().day.at("6:00").do(send_sms)
# schedule.every(10).seconds.do(send_sms)

while True:
    schedule.run_pending()
    time.sleep(1)

