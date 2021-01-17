
import pyttsx3
import speech_recognition as sr
from tkinter import *

import ticTacToe
import subprocess
import os
import webbrowser as wb
import wikipedia


import sqlite3

con = sqlite3.connect("AI.db")
cur = con.cursor()

engine = pyttsx3.init()


def speak(audio):
    """
    This function created to make the computer say things .
    Args:
        audio ([str]): [what the computer will say .]
    """
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """
    this function created to insert input to the AI assistent using a microphone .

    Returns:
        [str]: [The users input using a microphone]
    """
    # a recognizer instance to recognize a speech .
    r = sr.Recognizer()
    # get the speech entered by the user to the mic .
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold = 1
        # audio is the speech
        audio = r.listen(source)

    try:
        print("Recognizing .... ")
        # recognize what the user said using 'recognize_google' function then print it .
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        # if it didnt recognize then print this .
        print(e)
        print("Say that again please ... ")
        return "None"

    return query
    

def LetsTalk():

    user_answer = takeCommand()
        
    data = cur.execute("SELECT * FROM questions_answers").fetchall()
    
    for info in data:
        question, answer = info
        if question == user_answer.lower():
            speak(answer)
            break

def greetings():
    speak("Hello ! i Am Your personal assistent . my name is jacky jack x 1 y 5")
    speak("Please tell me how can i help you ...")

def anythingElseSir():
    speak("Would you like me to do anything else sir ?")

def okImListening():
    speak("Waiting for your request sir !")

def sayGoodbye():
    speak("fine ...")
    speak("I was glad to help you !")
    speak("Please tell me if you need anything else !")
    speak("See you later !")

