''''
# ya library computer kay speaker sy kuch bi bolwany ka liya hai or  speed or voice change kae sakty ya is ki koi bi setting
# we can do listen to the voice directly by 
'''
import pyttsx3
#--> pyttsx3.speak("Hello guys how are u ")
'''
# mick sy awaz suny or samajny kya liya
'''
import speech_recognition as sr



from Automation import WhatsappMsg
'''
#now we have to create or initiaize a engine (main part) 
# sapi5 driver controle hardware and software or setting kary ga voice ki 
#sapi5 is a voice driver :)
'''
engine = pyttsx3.init('sapi5')

#now we will get the voices of different persons from the system and store it in variable named as voices
voices = engine.getProperty('voices')

#now to set our own custom person voice we will set the id of the voice
engine.setProperty('voice',voices[5].id)

#We can change the speed of a voice
engine.setProperty('rate',130)  

#Now we are creating a function to run the voice engine and command it to say what we want
def speak(audio):
    print("     ")
    print(f"Computer : {audio}")
    print("     ")
    '''
    yaha computer boly ga q ka engine pyttex ka varibale tha or os ka kam copmuter sy bulwana 
    '''
    engine.say(audio)
    engine.runAndWait()
'''
mick sy awaz ko suny ga ya fuction
'''
def takecommand_English():
     r = sr.Recognizer()

     with sr.Microphone() as source:
          print("Listning...")

          r.pause_threshold = 2
          audio = r.listen(source)

          try:
               print("Recgnizing...")
               '''
               goole ko bhaja ya kya bolo raha
               '''
               query = r.recognize_google(audio,language='en-in')
               # print(f"Haniya command : {query}\n")
          except:   
               return ""      
     return query.lower()

#here we will call the function and passing the message which we want him to speak as an argument 
# speak("Hello Haniya how are you, What are u currently doing, are u doing great?")
def automatewhatsapp():
     speak("Tell me the number to whom u want to send msg ")
     number = str(takecommand_English())
     number.replace(" ","")
     print(f"your is {number}")
     speak("Tell) me the message you want to deliver")
     message = str(takecommand_English())
     WhatsappMsg(number,message)

def taskexecution():
     while True:#ak bar suny ka bad dobara chaly 
          text = takecommand_English()
          if "message" in text:
               text = text.replace("whatsapp message","")
               text = text.replace("message","")
               text = text.replace("jarvis","")
               text = text.replace("to","")
               text = text.replace("send","")
               text = text.replace("hi","")
               # automate wala functin yaha call karwa rahy
               automatewhatsapp()

          if "search on google" in text:
                text = text.replace("jarvis","")
                text = text.replace("google search","")
                text = text.replace("search","")
                text = text.replace("tell me","")
                text = text.replace("that","")
                '''
               # feature file sy google wala function import kiya
               '''
                from Feautures import GoogleSearch
                GoogleSearch(text)

          elif "search on youtube" in text:
               text = text.replace("jarvis", "")
               text = text.replace("youtube search", "")
               text = text.replace("on youtube", "")
               text = text.replace("show", "")
               text = text.replace("me", "")
               text = text.replace("that", "")
               text = text.replace("can", "")
               text = text.replace("you", "")
               from Feautures import Youtube_Search 
               Youtube_Search(text)

          elif "play video" in text:
               text = text.replace("jarvis", "")
               text = text.replace("play", "")
               text = text.replace("play video", "")
               text = text.replace("show video", "")
               text = text.replace("show me", "")
               text = text.replace("that", "")
               text = text.replace("can you", "")
               text = text.replace("on youtube", "")
               from Feautures import Youtube_play_video 
               Youtube_play_video(text)

taskexecution()