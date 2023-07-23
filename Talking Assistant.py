# talkingassistant
import pyttsx3
friend = pyttsx3.init()
friend.say("Keep quiet and support Man Utd")
friend.runAndWait()

#2nd one
speech = input("say it: ")
friend.say(speech)
friend.runAndWait()
