from django.shortcuts import redirect, render
from .models import Infos
from .forms import InfosForm

# Create your views here.
def index(request):
    infos = Infos.objects.order_by('opening_date')
    context = {
        'infos': infos
    }
    return render(request, 'infos/index.html', context)

def create(request):
    if request.method == 'POST':
        info_form = InfosForm(request.POST)
        if info_form.is_valid():
            info_form.save()
            return redirect('infos:index')
    else:
        info_form = InfosForm()
    context = {
        'info_form': info_form
    }
    return render(request, 'infos/create.html', context)

def detail(request, pk):
    info = Infos.objects.get(pk=pk)
    context = {
        'info':info
    }
    return render(request, 'infos/detail.html', context)

def delete(request, pk):
    info = Infos.objects.get(pk=pk)
    info.delete()
    return redirect('infos:index')

def update(request, pk):
    info = Infos.objects.get(pk=pk)
    if request.method == 'POST':
        info_form = InfosForm(request.POST, instance=info)
        if info_form.is_valid():
            info_form.save()
            return redirect('infos:detail', info_form.pk)
    else:
        info_form = InfosForm(instance=info)
    context = {
        'info_form': info_form,
        'info':info
    }
    return render(request, 'infos/update.html', context)