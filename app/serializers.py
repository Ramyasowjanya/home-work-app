from rest_framework import serializers
from app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password1')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','name','location','user')


class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menus
        fields=('id','name','cost','hotel')