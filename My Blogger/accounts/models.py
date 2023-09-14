from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

def image_upload(instance, filname):
   ts = time.time()
   imagename, extension =  filname.split(".")
   return f"profile/{instance.pk}_{int(ts)}.{extension}"

# Create your models here.
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)
   phone_number = models.CharField(max_length=15,null=True, blank=True)
   image = models.ImageField(upload_to = image_upload,null=True,blank=True,default='default.png')
   def __str__(self):
      return str(self.user)



## create new user ---> create new empty profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
      Profile.objects.create(user=instance)


class Country(models.Model):
   name = models.CharField(max_length=30)
   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = 'Countries'