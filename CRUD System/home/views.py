from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.urls import reverse
from .models import MyData
from .form import CreateDataForm, UpdateDataForm

# Create your views here.


def list_data(request):
    data = MyData.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'index.html', context)


def create_data(request):
    if request.method == 'POST':
        form = CreateDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateDataForm()
    
    context = {
        'creation_form': form,
    }
    return render(request, 'add_data.html', context)


def update_data(request,pk):
    # data = MyData.objects.get(pk=pk)
    data = get_object_or_404(MyData,pk=pk)
    if request.method == 'POST':
        form = UpdateDataForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            # return redirect('/')
            return redirect(reverse('home:list_data'))
    else:
        form = UpdateDataForm(instance=data)
    
    context = {
        'update_form': form,
    }
    return render(request, 'edit_data.html', context)


def destroy_data(request,pk):
    data = get_object_or_404(MyData,pk=pk)
    data.delete()
    return redirect('/')
