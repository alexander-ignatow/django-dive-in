from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def feed(request):
    feed = Post.objects.order_by('published_date')
    return render(request, 'blog/feed.html', {'feed': feed})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})
