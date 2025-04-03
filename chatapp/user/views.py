from django.shortcuts import render
from rest_framework.views import APIView
from user.serializers import UserRegistrationSerializer,LoginViewSerializer
from .models import *
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password,make_password

class UserRegistrationView(APIView):
    def post(self,request):
        data=request.data
        if CustomUser.objects.filter(Q(email=data.get('email') )| Q(username=data.get('username'))).exists():
            return Response({'message':'email/username is already registered','status':'failed'},status=status.HTTP_400_BAD_REQUEST)
        serializer=UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            pw=serializer.validated_data.get('password')
            serializer.validated_data['password']=make_password(pw)
            serializer.save()
            return Response({'message':'user registered succesfully','status':'success'},status=status.HTTP_200_OK)
        

class LoginView(APIView):
    def post(self,request):
            data = request.data      
            if CustomUser.objects.filter(email=data.get('email')).exists():
                serializer=LoginViewSerializer(data=data)
                if serializer.is_valid():                      
                    return Response({'message':'user logged in succesfully','data':{'token':serializer.validated_data['token']},'status':'succesfull'},status=status.HTTP_200_OK)  
                else:
                   return Response({'message':'invalid credentials','status':'failed'},status=status.HTTP_400_BAD_REQUEST)                                        
            return Response({'message':'user doesnt exist','status':'failed'},status=status.HTTP_400_BAD_REQUEST)
            
                 
                 
                 
           
             