"""
Speech Recognition and print the words or
Sentences Using python
"""
"""
 * Basic and Funtional. 
 * Uses google API (means needs Internet Connection)
"""

def SpeechRecognisor():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:  #Use the microphone of the pc 
        print("Say something\n")     #print this before listening to
        audio = r.listen(source)     #listen using the microphone

        text = r.recognize_google(audio)  
        return (text)        #print what are said


