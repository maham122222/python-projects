import requests
import json
import os
import win32com.client as wincom
# this means ma network ky through req mangwa sakti hu

city=input("Enter the name of the city \n")

url=f"https://api.weatherapi.com/v1/current.json?key=01a88f3570c64c1badd181949230607&q={city}" 

r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)

w=wdic["current"]["temp_c"]
# os.system(f"say'the current wheather in {city} is {w} degress")
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Python text-to-speech test. using win32com.client"
speak.Speak(text)
