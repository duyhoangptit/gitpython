import pyttsx3

robot_brain="I can't hear you, try again"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

# pip install pyttsx3
# pip install pipwin
# pipwin install pyaudio
# pip install pythoncom -> pip install pywin32
