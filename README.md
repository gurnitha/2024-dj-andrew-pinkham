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