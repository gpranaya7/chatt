from rest_framework import serializers
from .models import *
import jwt,datetime
from django.conf import settings
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import ValidationError
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
   
class LoginViewSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    def validate(self, attrs):
        user=CustomUser.objects.filter(email=attrs.get('email')).first()
        result=check_password(attrs.get('password'),user.password )
        if result==True:
                expiration_time=datetime.datetime.now()+datetime.timedelta(hours=24)
                expiration_timestamp=expiration_time.timestamp()
                token=jwt.encode({'email':attrs.get('email'),'exp':expiration_timestamp},settings.SECRET_KEY,algorithm='HS256')
                attrs['token']=token
                print(token)
                return attrs
        else:
             raise ValidationError('invalid credentials')
        
