from rest_framework import serializers
from .models import *
import jwt,datetime
from .utils import encode_token
from django.conf import settings
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.exceptions import ValidationError
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
    def validate(self, attrs):
         pw=attrs.get('password')
         attrs['password']=make_password(pw)
         return attrs
   
class LoginViewSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    def validate(self, attrs):
        user=CustomUser.objects.filter(email=attrs.get('email')).first()
        result=check_password(attrs.get('password'),user.password )
        if result==True:
                token=encode_token(attrs)
                return token
        else:
             raise ValidationError('invalid credentials')
