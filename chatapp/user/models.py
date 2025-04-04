from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
# Create your models here.


# class CustomUserManager(BaseUserManager):
#      def create_user(self,avatar,username,email,password=None):
#          if not email:
#              raise ValueError('email is not given')
#          nemail = self.normalize_email(email)
#          uo = self.model(avatar=avatar,username=username,email=nemail)
#          uo.set_password(password)
#          uo.save()
#          return uo
    
class CustomUser(PermissionsMixin,AbstractBaseUser):
    avatar = models.ImageField(null=True,blank=True)
    username = models.CharField(max_length=100,unique=True,null=False,blank=False )
    email = models.EmailField(unique=True,null=False,blank=False)
    is_active = models.BooleanField(default=False)
   # is_superuser=models.BooleanField(default=False)
    #objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email
 

 