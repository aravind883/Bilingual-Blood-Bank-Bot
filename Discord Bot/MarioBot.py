from googletrans import Translator
import pandas as pd
from csv import writer
import sys


BD_data = pd.read_csv(r"Data.csv").values.tolist()

blood_groups_list = ["A+","O+","B+","B-","AB+","A1+","O-","A-","A2-","A1B+","A2+","A2B+","AB-","A1-","A2B-","A1B-"]
donors_location_list = ['ARIYALUR', 'CHENGALPATTU', 'CHENNAI', 'COIMBATORE', 'CUDDALORE', 'DHARMAPURI', 'DINDIGUL', 'ERODE', 'KALLAKURICHI', 'KANCHIPURAM', 'KANYAKUMARI', 'KARUR', 'KRISHNAGIRI', 'MADURAI', 'MAYILADUTHURAI', 'NAGAPATTINAM', 'NAMAKKAL', 'NILGIRIS', 'PERAMBALUR', 'PUDUKKOTTAI', 'RAMANATHAPURAM', 'RANIPET', 'SALEM', 'SIVAGANGA', 'TENKASI', 'THANJAVUR', 'THENI', 'THOOTHUKUDI', 'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPATTUR', 'TIRUPPUR', 'TIRUVALLUR', 'TIRUVANNAMALAI', 'TIRUVARUR', 'VELLORE', 'VILUPPURAM', 'VIRUDHUNAGAR']

data_list = []
blood_group = ""
recipient_location = ""
input_type = "LANG"
language = "NONE"

rname = ""
rbloodgroup = ""
rlocation = ""
rmobile = ""


def tamil_to_english(str):
    t = Translator()
    return t.translate(str, dest='english').text
    

def english_to_tamil(str):
    t = Translator()
    return t.translate(str, dest='tamil').text

response_dict_tamil = {

    #Welcome Commands
    "வணக்கம்"    : "வணக்கம், நான் உங்களுக்கு உதவ இங்கே இருக்கிறேன். உங்கள் கோரிக்கையைச் சொல்லுங்கள்!",
    "HI"            : "வணக்கம், நான் உங்களுக்கு உதவ இங்கே இருக்கிறேன். உங்கள் கோரிக்கையைச் சொல்லுங்கள்!",
    "HELLO"         : "வணக்கம், நான் உங்களுக்கு உதவ இங்கே இருக்கிறேன். உங்கள் கோரிக்கையைச் சொல்லுங்கள்!",


    #Asking the user for his details
    "பதிவு"                    :   "நல்ல முடிவு!\nஉங்கள் பெயரைச் சொல்லுங்கள்",
    "இரத்ததானம்செய்ய"    :     "நல்ல முடிவு!\nஉங்கள் பெயரைச் சொல்லுங்கள்",
    "ரத்ததானம்செய்ய"      :    "நல்ல முடிவு!\nஉங்கள் பெயரைச் சொல்லுங்கள்",
    "தானம்செய்ய"           :    "நல்ல முடிவு!\nஉங்கள் பெயரைச் சொல்லுங்கள்",


    #Getting Blood group
    "எனக்குரத்தம்தேவை"       : "இரத்த வகையை சொல்லவும்",
    "எனக்குரத்தம்வேண்டும்"    : "இரத்த வகையை சொல்லவும்",
    "எனக்குஇரத்தம்தேவை"     : "இரத்த வகையை சொல்லவும்",
    "எனக்குஇரத்தம்வேண்டும்"  : "இரத்த வகையை சொல்லவும்",
    "இரத்த"                     : "இரத்த வகையை சொல்லவும்",
    "ரத்த"                       : "இரத்த வகையை சொல்லவும்",
    "தானம்"                    : "இரத்த வகையை சொல்லவும்",

    #Blood Groups    
    "BLOODGROUP"    : "இரத்தம் பெருநரின் மாவட்டம் சொல்லவும்",
    
    
    #Location
    "LOCATION"      : "தயவுசெய்து காத்திருங்கள், கிடைக்கக்கூடிய இரத்த தானம் செய்பவர்களை நான் தேடுகிறேன்",

}

