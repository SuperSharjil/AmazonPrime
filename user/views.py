from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return render(request, 'base.html', context)
    return HttpResponse("<h1>this is a user </h1>")
