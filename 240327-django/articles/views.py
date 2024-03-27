from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # 유효성 검사 여기서 하도록 해야 해, modelForm도입
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)

#     form = ArticleForm(request.POST) # 덩어리로 넣어주면 된다.
#     # 유효성 검사를 통과해야 save를 하시오
#     if form.is_valid() == True:
#         article = form.save()
#         return redirect('articles:detail', article.pk)
#     # 만약에 통과하지 못한다면?
#     context = {
#         'form' : form,
#     }
#     # 리턴값으로 에러메세지를 보여줌 (어떤 에러인지도)
#     return render(request, 'articles/new.html', context) 

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid() == True:
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm()

#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # article.title = title
#     # article.content = content
#     # article.save()

#     #instance를 넣어줌으로써 이건 생성이 아닌 수정임을 알려줌
#     form = ArticleForm(request.POST, instance = article) 
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article) 
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance = article) 
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)