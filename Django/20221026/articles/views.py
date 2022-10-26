from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm
from django.http import JsonResponse

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)
 
@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user 
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user: 
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
        else:
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/form.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    context = {
        'content': comment.content,
        'userName': comment.user.username
    }
    return JsonResponse(context)

def likes(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.user in article.like_user.all():
        article.like_user.remove(request.user)
        is_liked = False
    else:
        article.like_user.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_user.count()}
    return JsonResponse(context)

