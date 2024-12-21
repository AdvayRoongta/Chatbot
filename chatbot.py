import json #"self-murder" : "Suicide.", 

import turtle
#           
# profanity=["fuck","shit","bitch","ass","slave","retard","nigger","faggot","fag","dick","cunt"]
                #hi
                #          BAD LIST AT BOTTOM 
import sys
profanity=["fuck","shit","bitch","ass","slave","retard","nigger","faggot","fag","dick","cunt"]

#project idea if neded: dna to rna to amino acid
#can use chatgpt generated q&a found in doogle drive somewhere
'''
    if s=="ADVAY":
        file=open("forsubmission.json")
        aproved=file.read()
        file.truncate(0)
        file.close() 
        f=open("chatbottext.json","a")
        f.write(aproved)
asldfjal;skdfj;klj
        HI
        Welcome to my github.io site, i'm advay-
        a highschool freshman from California

        I like coding, complaining, and playing table tennis and the saxophone

        Mainly python, but teaching myself java for school robotics club, and i know HTML+CSS

        I made this site originally to advertise a freelance web design service and for High seas, howeveer, while creating the site:
        i leanered I didnt enjoy frontend developing too much, so I closed down that chapter of my life pretty soon

        I kept the original text I had for that "phase"  because I dont like writing and didnt want my work to go to wast :/
    
        The contant form is disabled on purpose btw
            Fun fact: Did you know that [insert name here] was the [insert position] for [time] years?!?!?!?
        
        '''
#import nltk
#from nltk.corpus import words
#insert bad words
print("\033[0;31m","FYI, this chatbot may require you to help improve it. Please use responsibly. Advay Roongta is not liable for any misuse. ","\033[0m")
while True:  #if anyting goes wrong with dumping and loading check screenshots
    f= open("chatbottext.json", "r")
    
    thedict=json.load(f)
#algorithms: keyword, any word larger than or 6 letters (will have to manually exlude "before")
#negation: if negation word is in front of keyword
#can do a "what is" "what is a" algorithm so if i say "what is qwert" and it doesnt have it in the json it can give some generic response
#scrap: today i worked on my python chatbot with json. i finsihed the UI. then i started working on a "what is" algorithm 
    f.close()
    print("     ") #for the ui, dont delete
    print("Hi. Say something.")
    s=input()
    news=s.lower() 
    finals=news.rstrip(".!?")
    
    if finals in thedict:
            print("\033[0;36m",thedict[finals],"\033[0m")
    else: 
            if "what is a " in finals:
                         item=finals.rsplit("what is a",1)
                         print("\033[0;36m",f"i dont know what a {item[1]} is (or how it works), but maybe you can search it up on google, firefox, bing, or any chromium brower","\033[0m")
                         item.clear()
            if "what is an" in finals:
                  item=finals.rsplit("what is an ",1)
                  print("\033[0;36m",f"i dont know what an {item[1]} is (or how it works), but maybe you can search it up on google, firefox, bing, or any chromium brower","\033[0m")
                  item.clear()
            if "whats a" in finals:
                  item=finals.rsplit("whats a ",1)
                  print("\033[0;36m",f"i dont know what a {item[1]} is (or how it works), but maybe you can search it up on google, firefox, bing, or any chromium brower","\033[0m")
                  item.clear()

            else:
                print( "\033[0;31m","Sorry, I do not know that phrase. Please give me a response, if you have one and it will help me learn. If you dont say: 'idont'","\033[0m")
                new=input()
                if new=="idont" or new=="Idont":
                    print("\033[0;36m","No worries","\033[0m")
                else: #
                    for i in profanity:
                          if i in new:
                            print("\033[1;31mPROFANITY DETECTED\033[0m") 
                            sys.exit(0)
                    with open("chatbottext.json", "r") as file:
                        data = json.load(file)
                        data[finals]=new
                        file.close()
                    with open('chatbottext.json', "w") as file:
                        json.dump(data, file, indent=4)

                        print("\033[0;36m","Data added successfully, thanks for contributing","\033[0m")

                    







'''
                    new_entry = {finals: new}
                    json.dump(new_entry, file)  
                    file.write('\n')
                    file.close()
                
                    '''
'''
import json

with open("chatbottext.json") as f:
    chatbot_responses = json.load(f)

while True:
    s = input("Hi. Say something: ")

    news = s.lower()
    finals = news.rstrip(".!?")

    if finals in chatbot_responses:
        print(chatbot_responses[finals])
    else:
        new = input("Sorry, but I do not know that phrase. Please give me a response, if you have one and it will help me learn. If you don't, say: I dont\n")

        if new.lower() == "i dont":
            print("No worries")
        else:
            # Append the new entry to the JSON file in proper JSON format
            with open("forsubmission.json", "a") as file:
                new_entry = {finals: new}
                json.dump(new_entry, file)
                file.write('\n')
                '''
#PLEASE IGNORE THIS IS FOR THE GREATER GOOD

#can use gitignore













profanity=["fuck","shit","bitch","ass","slave","retard","nigger","faggot","fag","dick","cunt"]



sfsfs


