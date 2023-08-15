from django.db import models


def upload_image(instance,filename):
    name,extension = str(filename).strip().split('.')
    return f'imgs/{instance.pk}.{extension}'

# Create your models here.
class MyData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=40)
    # image = models.ImageField(upload_to='imgs/')
    image = models.ImageField(upload_to=upload_image,blank=True,null = True)
    
    def __str__(self):
        return self.name