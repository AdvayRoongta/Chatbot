import json 
import sys

profanity=["shit","sigma"] #bruh

print("\033[0;31m","FYI, this chatbot may require you to help improve it. Please use responsibly. Advay Roongta is not liable for any misuse. ","\033[0m")
while True:  
    f= open("chatbottext.json", "r")
    
    thedict=json.load(f)=
    f.close()
    print("     ") #
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

                    


















