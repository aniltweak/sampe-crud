# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Tweaktalent
# # Create your views here.
#
#
# def custom_response(request):
#     import json
#     data = {'name': 'john', 'age': 25}
#     return HttpResponse(json.dumps(data), content_type='application/json')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweaktalent

def index(request):
    tweaks = Tweaktalent.objects.all()
    return render(request, 'crud/index.html', {'tweaks': tweaks})

def add(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['course'] and request.POST['price'] and request.POST['timings']:
            new_book = Tweaktalent(
                title=request.POST['title'], course=request.POST['course'], price=request.POST['price'],timings=request.POST['timings'])
            new_book.save()
            return redirect('index')
        else:
            return redirect('add')
    return render(request, 'crud/add.html')


def edit(request, tweak_id):
   tweak = Tweaktalent.objects.get(pk=tweak_id)

   if request.method == "POST":
       if request.POST['title'] and request.POST['course'] and request.POST['price'] and request.POST['timings']:
           tweak.title = request.POST['title']
           tweak.price = request.POST['price']
           tweak.author = request.POST['course']
           tweak.timings = request.POST['timings']
           tweak.save()
           return redirect('index')

   return render(request, 'crud/edit.html', {'tweak': tweak})


def delete(request, tweak_id):
    tweak = Tweaktalent.objects.get(pk=tweak_id)
    tweak.delete()

    return redirect('index')
