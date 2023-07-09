import warnings
import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import os
import webbrowser
import subprocess
import smtplib
import json
import requests
import wolframalpha
import pandas as pd
import numpy as np
import openpyxl

import json
import pymongo

warnings.filterwarnings("ignore")
def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        talk("Good Morning!")
        talk("Welcome to ZAX,your G R I E T virtual assistant . Please tell me how may I help you")
    elif hour>=12 and hour<18:
        talk("Good Afternoon!") 
      
        talk("Welcome to ZAX,your G R I E T virtual assistant . Please tell me how may I help you")

    else:
        talk("Good Evening!") 
        talk("Welcome to ZAX,your G R I E T virtual assistant . Please tell me how may I help you")

machine=pyttsx3.init()
voices = machine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
machine.setProperty('voice', voices[1].id) 
machine.setProperty('rate',170)  #changing index, changes voices. 1 for female

#def send_mail(to,content):
    #server=smtplib.SMTP("smtp.gmail.com",587)
listener=aa.Recognizer()
def talk(text):
    machine.say(text)
    machine.runAndWait()
def note_voice():
    with aa.Microphone() as source:
        listener.pause_threshold =1
        listener.adjust_for_ambient_noise(source)
        print("Listening....")
        speech=listener.listen(source,phrase_time_limit = 5)

     

     
                


    try:
        print("Recognizing...")
        instruction=listener.recognize_google(speech,language='en-in')
            
    except:
        return "None"
    return instruction
def input_instruction():
    
    with aa.Microphone() as source:
                listener.pause_threshold =1
                listener.adjust_for_ambient_noise(source)
                print("Listening....")
                speech=listener.listen(source,phrase_time_limit = 5)


    try:
        print("Recognizing...")
        instruction=listener.recognize_google(speech,language='en-in')
            
    except:
        return "None"
    return instruction
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["griet"]


