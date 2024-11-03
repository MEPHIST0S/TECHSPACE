import random
import string
from flask_mail import Message
from app import mail

def generate_otp(length=6):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp

def send_otp_email(user_email, otp):
    """Send an OTP email to the user."""
    msg = Message('Your OTP Code', recipients=[user_email])
    msg.body = f'Your OTP code is {otp}. Please use this code to complete your registration.'
    mail.send(msg)