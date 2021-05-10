import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('voicemailsend37@gmail.com', 'Dvverma0308#')
    email = EmailMessage()
    email['From'] = 'voicemailsend37@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'myself': 'divyansh.03082001@gmail.com',
    'graphic era': 'enquiry@geu.ac.in',
    'papa≥papa': 'vivekverm0110@gmail.com',
    'siddhant': 'singh.sidhant25@gmail.com',
}

def get_mail_info():
    talk('To Whom you want to send your email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email')
    subject = get_info()
    talk('Tell me the body in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey..Your email is successfully delivered')
    talk('Do you want to send mail again')
    send_more = get_info()
    if 'yes' in send_more:
        get_mail_info()

get_mail_info()
