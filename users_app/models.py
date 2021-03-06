from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.TextField(max_length=120)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"First name: {self.first_name} Last Name : {self.last_name} Email: {self.email} Age:{self.age}"
