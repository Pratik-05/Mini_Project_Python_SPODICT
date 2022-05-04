import pyttsx3
from PyDictionary import PyDictionary
  
  
class Speaking:
  
    def speak(self, audio):
        
        # Having the intial constructor of pyttsx3 
        # and having the sapi5 in it as a paramater
        engine = pyttsx3.init('sapi5')
          
        # Calling the getter and setter of pyttsx3
        voices = engine.getProperty('voices')
          
        # Method for the speaking of the the assistant
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()
  

def Dictionary(query):
    dic = PyDictionary()
    word = dic.meaning(query)
    return word
      
        # Taking the string input
        # if word:
        #     print(len(word))
              
            # for state in word:
            #     print(word[state])
            # speak.speak("the meaning  is" + str(word[state]))
        # else:
            # speak.speak("No Meaning found Try again" )

  
  
