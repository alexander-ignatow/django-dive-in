from django.shortcuts import render

def feed(request):
    return render(request, 'blog/feed.html', {})
