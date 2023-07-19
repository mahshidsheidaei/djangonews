from django.contrib import admin
from news import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=["title",'user','status','created','category','views']

admin.site.register(models.Category)
admin.site.register(models.City)
admin.site.register(models.Post,PostAdmin)