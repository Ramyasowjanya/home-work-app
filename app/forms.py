from django.contrib.auth.models import User
from django.forms import forms, Form
from django import forms
class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=30,label="User Name",required=True,error_messages={'invalid':'Username should be unique'})
    email=forms.EmailField(label="Email Id",required=True)
    password1=forms.CharField(max_length=30,widget=forms.PasswordInput(),label="Password",required=True)
    password2=forms.CharField(max_length=30,widget=forms.PasswordInput(),label="Password(again)",required=True)
    hotel=forms.CharField(max_length=40,label="Hotel Name",required=True,error_messages={'invalid':'Only one account for an restaurant'})
    location=forms.CharField(max_length=60)

def clean_username(self):
    u=self.cleaned_data['username']
    try:
        u=User.objects.get(username__exact=u)
    except User.DoesNotExist:
        return self.cleaned_data['username']
    raise forms.ValidationError("Username Already Exists . Please Try another name",code='invalid')
def clean(self):
    p1=self.cleaned_data['password1']
    p2=self.cleaned_data['password2']
    if p1 is not None and p2 is not None:
        if p1 != p2:
          raise forms.ValidationError("Two passwords did not match")
        else:
            return self.cleaned_data
    else:
        raise forms.ValidationError("Both fields should match")
