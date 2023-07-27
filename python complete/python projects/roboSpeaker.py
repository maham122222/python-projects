import os
import win32com.client as wincom


if __name__== '__main__':
    print("Welcome to robo speaker. Created by maham jamil")
    while(True):
        x=input("enter what you want me to pronounce : ")
        if x=="q":
            os.system("say 'bye bye friend'")
            break
        # command= f"say{x}"
        # os.system(command)
        speak = wincom.Dispatch("SAPI.SpVoice")
        text = "Python text-to-speech test. using win32com.client"
        speak.Speak(x)