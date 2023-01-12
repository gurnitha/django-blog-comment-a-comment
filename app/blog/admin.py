from django.contrib import admin

from app.blog.models import Comments, Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)