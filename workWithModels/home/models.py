from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.name} | {self.email} | {self.phone}'
    

