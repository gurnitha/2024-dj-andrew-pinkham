# 2024-dj-andrew-pinkham
Belajar membuat aplikasi berdasarkan bukunya Anrew Pinkham: Unleased Django


## 1.7 Creating a New Django Project and Django Apps

#### 1.7.1 Creating django project

        modified:   README.md
        new file:   manage.py
        new file:   suorganizer/__init__.py
        new file:   suorganizer/asgi.py
        new file:   suorganizer/settings.py
        new file:   suorganizer/urls.py
        new file:   suorganizer/wsgi.py

#### 1.7.2 Creating django app organizer

        new file:   organizer/__init__.py
        new file:   organizer/admin.py
        new file:   organizer/apps.py
        new file:   organizer/migrations/__init__.py
        new file:   organizer/models.py
        new file:   organizer/tests.py
        new file:   organizer/views.py

#### 1.7.3 Creating django app blog

        modified:   README.md
        new file:   blog/__init__.py
        new file:   blog/admin.py
        new file:   blog/apps.py
        new file:   blog/migrations/__init__.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/views.py

#### 1.7.4 Connecting Our New Django Apps to Our Django Project in settings.py

        modified:   README.md
        modified:   suorganizer/settings.py



## 2. Hello World

#### 2.1 Introduction

        Pass

#### 2.2 Creating a New App 

        new file:   helloworld/__init__.py
        new file:   helloworld/admin.py
        new file:   helloworld/apps.py
        new file:   helloworld/migrations/__init__.py
        new file:   helloworld/models.py
        new file:   helloworld/tests.py
        new file:   helloworld/views.py

#### 2.2.1 Registering the New App 

        modified:   suorganizer/settings.py

#### 2.3 Building Hello World

        Pass

#### 2.3.1 Webpage Data

        modified:   README.md
        modified:   helloworld/views.py

#### 2.3.2 Webpage URL

        modified:   README.md
        modified:   suorganizer/urls.py

#### 2.6.1 Removing Our Helloworld App from Our Project - Part 1 removing greeting method

        modified:   README.md
        modified:   suorganizer/urls.py

#### 2.6.2 Removing Our Helloworld App from Our Project - Part 2 removing helloworld from INSTALLED_APPS

        modified:   README.md
        modified:   suorganizer/settings.py

#### 2.6.3 Removing Our Helloworld App from Our Project - Part 3 removing helloworld app

        modified:   README.md
        deleted:    helloworld/__init__.py
        deleted:    helloworld/admin.py
        deleted:    helloworld/apps.py
        deleted:    helloworld/migrations/__init__.py
        deleted:    helloworld/models.py
        deleted:    helloworld/tests.py
        deleted:    helloworld/views.py


## 3 Programming Django Models and Creating a SQLite Database 31

#### 3.1 Introduction 31
#### 3.2 Why Use a Database? 32
#### 3.3 Organizing Our Data 32
#### 3.4 Specifying and Organizing Data in Django Using Models 36

#### 3.4.1 A First Look at Django Models and Fields - Part 1 basic

        modified:   README.md
        modified:   blog/models.py

#### 3.4.1 A First Look at Django Models and Fields - Part 2 add fields

        modified:   README.md
        modified:   blog/models.py

### 3.4.2.1 Completing Our Django Models - Part 1 basic

        modified:   README.md
        modified:   organizer/models.py

### 3.4.2.2 Completing Our Django Models - Part 2 add fields to Tag model

        modified:   README.md
        modified:   organizer/models.py

### 3.4.2.3 Completing Our Django Models - Part 3 add fields to Startup model

        modified:   README.md
        modified:   organizer/models.py

### 3.4.2.4 Completing Our Django Models - Part 4 add fields to NewsLink model

        modified:   README.md
        modified:   organizer/models.py


### 3.4.3.1 Adding Relational Fields to Our Models - Part 1 add OneToMany relationship between Startup and NewsLink

        modified:   README.md
        modified:   organizer/models.py


### 3.4.3.2 Adding Relational Fields to Our Models - Part 2 add ManyToMany relationship between Tag and Startup

        modified:   README.md
        modified:   organizer/models.py


### 3.4.3.3 Adding Relational Fields to Our Models - Part 3 add ManyToMany relationship between Tag and Startup to Post

        modified:   README.md
        modified:   blog/models.py

#### 3.4.4.1 Controlling Model Field Behavior with Field Options - Part 1 Tag model

        modified:   README.md
        modified:   organizer/models.py

#### 3.4.4.2 Controlling Model Field Behavior with Field Options - Part 2 add pub_date field to NewsLink model

        modified:   README.md
        modified:   organizer/models.py

#### 3.4.4.3 Controlling Model Field Behavior with Field Options - Part 3 add more fields to Startup model

        modified:   README.md
        modified:   organizer/models.py