if __name__=="__main__":

    wish()
    while(True):
        instruction=input_instruction().lower()
        print(instruction)
        
        f=0
        instruction=instruction.replace("details of","")
        instruction=instruction.replace("dr","")
            
        instruction=instruction.replace("babu","")
        instruction=instruction.replace("rao","")
        instruction=instruction.replace("raju","")
            
        instruction=instruction.replace("lakshmi","")
        instruction=instruction.replace("chandra","")
        
        if "contact " in instruction:
           
            
             collection = db["newcontactdetails"]
             if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                      
                        for doc in documents:
                            contact = doc['contact']
                            print(contact)
                            talk(contact)
                        
                        f=f+1
                    
                       
                   
                        f=f+1
            #  elif "Mallikarjuna" in instruction:
            #     print("Professor")
            #     talk("Professor")
             elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "bhargavi" in instruction:
                    x=x+'Dr.Krishna Bhargavi Y'
               else:
                   x=x+'N Krishna Chythanya'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                 del doc['_id']
               l_c=list(documents)
        
               if(len(l_c)!=0):
                
                   # print(l_c)
                    for doc in documents:
                        contact = doc['contact']
                        print(contact)
                        talk(contact)
                    f=f+1
                    
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df) 
            
            
                
                    


             elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  #  print(l_c)
                    for doc in documents:
                            contact = doc['contact']
                            print(contact)
                            talk(contact)
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df)
                #talk(df_1) 
                        
           
            

             else:

                results = collection.find({"$text": {"$search":instruction}})
            #results = collection.find({"name":instruction})
                
                documents = [doc.copy() for doc in results]
                
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                    #print(l_c)
                    for x in documents:
                            contact = x['contact']
                            print(contact)
                            talk(contact)
                    
                    f=f+1
                    
                #talk(l_c)
                    df=pd.DataFrame(l_c)
                
                    f=f+1
    

        elif "experience " in instruction:
           
            
             collection = db["experience"]
             if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            contact = doc['experience']
                            x=doc['link_source']
                            print(contact)
                            print(x)
                            talk(contact)
                        # talk(l_c)
                        f=f+1
                    #talk(l_c)
                        df=pd.DataFrame(l_c)
                   
                        f=f+1
            #  elif "Mallikarjuna" in instruction:
            #     print("Professor")
            #     talk("Professor")
             elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "bhargavi" in instruction:
                    x=x+'Dr.Krishna Bhargavi Y'
               else:
                   x=x+'N Krishna Chythanya'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                 del doc['_id']
               l_c=list(documents)
        
               if(len(l_c)!=0):
                
                   # print(l_c)
                    for doc in documents:
                        
                        contact = doc['experience']
                        x=doc['link_source']
                        
                        print(contact)
                        print(x)
                        talk(contact)

                       
                        
                        
                    f=f+1
                   
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df) 
            
            
                
                    


             elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  #  print(l_c)
                    for doc in documents:
                           contact = doc['experience']
                           x=doc['link_source']
                           print(contact)
                           print(x)
                           talk(contact)

                           
                           
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df)
                #talk(df_1) 
                        
           
            

             else:

                results = collection.find({"$text": {"$search":instruction}})
            #results = collection.find({"name":instruction})
                
                documents = [doc.copy() for doc in results]
                
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                    #print(l_c)
                    for x in documents:
                            contact = x['experience']
                            y = x['link_source']
                            print(contact)
                            print(y)
                            talk(contact)
                           
                    
                    f=f+1
                    
                #talk(l_c)
                    df=pd.DataFrame(l_c)
                
                    f=f+1




        elif "about" in instruction:
           
            collection = db["newabout"]
            if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            about = doc['about']
                            print(about)
                            talk(about)
                        f=f+1
                    #talk(l_c)
                        df=pd.DataFrame(l_c)
                    
                        f=f+1
            # elif "Mallikarjuna" in instruction:
            #     print("Professor")
            #     talk("Professor")
            elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "bhargavi" in instruction:
                    x=x+'Dr.Krishna Bhargavi Y'
               else:
                   x=x+'N Krishna Chythanya'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                 del doc['_id']
               l_c=list(documents)
        
               if(len(l_c)!=0):
                
                   # print(l_c)
                    for doc in documents:
                            about = doc['about']
                            print(about)
                            talk(about)
                    f=f+1
                
                    df=pd.DataFrame(l_c)
                
                    print(df)
                    f=f+1
                   # talk(df) 
            
            
                
                    


            elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  #  print(l_c)
                    for doc in documents:
                            about = doc['about']
                            print(about)
                            talk(about)
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                 
                        
           
            

            else:

                results = collection.find({"$text": {"$search":instruction}})
            #results = collection.find({"name":instruction})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                    #print(l_c)
                    for doc in documents:
                            about = doc['about']
                            print(about)
                            talk(about)
                    f=f+1
                
                    df=pd.DataFrame(l_c)
                
                    f=f+1
        






        
        elif "designation"  in instruction:
           
            collection = db["newdesgn"]
            if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            designation = doc['designation']
                            print(designation)
                            talk(designation)
                        f=f+1
                    
                        df=pd.DataFrame(l_c)
                    
                        f=f+1
            elif "Mallikarjuna" in instruction:
                print("Professor")
                talk("Professor")
            elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "bhargavi" in instruction:
                    x=x+'Dr.Krishna Bhargavi Y'
               else:
                   x=x+'N Krishna Chythanya'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                 del doc['_id']
               l_c=list(documents)
        
               if(len(l_c)!=0):
                
                   # print(l_c)
                    for doc in documents:
                            designation = doc['designation']
                            print(designation)
                            talk(designation)
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
                
                    f=f+1
                   # talk(df) 
            
            
                
                    


            elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  #  print(l_c)
                    for doc in documents:
                            designation = doc['designation']
                            print(designation)
                            talk(designation)
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
                
                    f=f+1
                 
                        
           
            

            else:

                results = collection.find({"$text": {"$search":instruction}})
            #results = collection.find({"name":instruction})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                    #print(l_c)
                    for doc in documents:
                            designation = doc['designation']
                            print(designation)
                            talk(designation)
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
              
                    f=f+1
                #talk(df_1)
                   
        
        



        elif "research papers " in instruction:
           
            
             collection = db["newpublications"]
             if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            x= doc['publications']
                            y=doc['link_source']
                            print(x)
                            print(y)
                            talk(x)

                            print(y)
                        # talk(l_c)
                        f=f+1
                    #talk(l_c)
                        df=pd.DataFrame(l_c)
                   
                        f=f+1
            
             elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "bhargavi" in instruction:
                    x=x+'Dr.Krishna Bhargavi Y'
               else:
                   x=x+'N Krishna Chythanya'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                 del doc['_id']
               l_c=list(documents)
        
               if(len(l_c)!=0):
                
                   # print(l_c)
                    for doc in documents:
                            x= doc['publications']
                            y=doc['link_source']
                            print(x)
                            print(y)
                            talk(x)

                            
                    f=f+1
                   
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df) 
            
            
                
                    


             elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  #  print(l_c)
                    for doc in documents:
                             x= doc['publications']
                             y=doc['link_source']
                             print(x)
                             print(y)
                             talk(x)

                             
                    f=f+1
                #talk(l_c)
                    df=pd.DataFrame(l_c)
               
                    f=f+1
                   # talk(df)
                #talk(df_1) 
                        
           
            

             else:

                results = collection.find({"$text": {"$search":instruction}})
            #results = collection.find({"name":instruction})
                
                documents = [doc.copy() for doc in results]
                
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                    #print(l_c)
                    for doc in documents:
                            x=doc['publications']
                            y=doc['link_source']
                            print(x)
                            print(y)
                            talk(x)

                            
                    
                    f=f+1
                    
                #talk(l_c)
                    df=pd.DataFrame(l_c)
                
                    f=f+1







        elif "courses" or "subject" in instruction:
            
            
            collection = db["subject"]
            

            if "sri " in instruction:
                results = collection.find({"name":'Dr.V Sri lakshmi'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            Courses_Taught = doc['Courses Taught']
                            print(Courses_Taught)
                            talk(Courses_Taught)
                        f=f+1
                   
                        df=pd.DataFrame(l_c)
                   
                        f=f+1
           

            elif "krishna" in instruction:
               # results = collection.find({"$text": {"$search":instruction}})
               x=''
               if "chaitanya" in instruction:
                    x=x+'N Krishna Chythanya'
                    
               else:
                   x=x+'Dr.Krishna Bhargavi Y'
               results = collection.find({"name":x})
               documents = [doc.copy() for doc in results]
               for doc in documents:
                    del doc['_id']
               l_c=list(documents)
            
               if(len(l_c)!=0):
                    
                       # print(l_c)
                        for doc in documents:
                            Courses_Taught = doc['Courses Taught']
                            print(Courses_Taught)
                            talk(Courses_Taught)
                        f=f+1
                    
                        df=pd.DataFrame(l_c)
                   
                        f=f+1
                       
            elif "bhargavi" in instruction:
                #results = collection.find({"$text": {"$search":instruction}})
                results = collection.find({"name":'Dr.S.Bhargavi Latha'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
        
                if(len(l_c)!=0):
                
                  
                    for doc in documents:
                            Courses_Taught = doc['Courses Taught']
                            print(Courses_Taught)
                            talk(Courses_Taught)
                    f=f+1
                
                    df=pd.DataFrame(l_c)
                
            else:

                results = collection.find({"$text": {"$search":instruction}})
                #results = collection.find({"name":'instruction'})
                documents = [doc.copy() for doc in results]
                for doc in documents:
                    del doc['_id']
                l_c=list(documents)
            
                if(len(l_c)!=0):
                    
                   # print(l_c)
                    for doc in documents:
                            Courses_Taught = doc['Courses Taught']
                            print(Courses_Taught)
                            talk(Courses_Taught)
                    f=f+1
                    
                    df=pd.DataFrame(l_c)
                   
                    



       
                    
             
        if "exit" in instruction or "quit" in instruction:
            talk("thank you,have a nice day")
            exit()

        

        elif "none" in instruction:
                print("...")
            
        elif(f==0):
            talk("data not found")
            talk("please repeat it correctly")
        else:

           
                print("")
            
            
