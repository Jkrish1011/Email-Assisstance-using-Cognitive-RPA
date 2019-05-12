# Import the required module for text 
# to speech conversion
from gtts import gTTS
# This module is imported so that we can 
# play the converted audio
import os
from pygame import mixer # Load the required library
import time

import json

language = 'en'

EmailDict = json.loads("{\"count\":\"10\",\"emails\":[{\"SenderName\":\"Aishwarya Bulbule\",\"RTime\":\"05/11/2019 19:14\",\"Subject\":\"RE: Python Code\"},{\"SenderName\":\"Yallaling Ram Bansode\",\"RTime\":\"05/11/2019 15:42\",\"Subject\":\"Python Code\"},{\"SenderName\":\"Hackathons\",\"RTime\":\"05/11/2019 14:45\",\"Subject\":\"Welcome to UiPath Power Up Automation Hackathon\"},{\"SenderName\":\"EPM Cloud User Feedback\",\"RTime\":\"05/10/2019 21:31\",\"Subject\":\"Feedback: Data export from FCCS to PBCS failing. Service restart was unable\"},{\"SenderName\":\"Lisa Perille\",\"RTime\":\"05/10/2019 22:01\",\"Subject\":\"N. America and India Staffing Schedules\"},{\"SenderName\":\"Huron Helping Hands\",\"RTime\":\"05/11/2019 07:01\",\"Subject\":\"Day of Service 2019 - Thank You!\"},{\"SenderName\":\"Aishwarya Bulbule\",\"RTime\":\"05/11/2019 11:00\",\"Subject\":\"Missed conversation with Aishwarya Bulbule\"},{\"SenderName\":\"Aishwarya Bulbule\",\"RTime\":\"05/11/2019 11:34\",\"Subject\":\"https://speechnotes.co/\"},{\"SenderName\":\"Aishwarya Bulbule\",\"RTime\":\"05/11/2019 11:37\",\"Subject\":\"video link\"},{\"SenderName\":\"Microsoft Azure\",\"RTime\":\"05/11/2019 12:23\",\"Subject\":\"Welcome to Cognitive Services!\"}]}")
# EmailDict = {
# 	"count":1,
# 	"emails":{
# 		{
# 			"SenderName":"Aishwarya Bulbule",
# 			"RTime":"05/11/2019 19:14",
# 			"Subject":"RE: Python Code"
# 		},
# 	}
# }

if(EmailDict["count"] == 1):
	ToPronounce = "There was just "+ EmailDict["count"]+ " Email"
else:
	ToPronounce = "There were "+ EmailDict["count"] +" Emails"


language = 'en'
myobj = gTTS(text=ToPronounce, lang=language, slow=False)
myobj.save("welcome.mp3")
mixer.init()
mixer.music.load('welcome.mp3')
mixer.music.play()
while mixer.music.get_busy():		
	time.sleep(1)

mixer.quit()

os.remove('welcome.mp3')

time.sleep(2)

ToPronounce = "Starting"


language = 'en'
myobj = gTTS(text=ToPronounce, lang=language, slow=False)
myobj.save("welcome1.mp3")
mixer.init()
mixer.music.load('welcome1.mp3')
mixer.music.play()

while mixer.music.get_busy():		
	time.sleep(2)

time.sleep(1)

mixer.quit()

try:
	os.remove('welcome1.mp3')
except Exception as e:
	os.remove('welcome1.mp3')

print("Removed welcome after pronouncing starting......")

time.sleep(2)



for i in EmailDict["emails"]:

	ToPronounce = ""
	ToPronounce = "The sender Name was " +i["SenderName"]+" with subject line "+i["Subject"] +". The email was received by "+i["RTime"]
	language = 'en'
	myobj = gTTS(text=ToPronounce, lang=language, slow=False)
	myobj.save("welcome.mp3")
	mixer.init()
	mixer.music.load('welcome.mp3')
	mixer.music.play()
	while mixer.music.get_busy():		
		time.sleep(2)

	mixer.quit()
	os.remove('welcome.mp3')

