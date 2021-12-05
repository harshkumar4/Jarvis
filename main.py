import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import json

def speak(text):    
    jarvis = pyttsx3.init('sapi5')
    jarvis.say(text)
    jarvis.runAndWait()

def wish():
    if int(datetime.datetime.now().hour) > 0 and int(datetime.datetime.now().hour) < 12 :
        speak('Good Morning')

    elif int(datetime.datetime.now().hour) >= 12 and int(datetime.datetime.now().hour) < 16 :
        speak('Good Afternoon')
    
    else:
        speak('Good Evening')

def listen():
    mac=sr.Recognizer()
    with sr.Microphone() as mic:
        print('\nListening...')
        mac.pause_threshold=1
        words=mac.listen(mic)
        
    try:
        print('Recognizing...')
        query=mac.recognize_google(words,language='en-in')
    
    except Exception as e:
        print("Something Went Wrong")
        print("Say that again")
        return "None"
    return query

def actions(query):

    if "open google" in query:
        webbrowser.open("google.com")
        return


    elif "open youtube" in query:
        webbrowser.open("youtube.com")
        return


    elif "open github" in query:
        webbrowser.open("github.com")
        return


    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")
        return


    elif "wikipedia" in query:
        print("Searching Wikipeda...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        print("According to Wiki : ",results)
        speak(results)


    elif "add command" in query:
        admore()


    elif query in ["exit","quit","none"]:
        exit()


    else:
        with open("jarvis.json","r") as file:
            dat = json.load(file)
            if query in dat:
                os.startfile(dat[query])
            del dat

def takecomm():
    key = input("\nEnter your Command : ")
    path = input("Enter your Path : ")
    path.replace("\\","\\\\")
    dic[key] = path

def admore():
    print("\nIf you Want to add your own commands like 'play music' than to open/play that, you will have to specify\npath of your file/application.")
    while True:
        dec = input("\nWant to add more [y/n] : ").lower()
        if dec == "y":
            takecomm()
            continue

        elif dec == "n":
            if len(dic) != 0:
                if os.path.getsize("jarvis.json"):
                    with open("jarvis.json","r") as file:
                        data = json.load(file)
                    data.update(dic)        #dic is the dictionary with your new data
                    with open("jarvis.json","w") as file:
                        json.dump(data,file)
                else:
                    with open("jarvis.json","w") as file:
                        json.dump(dic,file)
                break
            break

        else:
            print("INVALID INPUT!\nTry again!")
            continue




if __name__ == "__main__":
    dic = {}
    if not os.path.exists("jarvis.json") :
        with open("jarvis.json","w"):
            pass
        print("Hello User!\nI am FRIDAY, An AI assistant developed by Kratøs!, you can use me to set your own commands and to perform those actions.")
        speak("Hello User! I am FRIDAY, An AI assistant developed by Kratos!, you can use me to set your own commands and to perform those actions.")
        print("Here are few by Default commands and thier actions : ")
        speak("Here are few by Default commands and thier actions : ")
        print("Say 'Open Google' : To open Google Search")
        print("Say 'Open Youtube' : To open Youtube.com")
        print("Say 'Open Github' : To open Github.com")
        print("Say 'Open Whatsapp' : To open WhatsApp Web")
        print("Say 'Wikipedia' + your query : To get summary of your query from wikipedia")
        print("Say 'add command' : To add your own commands to perform a task")
        admore()

    wish()
    speak('How can i help you?')
    print('\nHow can i help you?')
    que=listen().lower()
    print(f"User Said : {que}")
    speak(que)
    actions(que)