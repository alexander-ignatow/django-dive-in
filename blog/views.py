from django.shortcuts import render
from django.utils import timezone
from .models import Post

def feed(request):
    feed = Post.objects.order_by('published_date')
    return render(request, 'blog/feed.html', {'feed': feed})