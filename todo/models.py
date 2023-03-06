from django.db import models
from acc.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name