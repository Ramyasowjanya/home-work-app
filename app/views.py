from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.serializers import *

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.forms import RegistrationForm
from app.models import  *

def logout1(request):
    logout(request)
    return HttpResponseRedirect("/restaurants/lists/")

def get_registrationform(request):
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            hotel=form.cleaned_data['hotel']
            location=form.cleaned_data['location']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1==password2:
                u=User.objects.create_superuser(username,email,password1)
                r=Restaurant(name=hotel,location=location,user=u)
                r.save()
                return HttpResponseRedirect("/restaurants/lists/")
    else:
        form=RegistrationForm()

    return render(request,'registration/registration.html',{'form':form},)

