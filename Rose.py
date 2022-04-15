# Import Items
import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import smtplib
from keyboard import press_and_release


# Note: I will make it using machine learning !

#Speak function

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine. setProperty("rate", 146)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def flipkart(Item):
    amount = "https://www.flipkart.com/search?q=" + Item
    print("Rose: Searching" + Item + "On Flipkart") 
    speak("Searching " + Item + "On Flipkart") 
    webbrowser.open(amount)    

def amazon(Item):
    price = "https://www.amazon.in/s?k=" + Item
    print("Rose: Searching" + Item + "On Amazon") 
    speak("Searching " + Item + "On Amazon") 
    webbrowser.open(price) 

def music(name):
    song = "https://gaana.com/search/" + name
    print("Rose: Playing Music!")
    speak("Playing Music!")
    webbrowser.open(song)

def google(term):
    information = "https://www.google.com/search?q=" + term
    print("Rose: This is What I Found on the Google!")
    speak("This is What I Found on the Google!")    
    webbrowser.open(information)

def youtubesearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    print("Rose: This is What I Found on the YouTube!")
    speak("This is What I Found on the YouTube!")    
    webbrowser.open(result)

def wishMe():
    name = input("Enter your name: ")
  
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Rose: Good Morning ! " + name)
        speak("Good Morning ! " + name)

    elif hour >= 12 and hour < 18:
        print("Rose: Good Afternoon ! " + name)
        speak("Good Afternoon ! " + name)

    else:
        print("Rose: Good Evening ! " + name)
        speak("Good Evening ! " + name)

# Main Code

if __name__ == "__main__":
    wishMe()
    print("Hello I am Rose!")
    speak("Hello I am Rose!")
    print("Let's tell me How can I help You?")
    speak("Let's tell me How can I help You?,")

while True:

# Tasks that she can do!
    
    hour = int(datetime.datetime.now().hour) 

    task = input("User: ").lower()
    
    if 'time' in task:
        print("Rose: The Time is " + datetime.datetime.now().strftime("%H:%M:%S"))
        speak("The Time is " + datetime.datetime.now().strftime("%H:%M:%S"))    

    elif 'wikipedia' in task:
        print("Rose: Finding Data...")
        speak("Finding Data")
        task = task.replace("wikipedia", "")
        results = wikipedia.summary(task, sentences=4)
        print("Rose:  " + results)
        speak("According to wikipedia, " + results)    
    
    elif 'stop' in task:
        print("Rose: OK! Closing Window...")
        speak("OK! Closing Window.")
        quit() 

    elif 'quite' in task:
        print("Rose: OK! Closing Window...")
        speak("OK! Closing Window.")
        quit() 

    elif 'thank' in task:
        print("Rose: Your Welcome! I glad to help you.")  
        speak("Your Welcome! I glad to help you.")  

    elif 'who are you' in task:
        print("Rose: I am Rose! Your Personal Assistant. Version - 1.8")
        speak("I am Rose! Your Personal Assistant. Version - 1.8") 

    elif 'on google' in task:
        task = task.replace("search", "")
        task = task.replace("on google", "")
        google(task)   

    elif 'play' in task:
        y = task.replace("play", "")
        music(y)

    #elif 'hi' or 'hello' in task:
       # print("Rose: Hi, how are you?")
        #speak("Hi, how are you?")

    elif 'open' in task:
       task = task.replace("open ", "")
       web1 = 'https://www.'+task+'.com'
       print("Rose: Opening " + task)
       speak("Opening " + task)
       webbrowser.open(web1)

    elif 'on youtube' in task:
        task = task.replace("search", "")
        task = task.replace("on youtube", "")
        youtubesearch(task)  

    elif 'on amazon' in task:
        task = task.replace("price", "") 
        task = task.replace("of", "")
        task = task.replace("search", "")
        task = task.replace("on amazon", "")   
        amazon(task)

    elif 'on flipkart' in task:
        task = task.replace("price", "") 
        task = task.replace("of", "")
        task = task.replace("search", "")
        task = task.replace("on flipkart", "") 
        flipkart(task)

    elif 'speak mode on' in task:
        print("Rose: Speak Mode is ON. Tell What Should I speak?")
        speak("Speak Mode is ON. Tell What Should I speak?")
        DATA = input("Enter TEXT: ")
        Freasult = DATA.replace("Enter TEXT:", "")
        speak(Freasult)

 #Mathematics of Rose!
    elif 'add' in task:
        print("Rose: Addition! Alright tell me the numbers.")
        speak("Addition! Alright tell me the numbers.")
        print("Enter First number: ")
        num1 = int(input())
        print("Enter Second number: ")
        num2 = int(input())
        ans = num1 + num2
        print("Rose: The Answer is: " + str(ans))
        speak("The Answer is: " + str(ans))
    elif 'add' in task:
        pass   
    
    elif 'sub' in task:
        print("Rose: Subtraction! Alright tell me the numbers.")
        speak("Subtraction! Alright tell me the numbers.")
        print("Enter First number: ")
        num1 = int(input())
        print("Enter Second number: ")
        num2 = int(input())
        ans_sub = num1-num2
        print("Rose: The Answer is: " + str(ans_sub))
        speak("The Answer is: " + str(ans_sub))

    elif 'multiply' in task:
        print("Rose: Multiply! Alright tell me the numbers.")
        speak("Multiply! Alright tell me the numbers.")
        print("Enter First number: ")
        num1 = int(input())
        print("Enter Second number: ")
        num2 = int(input())
        ans_mul = num1*num2
        print("Rose: The Answer is: " + str(ans_mul))
        speak("The Answer is: " + str(ans_mul))

    elif 'divide' in task:
        print("Rose: Divide! Alright tell me the numbers.")
        speak("Divide! Alright tell me the numbers.")
        print("Enter First number: ")
        num1 = int(input())
        print("Enter Second number: ")
        num2 = int(input())
        ans_div = num2 // num1, num2 % num1
        print("Rose: The Quotient and Remainder is: " + str(ans_div))
        speak("The Quotient and Remainder is: " + str(ans_div))

    else:
        print("Rose: Sorry! Please check that your spelling should right or it is possible that, This Function is not Available.")
        speak("Sorry! Please check that your spelling should right or it is possible that This function is not available.")
