# speech recognition(nhan dang giong noi)
# pip install speechrecognition
# pip install pyaudio
import speech_recognition

rebot_ear = speech_recognition.Recognizer()
# bat cai mic len
with speech_recognition.Microphone() as mic:
    print('Robot: I\'m Listening')
    audio = rebot_ear.listen(mic) # nghe xong r thi se tat mic di
# Nhan dien am thanh recognize
try:
    you  = rebot_ear.recognize_google(audio)
except:
    you = ""
print("You: " + you)