from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# 입력된 값의 디테일 페이지로 가
def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

# 새로운 정보를 생성해
def create(request):
    # print(request.GET) # <QueryDict: {'title': ['안녕'], 'contnet': ['클레오파트라']}>
    title = request.POST.get('title')
    content = request.POST.get('contnet')
    
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    article = Article(title=title, content=content)
    article.save()

    # Article.objects.create(title=title, content=content)

    return redirect('articles:detail', article.pk)

# 삭제해
def delete(request, pk):
    # 삭제 하려면 조회를 먼저 해야 함
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html')

def update(request, pk):
    article = Article.objects.get(pk = pk)

    #request.POST
    title = request.POST.get('title')
    content = request.POST.get('contnet')

    article.title = title
    article.content = content
    article.save()    # save 필수

    return redirect('articles:detail', article.pk)
