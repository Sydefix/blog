from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Comment
from .forms import CommentForm
from blog.models import Post

User = get_user_model()

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form, 'post': post})

@login_required
def remove_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user == comment.author or request.user.is_staff:
        comment.delete()
    
    return redirect('post_detail', post_id=comment.post.id)
