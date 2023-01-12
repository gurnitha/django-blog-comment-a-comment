from django.shortcuts import render

from app.blog.models import Post, Comments
from app.blog.forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/index.html', context)


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post)
    form = CommentForm()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            postid = request.POST.get('post_id')
            post = Post.objects.get(id = postid)
            comment.post = post
            comment.save()

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count = post.view_count + 1
    post.save()
    
    context = {'post':post, 'form':form, 'comments':comments}
    return render(request, 'blog/post.html', context)