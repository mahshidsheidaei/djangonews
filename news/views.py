from django.shortcuts import render,get_object_or_404
from django.views import generic
# from .models import*
from news.models import Category,Post,City
from tagging.models import Tag
# Create your views here.

# def home(request):
#     return render(request,'news/home.html')
    
# class homepageviews(generic.TemplateView):
#     template_name='news/detail.html'

def news_list(request):
    news=Post.objects.all()
    category=Category.objects.all()
    lastest_posts=Post.objects.all().order_by('-created')[:2]
    older_posts=Post.objects.all().order_by('-created')[2:6]
    olderr_posts=Post.objects.all().order_by('-created')[:4]
    populer_posts=Post.objects.order_by('-views')[:2]
    older_populer_posts=Post.objects.order_by('-views')[2:4]
    populerr_posts=Post.objects.order_by('-views')[:5]
    tags=Tag.objects.all()    
    post_tag=Post.objects.filter(tags__in=["طلا",'تصادف','ماشین',"قیمت",'فروش'])
  
    return render(request,'news/home.html',{'news':news,
                                            'category':category,
                                            "lastest_post":lastest_posts,
                                            'older_posts':older_posts,
                                            'olderr_posts':olderr_posts,
                                            'populer_posts':populer_posts,
                                            'older_populer_posts':older_populer_posts,
                                            'populerr_posts':populerr_posts,
                                            'tags':tags,
                                            'post_tag':post_tag,
                                            })

def category_post(request,pk):
    categories=Category.objects.get(id=pk)
    posts=Post.objects.filter(status=1,category=categories)
    tags=Tag.objects.all()
    category=Category.objects.all()
    populerr_posts=Post.objects.order_by('-views')[:5]
    return render(request,'news/category_post.html',{'categories':categories,
                                                     'posts':posts,
                                                      'populerr_posts':populerr_posts,
                                                    'tags':tags,
                                                    'category':category,
                                                     })



def detail(request,pk,category):
    # post=Post.objects.get(id=pk,category__name=category)
    post=get_object_or_404(Post,id=pk,category__name=category)
    post.views+=1
    post.save()
    populerr_posts=Post.objects.order_by('-views')[:5]
    tags=Tag.objects.all()
    category=Category.objects.all()
    return render(request,'news/detail.html',{'post':post,
                                              'populerr_posts':populerr_posts,
                                            'tags':tags,
                                            'category':category,
                                              })



# def home(request):
#     latest_posts =Post.objects.order_by('-created')[:2]
#     older_posts =Post.objects.order_by('-created')[2:6]
#     return render(request,'news/lastpost.html',{'latest_posts': latest_posts,"older_posts":older_posts})




    
def news(request):
    posts=Post.objects.all()
    populerr_posts=Post.objects.order_by('-views')[:5]
    tags=Tag.objects.all()
    category=Category.objects.all()
    return render(request,'news/news.html',{'posts':posts,
                                            'populerr_posts':populerr_posts,
                                            'tags':tags,
                                            'category':category,
                                            })
    
    
def post_tag(request):
   post_tag=Post.objects.filter(tags__in=["طلا",'تصادف','ماشین',"قیمت",'فروش'])
   populerr_posts=Post.objects.order_by('-views')[:5]
   tags=Tag.objects.all()
   category=Category.objects.all()
   return render(request,'news/post_tags.html',{'post_tag':post_tag,
                                                 'populerr_posts':populerr_posts,
                                                 'tags':tags,
                                                 'category':category,})