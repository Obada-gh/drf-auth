Lab: Django REST Framework & Docker

* to run the docker:
```
docker-compose up
```
* to run the docker without keeping the terminal buzy:
```
docker-compose up -d
```
* to install postgres:
```
brew install postgresql
to start:
pg_ctl -D /home/linuxbrew/.linuxbrew/var/postgres start

to make it start ez but did not work with me :) :
echo 'alias pgstart="pg_ctl -D /home/linuxbrew/.linuxbrew/var/postgres start"' >> ~/.profile
echo 'alias pgstop="pg_ctl -D /home/linuxbrew/.linuxbrew/var/postgres stop"' >> ~/.profile
```

* IN sitting add new database:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST':'db',
        'PORT': 5432,
    }
}
```

* in docker-compose.yml:
add new service:
```
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on: 
      - db
  
  db:
    image: postgres:11

```
* reset docker:
```
docker-compose down
```
then :
``` 
docker-compose up
```
* 
```
poetry add psycopg2
```
if error:
```
in sitting:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST':'db',
        'PORT': 5432,
    }
}

in docker-compose.yml:

version: '3.9'

services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on: 
      - db

in terminal:

poetry add psycopg2-binary

docker-compose up --build

docker-compose run web python manage.py migrate





```
* create users:
```
docker-compose run web python manage.py createsuperuser
```

* permission:
```
in sitting:

REST_FRAMEWORK = {
    'DEFAUILT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

make a file in app gpus named permissions.py put this code inside it :


from rest_framework import permissions

class IscompanyOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.company




```

I think i fixed it

# __________________________________________:

auth:

```
change the port in docker-compose.yml:

version: '3.9'

services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8001
    volumes:
      - .:/code
    ports:
      - "8001:8001"
    depends_on: 
      - db

------------------------------------------------------------
Installation & Setup
For this tutorial we are going to use the djangorestframework_simplejwt library, recommended by the DRF developers.

poetry add djangorestframework_simplejwt

in settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

urls.py in project rtx

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Your URLs...
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]






```






