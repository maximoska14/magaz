from django.shortcuts import render
from django.http import HttpResponse
from .models import zap

def index(request):
    items = zap.objects.all()
    context = {
        "items":items
    }
    return render(request, "myapp/index.html", context)

def indexItem(request, my_id):
    item = zap.objects.get(id=my_id)
    context = {
        "item":item
    }
    return render(request, "myapp/details.html", context=context)

