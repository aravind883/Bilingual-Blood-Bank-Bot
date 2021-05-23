from django.shortcuts import render
from django.http import HttpResponse

from AppTwo import forms

from AppTwo.bot import MarioBot

chat_list = []

# Create your views here.
def index(request):

    formobj = forms.chatForm 
    
    dictionary = {'form_key' : formobj }
    

    if request.method == "POST":
        formobj = forms.chatForm(request.POST)

        if formobj.is_valid():
            msg = formobj.cleaned_data['Message']
            chat_list.append(msg)
            response_msg = MarioBot.Mario(msg)
            if str(type(response_msg)) == str(type(list("v"))):
                dictionary['BD_data'] = response_msg
            else:
                chat_list.append(response_msg)
            #chat_list.append(MarioBot.test("TEST"))

        else:   
            print("Invalid")

    
    dictionary['chat'] = chat_list

    return render(request, "AppTwo/index.html", context = dictionary )

def help(request):
    my_dict = {'help_temp':"This is from views.py"}
    return render(request, "AppTwo/help.html", context = my_dict)