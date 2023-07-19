from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from tagging.fields import TagField
from django.urls import reverse
# Create your models here.
#عنوان خبر
class Category(models.Model):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=2,choices=(('1','Active'),('2','Inactive')),default=1)
    create=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='category_img/',blank=True)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default="")
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    descriptions=RichTextUploadingField()
    banner=models.ImageField(upload_to="news_banner")
    status=models.CharField(max_length=2,choices=(('1','Published'),('2','Unpublished')),default=2)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    views=models.PositiveIntegerField(default=0)
    tags=TagField(blank=True)
    def get_absolute_url(self):
        return reverse("news:detail", args=[self.id,self.category.name])
    
    
    
    def __str__(self):
        return self.title