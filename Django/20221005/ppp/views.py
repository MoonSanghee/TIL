from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-created_at')

    context = {
        'reviews':reviews
    }
    
    return render(request, 'ppp/index.html', context=context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("ppp:index")
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form
    }
    return render(request, 'ppp/create.html', context=context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review':review
    }
    return render(request, 'ppp/detail.html', context)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('ppp:index')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("ppp:detail")
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form' : review_form,
        'review':review
    }
    return render(request, 'ppp/update.html', context)

    #     if request.method == 'POST':
    #     review_form = ReviewForm(request.POST)
    #     if review_form.is_valid():
    #         review_form.save()
    #         return redirect("ppp:index")
    # else:
    #     review_form = ReviewForm()
    # context = {
    #     'review_form' : review_form
    # }
    # return render(request, 'ppp/create.html', context=context)