from django.db import models
from datetime import datetime

def upload_image(instance, filename):
    date_now = str(datetime.now())
    name, extension = str(filename).strip().split('.')
    return f'imgs/{instance.pk}_{date_now}.{extension}'

# Create your models here.


class MyData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=40)
    # image = models.ImageField(upload_to='imgs/')
    image = models.ImageField(default='imgs/default.png',upload_to=upload_image, blank=True, null=True)

    class Meta:
        verbose_name  = 'My Data'
        verbose_name_plural = 'Our Data'
    
    def __str__(self):
        return self.name
