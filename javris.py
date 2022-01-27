#py -3 -m pip install puttsx3  and pip install speech recognition in cmd

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia                                             #pip install wikipedia
import smtplib                                               #for sending emails
import webbrowser as wb                                      #for searching in chrome
import os            #builtin
import pyautogui
import psutil        #pip install psutil
import pyjokes 

engine = pyttsx3.init()                                      #it initializes the pyttsx3 module
voices = engine.getProperty('voices')                        # it guides the voice property from module pyttsx3
engine.setProperty('voice',voices[1].id)	                 #get a list of voices and we can choose one choice 0-male 1-female
newVoiceRate = 170                                           #by default the speed of voice rate will be 200 words per minute we r setting it to 190
engine.setProperty('rate',newVoiceRate)                      # it calls the 'rate' from pyttsx3 


def speak(audio):
	engine.say(audio)                                        #the predefined function say() will convert text in "" to speech
	engine.runAndWait()                                      #it will run the code - runAndWait
#speak("Hello! This is your assistant")

def time():                                                  #creating a function for time
	Time = datetime.datetime.now().strftime("%H:%M:%S")      #this will extracts that the current time from now() function
	speak("The current time is")
	speak(Time)                                              
#time()

def date():
	year = int(datetime.datetime.now().year)                 #extracts the year,month,date from now() function and getting it in integer format
	month = int(datetime.datetime.now().month)
	date = int(datetime.datetime.now().day)
	speak("The current day is")
	speak(date)
	speak(month)
	speak(year)
#date()

def wishme():
	speak("Welcome back mam!")
	# date()
	# time()
	hour = datetime.datetime.now().hour                      #to greet according to time
	if hour>=6 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<16:
		speak("Good Afternoon!")
	elif hour>=16 and hour<20:
		speak("Good Evening!")
	else:
		speak("Good Night!")

	speak("Your assistant is here. How can I help you mam?")
#wishme()

def takeCommand():                                           
	r = sr.Recognizer()                                      #initializing recognizer to r
	with sr.Microphone() as source:                          #with statement to get input from user thru mic making mic as source
		print("Listening....")     
		r.pause_threshold = 1                                #it will wait for 1 sec before it starts to listern
		audio = r.listen(source)                            #mic can listern to audio as source is taken as microphone
 
	try:                                                     
		print("Recognizing....")                             #if we get voice properly then it should come to try block and print recognizing   
		query = r.recognize_google(audio, language ='en-US')           #pass audio as we r getting voice from mic thru audio var and setting it to US english
		print(query)                                         
	except Exception as e:                                   #exception as e
		print(e)                                             #printing exception 
		speak("Say that again please.....")                  #if it is unable to recognize the comment then it will say this statement

		return "None"	                                     #if it gets exception we are returning none

	return query	                                         #if it works in try block then it returns query
#takeCommand()

def sendmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com'),587
	server.ehlo()
	server.starttls()
	server.login("vlrdharshini2003@gmail.com","inishidhar16")
	server.sendmail("vlrdharshini2003@gmail.com",to,content)
	server.close()

def screenshot():
	img = pyautogui.screenshot()
	im.save("path we want to save")

def cpu():
	usage = str(psutil.cpu_percent)                           #this will guide for cou percent and str will convert to string format
	speak("CPU is at " + usage)

	battery = psutil.sensors_battery
	speak("battery is at")
	speak(battery.percent )

def jokes():
	speak(pyjokes.get_joke())


if __name__ == "__main__":                                   #main function to create while loop
	wishme()                                                 #once we came it as to wish to adding wishme() here and it has to execute once so added outside of while loop

	while True:                                              #in while loop we r calling already called functions like date time and set to true so that it runs continuously
		query = takeCommand().lower()                        #create query var and call takecommand and lower as that all txt converted to lower and will guide thru function
		print(query)

		if "time" in query:
			time() 
		elif "date" in query:
			date()
		elif "offline" in query:
			quit()
		elif "wikipedia" in query:
			speak("Searching....")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences = 2)            #to get second sentence
			speak(result)
		elif "send email" in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				#to = "receiver add"
				sendmail(to,content)
				speak("Email sent successfully")
			except Exception as e:
				speak(e)
				speak("Unable to send the mail")
		elif "search in chrome" in query:
			speak("What should I search?")
			chromepath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.exe %s"
			search = takeCommand().lower()
			wb.get(chromepath).open_new_tab(search + ".com")
		elif "log out" in query:
			os.system("shutdown - l")
		elif "shutdown" in query:
			os.system("shutdown /s /t l")
		elif "restart" in query:
			os.system("shutdown /r /t l")

		elif "play songs" in query:
			songs_dir = "songs dir path in mysystem"                      #songs path in our system, path for songs directory
			songs = os.listdir(songs_dir)                                 #this returns list of songs in my computer using os.listdir
			os.startfile(os.path.join(songs_dir, songs[0]))               #plays first song using os.startfile

		elif "remember that" in query:
			speak("What should I remember?")                              
			data = takeCommand()                                          #takes what we are saying
			speak("You said me to remember that" + data)          
			remember = open("data.txt","w")                               #opens data.txt file and writes what v r saying
			remember.write(data)                             
			remember.close	

		elif "do you know anything" in query:
			remember = open("data.txt", "r")
			speak("You said me to remember that" + remember.read())                                              #closes the file

		elif "screenshot" in query:
			screenshot()
			speak("Done!")

		elif "CPU" in query:
			cpu()

		elif "jokes" in query:
			jokes()



































