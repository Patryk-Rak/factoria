from django.db import models

# Create your models here.
class Business(models.Model):
    NIP = models.CharField(max_length=13)
    name = models.CharField(max_length=255)
    owner = models.IntegerField()
    
    def __str__(self):
        return self.name
