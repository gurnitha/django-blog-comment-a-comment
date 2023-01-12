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


#### 06.2 Building the homepage (basics content)

        modified:   README.md
        new file:   app/blog/templates/blog/index.html
        modified:   app/blog/urls.py
        modified:   app/blog/views.py

        NOTE: Rendering some contens only(not yet complete in this 186 video)


#### 06.3 Building and Reder Tags

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/migrations/0002_tag_post_tags.py
        modified:   app/blog/models.py
        modified:   app/blog/templates/blog/post.html

        Activities:

        1. Build Tag model
        2. Add relationship with Post model + related_name
        3. Run and applay migrations
        4. Register Tag to admin
        5. Add some tag in admin
        6. Open post + select tag/s
        7. Render tags to post.html

        NOTE: just a basics (not complete the post page yet)

        # IN THE TERMINAL

        F:\_workspace\blog\blog-comment-a-comment (main)
        (venv3941) λ REM: open shell

        ...
        >>> from app.blog.models import Post, Tag
        >>> posts = Post.objects.all()
        # show first post --> [0]
        >>> posts[0]
        <Post: Post object (1)>
        # show all tags belongs to post1
        >>> posts[0].tags.all()
        <QuerySet [<Tag: tag1>, <Tag: tag2>]>

        IN THE POST PAGE

        <div class="blog-tags">
            {% for tag in post.tags.all %}
              <div class="tag">{{tag.name}}</div>
            {% endfor %}
        </div>


#### 06.4 Counting the views

        modified:   README.md
        new file:   app/blog/migrations/0003_post_view_count.py
        modified:   app/blog/models.py
        modified:   app/blog/templates/blog/post.html
        modified:   app/blog/views.py

        Video:188

        Activities:

        1. Add view_count field in Post model
        2. Run and appllay migrations
        3. Add logic for post view in post_page view
        4. Load view_count to post page
        5. Testing: refresh the browser
        6. Result: It works

        NOTE: Every time the browser is refreshed, view_count is added