#### 3.4.4.4 Controlling Model Field Behavior with Field Options - Part 4 add more fields to Post model

        modified:   README.md
        modified:   blog/models.py


#### 3.4.5.1 Adding Methods to Django Models - Part 1 add method to Tag model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.5.2 Adding Methods to Django Models - Part 2 add method to Startup model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.5.3 Adding Methods to Django Models - Part 3 add method to NewsLink model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.5.4 Adding Methods to Django Models - Part 4 add method to Post model

        modified:   README.md
        modified:   blog/models.py


#### 3.4.6.1 Controlling Model Behavior with Nested Meta Classes - Part 1 Declare Meta class in Tag model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.6.2 Controlling Model Behavior with Nested Meta Classes - Part 2 Declare Meta class in Startup model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.6.3 Controlling Model Behavior with Nested Meta Classes - Part 3 Declare Meta class in NewsLink model

        modified:   README.md
        modified:   organizer/models.py


#### 3.4.6.4 Controlling Model Behavior with Nested Meta Classes - Part 4 Declare Meta class in Post model

        modified:   README.md
        modified:   blog/models.py

#### 3.5.2 Creating Migrations

        (startup) λ python manage.py check
        System check identified no issues (0 silenced).

        (startup) λ python manage.py makemigrations organizer
        Migrations for 'organizer':
          organizer\migrations\0001_initial.py
            - Create model Startup
            - Create model Tag
            - Create model NewsLink
            - Add field tags to startup

        (startup) λ python manage.py makemigrations blog
        Migrations for 'blog':
          blog\migrations\0001_initial.py
            - Create model Post

        (startup) λ python manage.py makemigrations
        No changes detected

        modified:   README.md
        new file:   blog/migrations/0001_initial.py
        new file:   organizer/migrations/0001_initial.py


#### 3.7 String Case Ordering: Title Tag name in str method.

        modified:   README.md
        modified:   organizer/models.py


## 4. Django Templates

#### 4.1  Ch04: Code Hello World web page content (view).

        modified:   organizer/views.py

#### 4.1.1 Ch04: Code Hello World web page route (URL conf).

        modified:   README.md
        modified:   suorganizer/urls.py

#### 4.1.2 Ch04: Modify homepage view to list Tags.

        modified:   README.md
        modified:   organizer/views.py

#### 4.1.3 Ch04: Manually list tags with HTML on homepage.

        modified:   README.md
        modified:   organizer/views.py

#### 4.5.1 Ch04: Create Tag detail template with basic HTML.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_detail.html

#### 4.5.2 Ch04: Display variable in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.3 Ch04: Display variable in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.4 Ch04: Loop&print Startups in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.5 Ch04: Conditionally display Tag's Startups.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.6 Ch04: Tag detail template warns if no Startups.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html


#### 4.5.7 Ch04: Loop&print Posts in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.8 Ch04: Conditionally display Tag's Posts.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.9 Ch04: Tag detail template warns if no content.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.10 Ch04: Capitalize Tag&Post in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.11 Ch04: Use length filter in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.12 Ch04: Chain plural filter in Tag detail template.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.13 Ch04: Use count for Tag's Startup info.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html

#### 4.5.14 Ch04: Pluralize related Tag content titles.

        modified:   README.md
        modified:   organizer/templates/organizer/tag_detail.html


#### 4.6.1 Ch04-4.27: Create Tag list template.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_list.html


#### 4.6.2 Ch04-4.29: Conditionally list tags in list template.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_list.html


#### 4.6.3 Ch04-4.30: Use empty tag in Tag list template.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_list.html


#### 4.6.4 Ch04-4.33: Show empty tag equivalent using conditions.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_list.html


#### 4.6.5 Ch04-4.34: Revert to empty tag.

        modified:   README.md
        new file:   organizer/templates/organizer/tag_list.html


#### 4.6.6 Ch04-4.35: Create Startup detail template.

        modified:   README.md
        new file:   organizer/templates/organizer/startup_detail.html


#### 4.6.7 Ch04-4.41: Display Startup description as HTML.

        modified:   README.md
        new file:   organizer/templates/organizer/startup_detail.html


#### 4.6.8 Ch04-4.42: Create Startup list template.

        modified:   README.md
        new file:   organizer/templates/organizer/startup_list.html


#### 4.6.9 Ch04-4.43: Create Post detail template.

        modified:   README.md
        new file:   blog/templates/blog/post_detail.html


#### 4.6.10 Ch04-4.44: Create Post list template.

        modified:   README.md
        new file:   blog/templates/blog/post_list.html


#### 4.7.1 Ch04-4.46: Add generic template dir to settings.py

        modified:   README.md
        modified:   suorganizer/settings.py


#### 4.7.2 Ch04-4.47: Create site-wide base template.

        modified:   README.md
        new file:   templates/base.html



