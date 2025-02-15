import random
import string
import time
from twilio.rest import Client

# Function to generate a secure password
def generate_password(length=12, use_digits=True, use_specials=True, avoid_similar=True):
    chars = string.ascii_letters  # a-z, A-Z
    
    if use_digits:
        chars += string.digits
    
    if use_specials:
        chars += string.punctuation

    if avoid_similar:
        similar_chars = "O0Il1"  # Characters to avoid
        chars = ''.join(c for c in chars if c not in similar_chars)

    password = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    return password

# Function to send SMS alert using Twilio
def send_sms(new_password):
    account_sid = "your_twilio_account_sid"  # Replace with your Twilio Account SID
    auth_token = "your_twilio_auth_token"  # Replace with your Twilio Auth Token
    twilio_phone_number = "+1234567890"  # Replace with your Twilio phone number
    recipient_phone_number = "+0987654321"  # Replace with recipient's phone number

    client = Client(account_sid, auth_token)
    
    message_body = f"🔐 New Password: {new_password}\nThis will refresh in 10 minutes."

    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print(f"✅ SMS sent successfully! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")

# Auto-refresh password every 10 minutes
while True:
    new_password = generate_password(length=16, use_digits=True, use_specials=True, avoid_similar=True)
    print("\n🔐 New Password:", new_password)
    print("📱 Sending SMS alert...")

    send_sms(new_password)

    print("🔄 Refreshing in 10 minutes...\n")
    time.sleep(600)  # Wait for 10 minutes (600 seconds)
