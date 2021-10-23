# Overview

```powershell
python.exe -m venv env
python.exe -m pip install --upgrade pip
pip install Django
```
### Create django project
```powershell
django-admin startproject mysite .
```

### Init sqlite database and create super user
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
User/pass: anadmin/annvt@12345

Access to admin page:
```
http://127.0.0.1:8000/admin
```

### Create new blog app
```powershell
python manage.py startapp blog
```

### Edit site's setting.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

```

### Create models

### Make data migration
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Create templates

### Edit site's setting.py
Define Template dir and add to configuration
```python
import os
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Create html

### Create views

### Create urls.py file in app folder

### Edit site's urls to include app's urls
```python
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
]
```

### Install googletrans for google api 
```python
pip install googletrans==4.0.0-rc1
```
