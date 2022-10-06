from django.shortcuts import redirect, render
from infos.forms import InfosForm
from infos.models import Infos

# Create your views here.

def index(request):
    infos = Infos.objects.order_by('-pk')
    context = {
        'infos' : infos
    }
    return render(request, 'infos/index.html', context)

def create(request):
    if request.method == 'POST':
        infos_form = InfosForm(request.POST)
        if infos_form.is_valid():
            infos_form.save()
            return redirect('infos:index')
    else:
        infos_form = InfosForm()
    context = {
        'infos_form':infos_form
    }
    return render(request, 'infos/create.html', context=context)

def detail(request, pk):
    info = Infos.objects.get(pk=pk)
    infos_form = InfosForm(request.POST, instance=info)
    context = {
        'info': info,
        'infos_form' : infos_form
    }
    return render(request, 'infos/detail.html', context)

def delete(request, pk):
    info = Infos.objects.get(pk=pk)
    info.delete()
    return redirect('infos:index')

def update(request, pk):
    info = Infos.objects.get(pk=pk)
    if request.method == 'POST':
        infos_form = InfosForm(request.POST, instance=info)
        if infos_form.is_valid():
            infos_form.save()
            return redirect('infos:detail', info.pk)
    else:
        infos_form = InfosForm(instance=info)
    context = {
        'infos_form':infos_form,
        'info':info
    }
    return render(request, 'infos/update.html', context=context)