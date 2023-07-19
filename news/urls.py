from django.urls import path
from .views import *

app_name='news'
urlpatterns = [
  path('',news_list,name='home'),
  path("category/<int:pk>/",category_post,name='category_post'),
  path('detail/<int:pk>/<str:category>/',detail,name='detail'),
  path('news/',news,name='news'),
  path('post/',post_tag,name='post_tag')
  
]
