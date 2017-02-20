from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def feed(request):
    feed = Post.objects.order_by('-published_date')
    return render(request, 'blog/feed.html', {'feed': feed})


def post(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.filter(pk=pk)
    if post:
        return render(request, 'blog/post.html', {'post': post})
    else:
        return render(request, 'blog/no_post.html', {})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
