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


#### 06.5 Allowing users to comment posts - Part 1: Configurations

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/forms.py
        new file:   app/blog/migrations/0004_comments.py
        modified:   app/blog/models.py
        modified:   app/blog/templates/blog/post.html
        modified:   app/blog/views.py

        Video:189

        Activities:

        1. In models.py:
        1.1 Import User from django contrib
        1.2 Create Comment model, place it under Post model
        2. Run and applay the migrations
        3. Register Comment model to admin
        4. Create a new file: blog/forms.py
           user Comment model to create form fields
        5. In post_page view, use the the CommentForm and pass it to  context
        6. Render data instan from the form to post page

        NOTE:

        1. Comment only added to db
        2. Comment did not showed up on the post page


#### 06.6 Allowing users to comment posts - Part 2: Rendering comments

        modified:   README.md
        modified:   app/blog/templates/blog/post.html
        modified:   app/blog/views.py

        Video:190

        Activities:

        1. post_page view add comment, and in the context
        2. render the comments to post page
        3. test to comment


        NOTE:

        1. Comment added and rendered successfully
        2. But, when refresh the browser, the same comment added again


#### 06.7 Allowing users to comment posts - Part 3: Fixing the sumbit issue on refresh

        modified:   README.md
        modified:   app/blog/views.py

        Video:191

        Activities:

        1. in views.py, use HttpResponseRedirect and redirect modules
        2. test add more comments

        NOTE:

        1. Issue fixed
        2. No more comment object re-created when refresh the browser


#### 06.8 Allowing users to comment posts - Part 4: Building replies configurations

        modified:   README.md
        new file:   app/blog/migrations/0005_comments_parent.py
        modified:   app/blog/models.py
        modified:   templates/base.html

        Video:192

        Activities:

        1. Add field parent field to Comment model + related_name as replaies
        2. Run and applay migrations
        3. Add url.js to static file and load url.js


        NOTE:

        1. The replay form works


#### 06.9 Allowing users to comment posts - Part 5: Allowing users to leave reply

        modified:   README.md
        modified:   app/blog/templates/blog/post.html
        modified:   app/blog/views.py

        Video:193

        Activities:

        1. In post page: Configure the replay form commnet
        2. In Comment views: Add logic
        3. Reply to a comment
        4. Check the reply in db

        NOTE:

        1. Comment to a comment save the comment to db.
        2. But the comment does not show up in the post page


#### 06.10 Allowing users to comment posts - Part 6: Reply to a comment

        modified:   README.md
        modified:   app/blog/templates/blog/post.html