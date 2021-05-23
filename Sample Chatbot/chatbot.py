import pandas as pd
from termcolor import colored
import time
import random
from googletrans import Translator

data = pd.read_csv(r'Data1.csv').values.tolist()
blood_groups_list = ["A+","O+","B+","B-","AB+","A1+","O-","A-","A2-","A1B+","A2+","A2B+","AB-","A1-","A2B-","A1B-"]
donors_location_list = ['ARIYALUR', 'CHENGALPATTU', 'CHENNAI', 'COIMBATORE', 'CUDDALORE', 'DHARMAPURI', 'DINDIGUL', 'ERODE', 'KALLAKURICHI', 'KANCHIPURAM', 'KANYAKUMARI', 'KARUR', 'KRISHNAGIRI', 'MADURAI', 'MAYILADUTHURAI', 'NAGAPATTINAM', 'NAMAKKAL', 'NILGIRIS', 'PERAMBALUR', 'PUDUKKOTTAI', 'RAMANATHAPURAM', 'RANIPET', 'SALEM', 'SIVAGANGA', 'TENKASI', 'THANJAVUR', 'THENI', 'THOOTHUKUDI', 'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPATTUR', 'TIRUPPUR', 'TIRUVALLUR', 'TIRUVANNAMALAI', 'TIRUVARUR', 'VELLORE', 'VILUPPURAM', 'VIRUDHUNAGAR']
#donors_location_list = ['BANGALORE', 'BILASPUR', 'CHENNAI', 'COIMBATORE', 'CUDDALORE', 'DINDIGUL', 'ERNAKULAM', 'ERODE', 'GODDA', 'HOOGHLY', 'HYDERABAD', 'INDORE', 'KANCHEEPURAM', 'KANNIYAKUMARI', 'KARAIKAL', 'KARUR', 'KRISHNAGIRI', 'KURNOOL', 'MADURAI', 'MALDA', 'MUMBAISUBURBAN', 'MUZAFFARNAGAR', 'NAGAPATTINAM', 'NAMAKKAL', 'NELLORE', 'PATNA', 'PERANMBALUR', 'PONDICHERRY', 'PUDUKKOTTAI', 'RAJKOT', 'RANCHI', 'SALEM', 'SINGHBHUM', 'THANJAVUR', 'THENI', 'THIRUVALLUR', 'TIRUCHIRAPALLI', 'TIRUNELVELI', 'TIRUPUR', 'TIRUVANNAMALAI', 'VELLORE', 'VILLUPURAM', 'VIRUDHUNAGAR', 'WESTDELHI']


blood_group = ""
recipient_location = ""
resp_msg = ""


language = "ENG"
t = Translator()

response_dict_tamil = {

    #Welcome Commands
    "வணக்கம்"    : "வணக்கம், நான் உங்களுக்கு உதவ இங்கே இருக்கிறேன். உங்கள் கோரிக்கையைச் சொல்லுங்கள்!",

    #Getting Blood group
    "எனக்குரத்தம்தேவை"     : "இரத்த வகையை சொல்லவும்",
    "எனக்குரத்தம்வேண்டும்"  : "இரத்த வகையை சொல்லவும்",

    #Blood Groups    
    "BLOODGROUP"    : "இரத்தம் பெருநரின் மாவட்டம் சொல்லவும்",
    
    
    #Location
    "LOCATION"      : "தயவுசெய்து காத்திருங்கள், கிடைக்கக்கூடிய இரத்த தானம் செய்பவர்களை நான் தேடுகிறேன்",

}

response_dict = {

    #Welcome Commands
    "HI"            : "Hi, How can I help you!",
    "HELLO"         : "Hi, How can I help you!",
    "HOWDY"         : "Hi, How can I help you!",

    #Getting Blood group
    "INEEDBLOOD"     : "Enter the blood group",
    "IWANTBLOOD"     : "Enter the blood group",

    #Blood Groups    
    "BLOODGROUP"    : "Tell me the blood recipient's District",
    
    
    #Location
    "LOCATION" : "Please wait, I am checking the available donors",
}

def response_tamil(command):

    for i in list(response_dict_tamil.keys()):
        if (command in i) or (i in command):
            return response_dict_tamil[i]       
    else:
        return "Command not configured!"

