from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150,verbose_name='Blog Title')
    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add =True)
    # author
    # Comment
    # Category