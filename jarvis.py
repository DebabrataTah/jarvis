from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import requests
import command
import PyAudio


def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say" + audio)


# listening of commands section

def MyCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("you said:" + command + "\n")


    # return back to proceed this process when any error occurs to listen or commands

    except sr.UnknownValueError:
        assistant(MyCommand())

    return command


# if loop statement to execute commands
def assistant(command):
    if 'open Reddit python' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)
    if 'who you are' or 'what is your name' in command:
        talkToMe('I am your friend...Jarvis')
    if 'whats up' in command:
        talkToMe('nothing much and you?')
        me = MyCommand()
        if 'playing with you babe' in command:
            talkToMe('he he i am thats fine dude!!')
    if 'email' in command:
        talkToMe('who is the recipient?')
        recipient = MyCommand()
        if 'aditi' in recipient:
            talkToMe('what should I say her?')
            content = MyCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # identify to server

            mail.ehlo()

            # to encrypt session
            mail.starttls()

            # login

            mail.login('debabrata.tah98@gmail.com', 'QWERTY98@a')

            # send message

            mail.sendmail('aditi', '', content)

            # close mail connection

            mail.close()

            talkToMe('Email has sent')


talkToMe('i am ready for your next cammand')
while True:
    assistant(MyCommand())
