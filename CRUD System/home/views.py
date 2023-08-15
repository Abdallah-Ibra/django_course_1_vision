from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import MyData
from .form import CreateDataForm,UpdateDataForm

# Create your views here.
def list_data(request):
    data = MyData.objects.all()
    
    context = {
        'data':data,
    }
    return render(request,'index.html',context)


def add_data(request):
    if request.method == 'POST':
        form = CreateDataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateDataForm()
        context = {
            'creation_form':form
            }
        return render(request,'add_data.html',context)

def edit_data(request,pk):
    # data_detail = MyData.objects.get(pk=pk)
    data_detail = get_object_or_404(MyData,pk=pk)
    if request.method == 'POST':
        form = UpdateDataForm(request.POST,request.FILES,instance = data_detail)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateDataForm(instance=data_detail)
        context = {
            'update_form': form,
        }
        return render(request,'edit_data.html',context)


def destroy_data(request,pk):
    data_detail = get_object_or_404(MyData,pk=pk)
    data_detail.delete()
    return redirect('/')