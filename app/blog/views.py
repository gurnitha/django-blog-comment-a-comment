from django.shortcuts import render

from app.blog.models import Post

# Create your views here.
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'blog/post.html', context)