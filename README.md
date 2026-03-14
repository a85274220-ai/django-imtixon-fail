# django-imtixon-fail

$ git clone
$ python -m venv venv
$ source venv/Scripts/activate
$ mkdir src
$ pip install django 
$ pip freeze > requirements.txt
$ cd src/
$ django-admin startproject config .
$ mkdir apps
$ mkdir templates
$ python manage.py startapp book apps/book
$ python manage.py startapp user apps/user