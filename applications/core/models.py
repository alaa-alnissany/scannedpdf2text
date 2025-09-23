import uuid
from typing import Optional
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length = 50)
    # password = models.CharField(max_length = 100)
    age = models.IntegerField()
    # email = Optional[models.EmailField(max_length = 100)]
    # phone = Optional[models.CharField(max_length = 15)]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name