response_dict = {

    #Welcome Commands
    "HI"            : "Hi, How can I help you!",
    "HELLO"         : "Hi, How can I help you!",

    #Asking the user for his details
    "REGISTER"              : "That's great!\nPlease tell me your Name",
    "BECOMEADONOR"          : "That's great!\nPlease tell me your Name",
    "BECOMEABLOODDONOR"     : "That's great!\nPlease tell me your Name",

    #Getting Blood group
    "INEEDBLOOD"     : "Enter the blood group",
    "IWANTBLOOD"     : "Enter the blood group",
    "DONOR"          : "Enter the blood group",
    "DONATE"          : "Enter the blood group",
    "DONATEBLOOD"          : "Enter the blood group",

    #Blood Groups    
    "BLOODGROUP"    : "Tell me the blood recipient's District",
    
    
    #Location
    "LOCATION" : "Please wait, I am checking the available donors",
}

def Mario(message_str):
    
    global language
    global input_type
    if input_type == "RNAME" or input_type == "RPLACE":
        if language == "TAM":
            message_str = tamil_to_english(message_str).capitalize()
        else:
            message_str = message_str.capitalize()

    elif language == "TAM":
        message_str = message_str.strip().replace(" ","")
    else:
        message_str = message_str.strip().replace(" ","").upper()

    if ("THANK" in message_str) or ("EXIT" in message_str) or ("நன்றி" in message_str) or ("போகிறேன்" in message_str) or ("வருகிறேன்" in message_str):
        if language == "TAM":
            return english_to_tamil("Thankyou for using our service!")
        else:
            return "Thankyou for using our service!"


    global blood_group
    global recipient_location
    global rname
    global rbloodgroup
    global rlocation
    global rmobile
    if input_type == "LANG":
        
        if ("TAM" in message_str) or ("த" in message_str) or ("2" == message_str):
            language = "TAM"
            input_type = "N"
            return "வணக்கம்! என் பெயர் மேரியோ. உங்கள் கோரிக்கையைச் சொல்லுங்கள்!"
            
        elif "ENG" in message_str or ("1" == message_str):
            language = "ENG"
            input_type = "N"
            return "Hi, I am Mario. How can I help you!"

        elif "HI" in message_str or "HELLO" in message_str:

            var = "Hi, I am Mario. Your personal Blood Bank Bot!\n"
            var = var + "Please choose your language\n"          
            var = var + "உங்கள் மொழியைத் தேர்வுசெய்க\n"
            var = var + "(English/தமிழ்)"
            return var
            
        else:
            return "Please enter proper language"

    elif input_type == "N":

        if language == "TAM":
            dict = response_dict_tamil
        else:
            dict = response_dict

        for i in list(dict.keys()):
            
            if (i in message_str) or (message_str in i):
                if (i == "INEEDBLOOD") or (i == "IWANTBLOOD") or (i == "DONOR") or (i == "DONATE") or (i == "DONATEBLOOD") or (i == "எனக்குரத்தம்தேவை") or (i == "எனக்குரத்தம்வேண்டும்") or (i == "எனக்குஇரத்தம்தேவை") or (i == "எனக்குஇரத்தம்வேண்டும்") or (i == "இரத்த") or (i == "ரத்த") or (i == "தானம்"):
                    input_type = "BLOOD"

                elif (i == "REGISTER") or (i == "BECOMEADONOR") or (i == "BECOMEABLOODDONOR") or (i == "பதிவு") or (i == "இரத்ததானம்செய்ய") or (i == "ரத்ததானம்செய்ய") or (i == "தானம்செய்ய"):
                    input_type = "RNAME"

                if language == "TAM":
                    return response_dict_tamil[i]
                else:
                    return response_dict[i]
        else:
            input_type = "N"
            if language == "TAM":
                return english_to_tamil("Command not configured")
            else:
                return "Command not configured"

    elif input_type == "RNAME":
        rname = message_str
        input_type = "RBLOOD"

        if language == "TAM":
            return english_to_tamil("What is your Blood Group")
        else:
            return "What is your Blood Group"

    elif input_type == "RBLOOD":
        blood_group = message_str

        if "POSITIVE" in blood_group:
            blood_group = blood_group.replace("POSITIVE","+")
        elif "NEGATIVE" in blood_group:
            blood_group = blood_group.replace("NEGATIVE","-")
        elif "+VE" in blood_group:
            blood_group = blood_group.replace("+VE","+")
        elif "-VE" in blood_group:
            blood_group = blood_group.replace("-VE","-")
        elif "பாசிடிவ்" in blood_group:
            blood_group = blood_group.replace("பாசிடிவ்","+")
        elif "நேகடிவ்" in blood_group:
            blood_group = blood_group.replace("நேகடிவ்","-")

        if blood_group in blood_groups_list:
            rbloodgroup = blood_group
        else:
            if language == "TAM":
                return english_to_tamil("Please enter a proper blood group")
            else:
                return "Please enter a proper blood group"

        input_type = "RPLACE"

        if language == "TAM":
            return english_to_tamil("Tell me your district")
        else:
            return "Tell me your district"

    elif input_type == "RPLACE":
        if message_str.upper().strip().replace(" ","") in donors_location_list:
            rlocation = message_str.upper().strip().replace(" ","")
            input_type = "RMOBILE"
            if language == "TAM":
                return english_to_tamil("Tell me your mobile number")
            else:
                return "Tell me your mobile number"
        else:
            if language == "TAM":
                return english_to_tamil("Please enter a proper district name")
            else:
                return "Please enter a proper district name"
    
    elif input_type == "RMOBILE":
        message_str = message_str.replace("+91","").replace(" ","").strip()
        try:
            message_str = str(int(message_str))
        except:
            if language == "TAM":
                return english_to_tamil("Please enter a proper mobile number")
            else:
                return "Please enter a proper mobile number"
        
        if len(message_str) == 10:
            rmobile = message_str
        else:
            if language == "TAM":
                return english_to_tamil("Please enter a proper mobile number")
            else:
                return "Please enter a proper mobile number"

        error_flag = 0
        details_list = [rname, rbloodgroup, rlocation, rmobile]
        try:
            with open("Data.csv", 'a') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(details_list)
                f_object.close()            

        except:
            print(str(sys.exc_info()[0]))
            error_flag = 1

        if error_flag == 0:
            input_type = "N"
            if language == "TAM":
                return english_to_tamil("You have been added to the donors list successfully!")
            else:
                return "You have been added to the donors list successfully!"
        else:
            input_type = "RNAME"
            if language == "TAM":
                return english_to_tamil("There has been an error! Please tell me your name again.")
            else:
                return "There has been an error! Please tell me your name again."

            

    elif input_type == "BLOOD":
        blood_group = message_str

        if "POSITIVE" in blood_group:
            blood_group = blood_group.replace("POSITIVE","+")
        elif "NEGATIVE" in blood_group:
            blood_group = blood_group.replace("NEGATIVE","-")
        elif "+VE" in blood_group:
            blood_group = blood_group.replace("+VE","+")
        elif "-VE" in blood_group:
            blood_group = blood_group.replace("-VE","-")
        elif "பாசிடிவ்" in blood_group:
            blood_group = blood_group.replace("பாசிடிவ்","+")
        elif "நேகடிவ்" in blood_group:
            blood_group = blood_group.replace("நேகடிவ்","-")

        input_type = "PLACE"

        if language == "TAM":
            return response_dict_tamil["BLOODGROUP"]
        else:
            return response_dict["BLOODGROUP"]

    elif input_type == "PLACE":

        if language == "TAM":
            message_str = tamil_to_english(message_str)
        recipient_location = message_str

        blood_group = blood_group.strip().replace(" ","").upper()
        recipient_location = recipient_location.strip().replace(" ","").upper()
        
        input_type = "N"
        

        if (blood_group in blood_groups_list) and (recipient_location in donors_location_list):            
            global data_list
            for i in BD_data:
                a = i[1].strip().replace(" ","").upper()
                b = i[2].strip().replace(" ","").upper()
                if (blood_group == a) and (recipient_location == b):
                    if language == "TAM":
                        data_list.append("பெயர் : " + english_to_tamil(str(i[0])))
                        data_list.append("கைபேசி எண் : " + str(i[3]))
                    else:
                        data_list.append("Name : " + str(i[0]))
                        data_list.append("Mobile Number : " + str(i[3]))
                    data_list.append("")
            return data_list


        else:
            if language == "TAM":
                return english_to_tamil("Data not received properly, Please try again")
            else:
                return "Data not received properly, Please try again"


        if language == "TAM":
            return response_dict_tamil["LOCATION"]
        else:
            return response_dict["LOCATION"]


def test(string):
    return string