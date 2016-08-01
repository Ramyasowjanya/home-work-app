from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import  viewsets, status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
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

class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer


@api_view(['GET'])
def rest_list(request):
        if request.method == 'GET':
            snippets = Restaurant.objects.all()
            serializer = RestaurantSerializer(snippets, many=True)
            return Response(serializer.data)

@api_view(['POST'])
def user_list(request):
        if request.method == 'POST':
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data['username']
                    email = form.cleaned_data['email']
                    hotel = form.cleaned_data['hotel']
                    location = form.cleaned_data['location']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']
                    if password1 == password2:
                        # serializer = UserSerializer(username=username,password1=password1,email=email)
                        # if serializer.is_valid():
                        #     serializer.save()
                        # seri = RestaurantSerializer(hotel=hotel,location=location, user=serializer)
                        # if seri.is_valid():
                        #     seri.save()
                        u = User.objects.create_superuser(username, email, password1)
                        u.save()
                        r = Restaurant(name=hotel, location=location, user=u)
                        r.save()
                        return Response(request.get_host(), status=status.HTTP_201_CREATED)
                #return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def menus_detail(request, pk):
    try:
        list = Menus.objects.filter(hotel__id=pk)
    except Menus.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenusSerializer(list,many=True)
        return Response(serializer.data)
