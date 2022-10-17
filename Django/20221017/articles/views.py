from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article = ArticleForm(request.POST, request.FILES)
        if article.is_valid():
            article.save()
            return redirect('articles:index')
    else:
        article = ArticleForm()
    context = {
        'article' : article
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article = ArticleForm(request.POST, request.FILES, instance=article)
        if article.is_valid():
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else:
        article = ArticleForm(instance=article)
    context = {
        'article' : article
    }
    return render(request, 'articles/form.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
