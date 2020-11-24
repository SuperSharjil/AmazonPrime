from django.shortcuts import render, redirect


def index(request):
    if request.session.get('id'):
        return render(request, 'video/feed.html', )
    return render(request, 'homepage.html', )





