from importlib.resources import contents
from django.shortcuts import render, redirect
from . models import Review

# Create your views here.



def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }

    return render(request,"todos/index.html",context)

def new(request):
    return render(request,"todos/new.html")

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    Review.objects.create(title=title, content=content)
    return redirect('todos:index')

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request,"todos/detail.html", context)

def update(request, pk):
    review = Review.objects.get(pk=pk)

    title = request.GET.get('title')
    content = request.GET.get('content')

    review.title = title
    review.content = content
    review.save()

    return redirect("todos:index")

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()

    return redirect("todos:index")

def search(request):
    search = request.GET.get('title')
    reviews = Review.objects.filter(title__contains = search)
    context={
        'reviews': reviews
    }
    
    return render(request,"todos/search.html",context)