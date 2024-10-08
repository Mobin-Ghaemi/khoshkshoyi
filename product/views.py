from django.shortcuts import render, redirect
from django.contrib import messages
from product import forms
from product import models

from django.shortcuts import render, get_object_or_404

def sabteSefaresh(request):
    object_id = None  

    if request.method == 'POST':
        form = forms.SabteSefaresh(request.POST)
        if form.is_valid():
            new_object = form.save() 
            object_id = new_object.id
            return redirect('product:success',object_id=object_id)
        else:
            messages.error(request, 'خطایی در ثبت سفارش رخ داده است.')
    else: 
        form = forms.SabteSefaresh()

    ctx = {
        'form': form,
        'object_id': object_id,  
    }
    return render(request, 'sabt.html', ctx)
def movafagh(request,object_id):
    return render (request,'success.html',{'object_id':object_id})
def sefaresh(request, id):
    sefaresh_instance = get_object_or_404(models.sefaresh, id=id)
    ctx = {
        'sefaresh': sefaresh_instance,
    }
    return render(request, 'sefaresh.html', ctx)
