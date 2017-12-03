import wikipedia  #Adds wikipedia
import wolframalpha  #Adds wolfram alpha
import speech_recognition as sr


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Question: ")
        uinput = r.listen(source) #Adds user input
        print(uinput)  
    
    if uinput == "exit program":
        exit()
        
    elif uinput:
        #WIKIPEDIA
        wikipedia.set_lang("en")  #Language!
#        uinput = uinput.split(" ")
#        uinput = " ".join(uinput[2:])
        print(wikipedia.summary(uinput))

    elif uinput.startswith("What's"): 
    #WOLFRAM ALPHA
        app_id = "G58JY9-WQ963T9EQV"  #to get the info
        client = wolframalpha.Client(app_id)  #connecting to info
        result = client.query(uinput)  #collecting result
        answer = next(result.results).text  #processing answer
        print(answer)  #answering with answer
    
    
        