def startAI():
    """
    this fucntion will be the function shat start the program .
    while this function works -> the AI assistent is still on .
    """
    # AI introduce itself . then it aks how can he help you .
    greetings()

    while True:
        # the user say to the mic how can the AI assistent help him and store it in this variable 'users_request' .
        users_request = takeCommand()

        # if the user said somethig with 'play' and 'game' in the senetence -> the AI assistent will play tic and toe with him .
        if 'play' and 'game' in users_request.lower():
            speak("okay sir , lets play a game !!")
            speak("You can go first . Please mark one of the places ...")
            ticTacToe.TicTacToe()

        # if the user say 'open' then something else .
        elif 'open' in users_request.lower():
            
            # if the user say 'calculator' in that sentence -> open calculator .
            if 'calculator' in users_request.lower():
                speak("Opening Calculator ...")
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')

            # if the user say 'word' in that sentence -> open word .
            elif 'ward' in users_request.lower():
                speak('Opening MS word ...')
                ms_word = r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
                os.startfile(ms_word)

            # if the user say 'excel' in that sentence -> open excel .
            elif 'excel' in users_request.lower():
                speak("Opening MS excel ... ")
                ms_excel = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
                os.startfile(ms_excel)

            # if the user say 'powerPoint' in that sentence -> open power point .
            elif 'powerpoint' in users_request.lower():
                speak("Opening MS power point ... ")
                ms_powerPoint = r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
                os.startfile(ms_powerPoint)

            # if the user say 'publisher' in that sentence -> open publisher .
            elif 'publisher' in users_request.lower():
                speak("Opening MS publisher ... ")
                ms_publisher = r"C:\Program Files (x86)\Microsoft Office\root\Office16\MSPUB.EXE"
                os.startfile(ms_publisher)

            # user say 'google' in that sentence -> open google .
            elif 'google' in users_request.lower():
                speak("Opening google ... ")
                wb.open('https://www.google.com')

            # user say 'youtube' in that sentence -> open youtube .
            elif 'youtube' in users_request.lower():
                speak("Opening youtube ... ")
                wb.open('https://www.youtube.com')

            # user say 'facebook' in that sentence -> open facebook .
            elif 'facebook' in users_request.lower():
                speak("Opening facebook ... ")
                wb.open('https://www.facebook.com')

            # the user say other website -> the AI assistent ask him if its a website -> open the website .
            else:
                speak("Is that a website sir ?")
                user_answer = takeCommand()
                if user_answer.lower() == 'yes':
                    users_request_split = users_request.split()
                    wb.open('https://www.{}.com'.format(users_request_split[-1]))
                else:
                    speak("Sorry sir . dont know how to do it .")

        # if user say search in the sentence 
        elif 'search' in users_request.lower():

            # and youtube in the same sentence -> searching 'search_Term' on youtube .
            if 'youtube' in users_request.lower():
                speak('What should i search ?')
                search_Term = takeCommand().lower()
                speak("Ok sir . searching {} on Youtube".format(search_Term))
                wb.open('https://www.youtube.com/results?search_query='+search_Term)

            # and google in the same sentence -> searching 'search_Term' on google .
            elif 'google' in users_request.lower():
                speak('What should i search ?')
                search_Term = takeCommand().lower()
                speak("Ok sir . searching {} on google".format(search_Term))
                wb.open('https://www.google.com/search?q='+search_Term)

            # and 'wikipedia' in the same sentence -> searching 'search_Term' in wikipedia .
            elif 'wikipedia' in users_request.lower():
                speak("What would you like to know ?")
                search_Term = takeCommand().lower()
                speak("Searching {} on wikipedia".format(search_Term))
                # then get a summary from wikipedia about waht the user said to the mic .
                result = wikipedia.summary(search_Term, sentences=3)
                # the print and say what was found in wikipedia .
                speak('According to wikipedia')
                speak(result)
        
        # the user say that he wants to talk to the AI assistent .
        elif 'lets' and 'talk' in users_request:
            speak("Ok sir . Ask me anything you want .")

            while True:
                # if the user ask a question that is not in db -> the AI assistent will ask him to teach him the answer to that question .
                statment = False

                # user ask AI assistent a question .
                users_question = takeCommand()

                # then i search this question in db -> if that question is in db then the AI assistent will tell the answer and mark 'statment' = True .
                data = cur.execute("SELECT * FROM questions_answers").fetchall()
                for info in data:
                    question, answer = info
                    if question == users_question.lower():
                        speak(answer)
                        statment = True
                        break

                # otherwise the 'statment' will stay False -> means the question the user asked is not in db -> user teach the AI assistent the answer to that question .
                # then it will be stored in db (stord if the user teach the answer) , if the user use wikipedia it will not be stored .
                if statment == False:
                    speak("I dont know the answer to this question sir .")
                    speak("Would you like to teach me the answer to that question ?")
                    speak("Or should i search this on wikipedia ?")

                    # user tell AI if he wants to teach him the answer or AI will search it on wikipedia .
                    users_answer = takeCommand()
                    
                    # the user tell AI to search it on wikipedia .
                    if 'search' and 'wikipedia' in users_answer.lower():
                        speak("Searching {} on wikipedia".format(users_question))
                        # then get a summary from wikipedia about waht the user said to the mic .
                        result = wikipedia.summary(users_question, sentences=3)
                        # the print and say what was found in wikipedia .
                        speak('According to wikipedia')
                        speak(result)
                    
                    # the user tell AI that he wants to give him the answer for that question .
                    elif 'teach' and 'you' in users_answer.lower():
                        speak("Ok sir . im listining ...")
                        users_answer = takeCommand()

                        # AI assistent make sure that he got the answer right .
                        speak("The answer is .")
                        speak(users_answer)
                        speak("Did i got the answer right sir ?")
                        yes_or_no = takeCommand()

                        # if yes -> store it in db .
                        if yes_or_no.lower() == 'yes':
                            query = "INSERT INTO questions_answers (questions, answers) VALUES (?, ?)"
                            cur.execute(query, (users_question, users_answer))
                            con.commit() 

                        # if no -> ask again until gets the right answer .
                        else:
                            while True:
                                speak("sorry sir . please say it again .")
                                users_answer = takeCommand()
                                speak("The answer is .")
                                speak(users_answer)
                                speak("Did i got the answer right sir ?")
                                yes_or_no = takeCommand()
                                if 'yes' in yes_or_no.lower():
                                    query = "INSERT INTO questions_answers (questions, answers) VALUES (?, ?)"
                                    cur.execute(query, (users_question, users_answer))
                                    con.commit()
                                    
                    else:
                        speak("Cant do that sir .")
                        
                
                # afther the AI assistent got the answer , he ask if the user wants to give him more questions .
                # is the user say 'no' -> break out of the 'lets talk' statment .
                speak("Do you have any other questions sir ?")
                user_answer = takeCommand()
                if user_answer == 'no':
                    break
                
                # the while loop in 'lets talk' statment will be activated all over .
                speak("Ok sir . Ask me anything you want ")



        anythingElseSir()
        users_request = takeCommand()

        if 'no' in users_request.lower():
            sayGoodbye()
            break
        else:
            okImListening()


    
if __name__ == "__main__":
     startAI()





