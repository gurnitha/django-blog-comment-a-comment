## Django Blog Comment a Comment 

Building a very complete blog application

Github link: https://github.com/gurnitha/django-blog-comment-a-comment
My Learning link: https://www.udemy.com/course/python-django-masterclass/learn/lecture/


## 01. Project Setup


#### 01.1 Modified .gitignore and readme files


#### 01.2 Create django project

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 01.3 Create django app

        modified:   README.md
        new file:   app/blog/__init__.py
        new file:   app/blog/admin.py
        new file:   app/blog/apps.py
        new file:   app/blog/migrations/__init__.py
        new file:   app/blog/models.py
        new file:   app/blog/tests.py
        new file:   app/blog/views.py


#### 01.4 Register the blog app

        modified:   app/blog/apps.py
        modified:   config/settings.py



## 02. Django models


#### 02.1 Create Post model and image path

        modified:   README.md
        new file:   app/blog/migrations/0001_initial.py
        modified:   app/blog/models.py
        modified:   config/settings.py



## 03. Django templates and views


#### 03.1 Setting up templates and views

        modified:   README.md
        new file:   app/blog/templates/blog/post.html
        modified:   app/blog/views.py
        modified:   config/settings.py
        new file:   templates/base.html



## 04. Django urls


#### 04.1 Define urls and create posts

        modified:   app/blog/admin.py
        new file:   app/blog/urls.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   upload/images/cat-1.png



## 05. Django Static and Media Files


#### 05.1 Configure stati files

        modified:   README.md
        new file:   app/blog/static/blog/style.css
        modified:   templates/base.html

        NOTE: css is gitignored


#### 05.2 Configure media files

        modified:   README.md
        modified:   config/urls.py



## 06. Rendering Blog Posts


#### 06.1 Rendering basics posts content from db

        modified:   README.md
        modified:   app/blog/templates/blog/post.html
        new file:   upload/images/post.png

        def post_page(request, slug):
                post = Post.objects.get(slug=slug)
                context = {'post':post}
                return render(request, 'blog/post.html', context)

        path('post/<slug:slug>',views.post_page,name='post_page')

        http://127.0.0.1:8000/post/post1