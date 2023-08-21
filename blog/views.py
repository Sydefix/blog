from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm
from comments.models import Comment

User = get_user_model()

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def moderate_posts(request):
    if not request.user.is_staff:
        return redirect('post_list')
    posts = Post.objects.all()
    return render(request, 'blog/moderate_posts.html', {'posts': posts})

@login_required
def ban_user(request, user_id):
    if not request.user.is_staff:
        return redirect('post_list')
    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return redirect('moderate_posts')


# Comments

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
