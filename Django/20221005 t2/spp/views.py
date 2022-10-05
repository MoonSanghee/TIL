from django.shortcuts import redirect, render

from .forms import sppForm
from .models import Reviews
# Create your views here.

def index(request):
    reviews = Reviews.objects.order_by('-pk')
    context = {
        'reviews':reviews
    }
    return render(request, 'spp/index.html', context=context)

def create(request):
    if request.method == 'POST':
        review_form = sppForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('spp:index')
    else:
        review_form = sppForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'spp/new.html', context=context)

def detail(request, pk):
    review = Reviews.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'spp/detail.html', context= context)

def update(request, pk):
    review = Reviews.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = sppForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('spp:detail', review.pk)
    else:
        review_form = sppForm(instance=review)
    context = {
        'review_form': review_form,
        'review': review
    }
    return render(request, 'spp/update.html', context=context)

def delete(request, pk):
    review = Reviews.objects.get(pk=pk)
    review.delete()
    return redirect('spp:index')