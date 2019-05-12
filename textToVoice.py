# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os
from pygame import mixer # Load the required library
import time


def TextToSpeech(ToSay):
	language = 'en'
	myobj = gTTS(text=ToSay, lang=language, slow=False)
	myobj.save("welcome.mp3")
	mixer.init()
	mixer.music.load('welcome.mp3')
	mixer.music.play()
	while mixer.music.get_busy():		
		time.sleep(1)
	mixer.quit()
	os.remove('welcome.mp3')

	
	
