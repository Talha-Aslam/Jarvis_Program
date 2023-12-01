'''
google ya kisi bi cheez ko kholy or chalaay
'''
import pywhatkit
from pywikihow import WikiHow,search_wikihow# how walo ko sesarch kiya
import pyttsx3
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[5].id)
engine.setProperty('rate',130)  
def speak(audio):
    print("     ")
    print(f"Computer : {audio}")
    print("     ")
    engine.say(audio)
    engine.runAndWait()

def GoogleSearch(text):
    
    O_query = str(text)#storing the orignal text in O-query
    pywhatkit.search(O_query)

    if 'how to' in O_query:
        how_to_func = search_wikihow(query= O_query,max_results=2)# btao search kya kar rahyy
        assert len(how_to_func ) == 2#line by line likhta
        how_to_func[0].print()
        speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(O_query,2)
        speak(f"According to my research   {search}")

def Youtube_Search(text):
    result = "https://www.youtube.com/results?search_query=" + text
    import webbrowser as web
    web.open(result)
    speak("Here is your result Sir")

def Youtube_play_video(text):

    pywhatkit.playonyt(text)
    
    speak("Command executed Sir")
    
# Youtube_play_video("who is mubeen")