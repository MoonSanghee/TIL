from django.shortcuts import redirect, render

from .models import Articles
from .forms import ArticlesForm
# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context=context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticlesForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticlesForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method =='POST':
        article_form = ArticlesForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticlesForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()

    return redirect("articles:index")