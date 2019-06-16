from django.shortcuts import render
from . import  models
# Create your views here.
from django.http import HttpResponse
# def index(request):
#     return render(request,'index.html',{'hello':'Blog body'})
def index(request):

    # acticle = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) =='0':
        return  render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return  render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content', 'Content')
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        models.Article.objects.create(title=title,content = content)
        articles = models.Article.objects.all()
        return render(request,'blog/index.html',{'articles':articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.cnotent = content
    article.save()
    return render(request, 'blog/article_page.html',{'article':article})