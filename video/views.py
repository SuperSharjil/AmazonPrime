from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from AmazonPrime.models import Video
#from django.db import models
from django.db.backends.oracle import schema


# Create your views here.
def index(request):
    return render(request, 'base.html', )


def VideoDetail(request, id):
    vid = get_object_or_404(Video, pk=id)
    return HttpResponse("<h1>You want this video : " + str(vid) + "</h1>")