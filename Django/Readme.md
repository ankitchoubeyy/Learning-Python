## Framework

- Framework is structure intended to serve as a guide for building applications that expands the structure into something useful.

## Library

- It is the predefined code you use to build an application.
- Provides more flexibility as you can pick and choose which parts to use and how to use them.

## Library vs Framework

| **Library** | **Framework** |
| --- | --- |
| It is the predefined code | Provides a complete structure and architecture for building applications. |
| The control flow is in your hands, so it is more flexible. | A very basic application is already created. You just expand it's functionalities. |
| ex: **React, NumPy** | ex: **Django, Next, Angular** |

* * *

## Django Introduction

- It is a python based free and open source `web framework`
- It follow a model **view-template architectural pattern**.
- It is maintained by **Django software foundation**.
- primary goal to create **complex**, **database** driven websites.
- companies using Django: **YouTube**, **Dropbox**, **Mozilla**, **Instagram**.etc.

### History

- Developed in 2003 by **Adrian Holovaty**, **Simon willison**.
- First version is released in **2005**
- In **2008**, Django software foundation in established to maintained this.

### Features

- Fast Development
- Provides web servers for development and testing.
- Scalability
- loaded with apps
- secure

* * *

### Django Installation

- Write this command in your terminal to install Django.

```py
python -m pip install Django==5.1
```

* * *

## Steps to perform

1.  Create project
2.  create a web app
3.  update `settings.py`
4.  Defining views
5.  Set URL for the view in `urls.py`

### 1\. Creating a project with Django

- To create your project in Django use command given below:
- `django-admin startproject firstProject`
- After this command a directory will be created with name firstProject and inside this directory another firstProject directory will be crated know as child firstProject directory.  
    ![5ef692e3ecb5720b8c6166a93aba0a98.png](:/a68261ecebef4c1d9d4cd52a8a2e7d9a)
- Let's understand the folder structure of this directory:
- `_*init*_.py` : is an empty file. It's presence make the folder as python package.
- `settings.py` : Contains project related setting statement.
- `urls.py` : contains **URL** pattern to web pages.
- `wsgi.py` : is a **web server gateway interface**, it is a special file, **no modification** is required in this file.
- `asgi.py` : is asynchronous gateway interface, it describe a common interface between a python web app and the web server.
- `manage.py` : is a program to do same initial stuff. *Never edit this file.*

### How to start our own Django web server?

To run the web server write the command in terminal which is given below:

```py
python manage.py runserver 
```

- By default port no. is 8000, but you can change it by specifying port number at the end of the command.
- Running web server at Port: 3000 `python manage.py runserver 3000`
- **Note**: Before running above command make sure that you're in the current project directory.

### 2\. How to create a web app?

1.  To create a web app, Run the given command below inside the parent directory where `manage.py` is located.

- Command:

```py
python manage.py startapp testapp
```

- Here **testapp** can be anything according to your choice.

### 3\. Update `settings.py`

- make an entry for this app.

![d475f8cf8f60b649e9c8ec28833e21ca.png](:/9272c25628b1488e87475477668fa6ea)

### 4\. Defining Django View

- Views are the python functions that takes **HTTP request** and return **HTTP response**.
- This response can be the **HTML contents** of a web page, or a **redirect**, or a **404 error**, or anything.

### What is the purpose of a view?

- Django use **MVT** (Model view template)
- views are the part of user interface.
- **Purpose**: to take request, perform business logic and return HTTP response.

### Where to create a view?

- go to the web app directory `views.py` file.  
    ![e908b896310dab6c13c580eaba86eb74.png](:/af0a90796b114e9687e09f79ec94cf11)
- Define your function for the request and return a HTTP response

```py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting(req):
    msg = "Hello and welcome to first view"
    return HttpResponse(msg)
```

### 5.Updating our web `urls.py`

- Go to the firstProject directory open `urls.py`
- import the required modules and update URL pattern list.

```py
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting', views.greeting),
]
```

- Now, start your web server and go to `localhost:8000/greeting` and your view will be appear.

![03d74a063a95ee1cb03226f7ffb69d80.png](:/9ba90503dc8e49bab868954e84ec3362)

* * *

### App level URLs

**Why we need app level URLs?**

- To improve the reusablility of web apps. instead of placing all the views url in the project level we can define our own app level url.

How to create app level URls?

1.  Create `urls.py` in each app. and define the path as you initially dfine your path in firstProject `urls.py`
- example: define app level urls of **testapp**
```py
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('greeeting', views.greeting),
    path('about', views.about),
    path('contact', views.contact),
]
```

2.  go to **firstProject** urls.py and configure your apps urls using `include()`

```py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include #import this include function

urlpatterns = [
   path('admin/', admin.site.urls),
   path('testapp/', include('testapp.urls')),
   path('exam/', include('exam.urls')),
]
```

---
## Templates in Django
- In Django, templates are used to separate the presentation layer (HTML) from the business logic (Python code). 
- Django's templating system allows you to create dynamic HTML by embedding special syntax within the HTML files. 
- Here’s an overview of Django templates:
### 1. Creating a Template
Templates are usually stored in a directory named templates within your Django app.
Example directory structure:
```
firstproject/
    		exam/
        		templates/
            		result.html
```

### 2. Using a Template in a View
In your Django view, you can render a template using the render function.
Example:
```py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def result(req):
    template = loader.get_template('result.html')
    res = template.render()
    return HttpResponse(res)
```

### Dynamic content in our template
- we want to insert dynamic content from view functio to template file then we will use Dynamic behaviour.
- **view** contains bussiness logic, which results in data to be displayed on the page.