from django.db import models

# Create your models here.

class Contact(models.Model):
    
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = 'Clients Message'
        verbose_name_plural = 'Clients Messages'