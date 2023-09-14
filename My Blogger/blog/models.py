from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
import time



def image_upload(instance, filname):
    ts = time.time()
    imagename, extension =  filname.split(".")
    return f"blogs/{instance.pk}_{int(ts)}.{extension}"


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, related_name='blog_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250,verbose_name='Blog Title')
    image = models.ImageField(upload_to=image_upload)
    description = models.TextField(max_length=3000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='category_blogs')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add =True)
    slug = models.SlugField(blank=True, unique=True)
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog,self).save(*args, **kwargs)  
    
    
    def __str__(self):
        return f'"{self.title}"'
    
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['-created_at',]


class Category(models.Model):
    
    name = models.CharField(max_length=35, null= True,verbose_name='Category Name')
    description = models.TextField(verbose_name='Category Description',null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='blog_comments')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    text = models.TextField(max_length=800,verbose_name='Comment') 
    image = models.ImageField(upload_to='comments/',null=True, blank=True,default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name_plural = 'Comments'


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} likes {self.blog.title}"

    class Meta:
        verbose_name_plural = 'Likes'