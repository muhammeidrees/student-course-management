from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    instructor=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

