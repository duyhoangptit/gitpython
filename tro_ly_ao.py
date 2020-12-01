# speech recognition(nhan dang giong noi)
# pip install speechrecognition
# pip install pyaudio
import speech_recognition
import pyttsx3
from datetime import date, datetime

rebot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""

while True:
    # bat cai mic len
    with speech_recognition.Microphone() as mic:
        print('Robot: I\'m Listening')
        audio = rebot_ear.listen(mic) # nghe xong r thi se tat mic di
    # Nhan dien am thanh recognize
    print("Robot: ...")
    try:
        you  = rebot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)
    if you == '':
        robot_brain='I can\' hear you, try again'
    elif 'hello' in you:
        robot_brain='Hello tiger'
    elif 'today' in you:
        today = date.today()
        print("Today's date: ", today)
        robot_brain=today.strftime("%B %d, %Y")
    elif 'time' in you:
        now=datetime.now()
        robot_brain=now.strftime("%H hours %M minutes %S seconds")
    elif "bye"  in you:
        robot_brain="Bye tiger"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain='I\'m fine thank you and you'

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()





# pip install pyttsx3
# pip install pipwin
# pipwin install pyaudio
# pip install pythoncom -> pip install pywin32
