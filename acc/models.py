from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='usr/%y/%m')
    comment = models.TextField()

    def getpic(self):
        if self.pic:
            return self.pic.url
        
        return '/media/noimage.png'