def response(command):

    for i in list(response_dict.keys()):
        if (command in i) or (i in command):
            return response_dict[i]       
    else:
        return "Command not configured!"

def tamil_to_english(str):
    #return t.translate(str, src='tamil', dest='english').text
    return t.translate(str, dest='english').text

def english_to_tamil(str):
    return t.translate(str, dest='tamil').text

def mario(str):
    if language == "TAM":
        str = english_to_tamil(str)
    print(colored(str,'green'))

def print_donors(str):
    print( colored(str, 'yellow') )



def greet_eng():
    print("SPEAK TO YOUR BOT HERE:")
    mario("Hi, I am Mario. How can I help you!")

    
def greet_tam():
    print("உங்கள் போட் உடன் இங்கே பேசுங்கள்:")
    mario("வணக்கம்! என் பெயர் மரியோ. உங்கள் கோரிக்கையைச் சொல்லுங்கள்!")

#col = ['Name','Bloodgroup','Address','Phonenumber']
#length = data.len()

test_lang = input("Do you wish to continue in English? Or switch to Tamil?")

while(True):
    if "TAM" in test_lang.strip().replace(" ","").upper():
        language = "TAM"
        break
    elif "ENG" in test_lang.strip().replace(" ","").upper():
        language = "ENG"
        break
    else:
        print("Please enter proper language")

if language == "TAM":
    greet_tam()
else:
    greet_eng()


while(True):

    if resp_msg == "Enter the blood group" or resp_msg == "இரத்த வகையை சொல்லவும்":
        while(True):
            test_input = input().strip().replace(" ","").upper()

            if "POSITIVE" in test_input:
                test_input = test_input.replace("POSITIVE","+")
            elif "NEGATIVE" in test_input:
                test_input = test_input.replace("NEGATIVE","-")
            elif "+VE" in test_input:
                test_input = test_input.replace("+VE","+")
            elif "-VE" in test_input:
                test_input = test_input.replace("-VE","-")
            elif "பாசிடிவ்" in test_input:
                test_input = test_input.replace("பாசிடிவ்","+")
            elif "நேகடிவ்" in test_input:
                test_input = test_input.replace("நேகடிவ்","-")

            if test_input in blood_groups_list:
                blood_group = test_input
                break
            else:
                mario("Please enter a Proper blood group")     

        command = "BLOODGROUP"

    elif resp_msg == "Tell me the blood recipient's District" or resp_msg == "இரத்தம் பெருநரின் மாவட்டம் சொல்லவும்":
        while(True):
            test_input = input().strip().replace(" ","").upper()

            if language == "TAM":
                test_input = tamil_to_english(test_input).strip().replace(" ","").upper()        

            if test_input in donors_location_list:
                recipient_location = test_input 
                command = "LOCATION"               
                break
            else:
                mario("Sorry, No Donors found in " + test_input.capitalize())
                command = "exit()"
                break

    elif resp_msg == "Please wait, I am checking the available donors" or resp_msg == "தயவுசெய்து காத்திருங்கள், கிடைக்கக்கூடிய இரத்த தானம் செய்பவர்களை நான் தேடுகிறேன்":
        if (blood_group in blood_groups_list) and (recipient_location in donors_location_list):
            time.sleep(random.randint(0,10))
            mario("Following donors are found in your location:")
            for i in data:
                a = i[1].strip().replace(" ","").upper()
                b = i[2].strip().replace(" ","").upper()
                if (blood_group == a) and (recipient_location == b):
                    if language == "TAM":
                        print_donors("\nஇரத்த தானம் செய்பவரின் பெயர்       : " + english_to_tamil(str(i[0])) )
                        print_donors("இரத்த தானம் செய்பவரின் கைபேசி எண் : " + str(i[3]) + "\n")
                    else:
                        print_donors("\nDonor's name          : " + str(i[0]))
                        print_donors("Donor's mobile number : " + str(i[3]) + "\n")
            break

        else:
            print("Data not received properly, Please try again")
            resp_msg = ""

    else:
        command = input()


    if command == "exit()":
        break
    else:
        if language == "TAM":
            resp_msg = response_tamil(command.strip().replace(" ","")) 
        else:
            resp_msg = response(command.strip().replace(" ","").upper())     
        mario(resp_msg)

mario("Thank You for using our service!")
