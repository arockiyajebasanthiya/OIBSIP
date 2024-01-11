import speech_recognition as sr
import subprocess
import wolframalpha
import pywhatkit
import schedule
import time
import smtplib
import pywhatkit
import tkinter as tk
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

now = datetime.datetime.now()
hour = int(now.hour)
def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def wishMe():
      ampm = now.strftime("%p")
      if hour>= 0 and hour<12 and ampm=='AM':
            speak("Good Morning!")
      elif hour>= 12 and hour<16 and ampm=='PM':
            speak("Good Afternoon!")
      elif hour>=16 and hour<19 and ampm=='PM':
            speak("Good Evening!")

      else:
            speak("Good Night!") 

      assname =(" 1 point o")
      speak("I am your Assistant")
      speak(assname)

def calculate(expression):
    result = float(eval(expression))
    print(result)
    return result


def username():
      try:
            speak("What should i call you ")
            uname = voice_assistant()
            speak("Welcome")
            speak(uname)
            columns = shutil.get_terminal_size().columns
            print("************".center(columns))
            print("Welcome Mr/Miss.", uname.center(columns))
            print("***********".center(columns))
            
            speak("How can i Help you")
      except:
            speak('sorry I can\'t hear you voice')

def voice_assistant():
      r = sr.Recognizer()
      with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 1
          audio = r.listen(source)
      try:
          print("Recognizing...") 
          query = r.recognize_google(audio, language ='en-in')
          print(f"User said: {query}\n")
          return query

      except Exception as e:
          print(e) 
          print("Unable to Recognize your voice.") 
          return "None"

def sendEmail(to,content):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    s.starttls()
    s.login("Sender EmailId", "Password")
    s.sendmail("Sender EmailId",to, content)
    s.quit()


def send_sms():
      speak("Tell me county code of receiver")
      code=voice_assistant()
      speak("Tell me receiver phone no")
      no=voice_assistant()
      speak("Tell me the message to send")
      msg=voice_assistant()
      minute=int(now.minute)
      pywhatkit.sendwhatmsg('+'+code+no, msg,hour ,minute+3 )

if __name__ == '__main__':
      clear = lambda: os.system('cls')
      clear()
      wishMe()
      username()
      
      while True:
            
                query = voice_assistant().lower()
                if 'send email' in query or 'send mail' in query:
                      try:
                          speak("What should I say?")
                          content = voice_assistant()
                          to = "Receiver Email Id"
                          sendEmail(to, content)
                          speak("Email has been sent !")
                      except Exception as e:
                                print(e)
                                speak("I am not able to send this email")

                elif 'message' in query or 'chat' in query:
                      try:
                            send_sms()
                      except Exception as e:
                             speak(e)
                            

                elif 'open youtube' in query or 'youtube' in query:
                        speak("Here you go to Youtube\n")
                        webbrowser.open("youtube.com")

                elif 'date'in query :
                        now=time.ctime()
                        speak(f"Today date is {now}")

                elif 'open google' in query or 'google' in query:
                        speak("Here you go to Google\n")
                        webbrowser.open("google.com")

                elif 'how are you' in query:
                        speak("I am fine,Thank you")
                        speak("How are you")

                elif 'open stack overflow' in query:
                        speak("Here you go to Stack Over flow.Happy coding")
                        webbrowser.open("stackoverflow.com")

                elif 'thank you' in query:
                        speak("You are welcome!If you have any more updates or questions,feel free to share!")


                elif 'play music' in query or "play song" in query:
                      try:
                              speak("Here you go with music")
                              #copy your diectory path
                              directory="E:\\Intern\\Oasis\\music"
                              files = os.listdir(directory)
                              for file in files:
                                    if file.endswith(".mp3") or file.endswith(".wav") or file.endswith(".ogg"):
                                          print(file)
                                          playsound.playsound(directory+'\\'+file)
                                    speak("Do you like to play next song")
                                    s=voice_assistant().lower()
                                    if 'yes' in s:
                                           break
                      except Exception as e:
                              speak(e)
                  


                elif "calculator" in query:
                      try:
                            
                            text=voice_assistant()
                            result = calculate(text)
                            speak(result)

                      except Exception as e:
                              speak(e)
                              

                elif "open wikipedia" in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences = 3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                elif "Good Morning" in query:
                        speak("A warm" +query)
                        speak("How are you")
                        speak(assname)

                elif 'write note' in query:
                      try:
                            speak("Tell me file name")
                            filename=voice_assistant()
                            f=open(filename+'.txt', 'w')# your file path
                            speak('List the items to store or say stop to exit\n') 
                            while True:
                                line = voice_assistant().lower()
                                if  'stop' in line:
                                    break
                                f.write(line + '\n')

                            speak('Items saved successfully')
                            f.close()
                      except Exception as e:
                           speak(e)
                                  

                elif "show note" in query:
                      try:
                              speak("Showing Notes")
                              file = open("notes.txt", "r") #write your own path
                              print(file.read())
                              speak(file.read(6))
                      except Exception as e:
                            print(e)
                            speak(e)

                elif "weather" in query:
                        api_key = "Api key"
                        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                        speak(" City name ")
                        print("City name : ")
                        city_name = voice_assistant()
                        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                        response = requests.get(complete_url) 
                        x = response.json() 
                        
                        if x["code"] != "404": 
                                y = x["main"] 
                                current_temperature = y["temp"] 
                                current_pressure = y["pressure"] 
                                current_humidiy = y["humidity"] 
                                z = x["weather"] 
                                weather_description = z[0]["description"] 
                                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
                        
                        else: 
                                speak(" City Not Found ")

                elif "log off" in query or "sign out" in query:
                        speak("Make sure all the application are closed before sign-out")
                        time.sleep(5)
                        subprocess.call(["shutdown", "/l"])

                elif "who are you" in query:
                        speak("I am your virtual assistant created by Sandy")

                elif 'time' in query:
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        print(current_time)
                        speak(f"Time\t{current_time}")
                elif 'who created you' in query:
                        speak("I have been created by Sandy")

                elif "location" in query:
                        query = query.replace("where is", "")
                        location = query
                        speak("User asked to Locate")
                        speak(location)
                        webbrowser.open("https://www.google.nl / maps / place/" + location + "")

                elif 'exit' in query:
                        speak("Are you sure?")
                        c=voice_assistant().lower()
                        if 'yes'in c:
                                speak("Thank you for giving me your time")
                                exit()

                elif 'open chrome' in query:
                      webbrowser.open('chrome.com')

                elif 'open whatsapp' in query:
                      from AppOpener import open
                      open('whatsapp')

                elif 'open telegram' in query:
                      from AppOpener import open
                      open('telegram')

                elif 'search' in query:
                      try:
                          query = voice_assistant()

                          for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                                print(j)

                      except Exception as e:
                            speak(e)


                else:
                        speak("I can't understand you")
                                








 
                
                        



