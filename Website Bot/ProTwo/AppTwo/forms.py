from django import forms

class chatForm(forms.Form):
    Message = forms.CharField( widget = forms.TextInput(attrs={"class":"inputfields", "placeholder":"Enter your Message here", "value":""}), label="")