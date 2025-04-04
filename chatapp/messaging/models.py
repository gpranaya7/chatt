# Create your models here.
from django.db import models
from user.models import CustomUser
class Message(models.Model):
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content}"
    



