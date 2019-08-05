djangorestframework_emailuser
=============================

.. image:: https://travis-ci.org/simlist/django-rest-framework-emailuser.svg?branch=dev
    :target: https://travis-ci.org/simlist/django-rest-framework-emailuser

.. image:: https://coveralls.io/repos/github/simlist/django-rest-framework-emailuser/badge.svg?branch=dev
    :target: https://coveralls.io/github/simlist/django-rest-framework-emailuser?branch=dev

Overview
--------

A user for djangorestframework that uses an email as the username.

Features
--------

* Use email as username for loging in
* One name field instead of first name and last name
* Endpoints for creating an account, viewing, and updating accounts
* Django admin to work with EmailUser model.

Requirements
------------

- Python 3.5+
- Django 2.2+
- Djangorestframework 3.10+

Installation and Configuration
------------------------------

Install using ``pip``:

.. code_block:: Shell

  $ pip install djangorestframework_emailuser

Add ``'emailuser'`` to ``INSTALLED_APPS``:

.. code-block:: Python

  # mysite/settings.py
  INSTALLED_APPS = [
      ...
      'emailuser',
  ]

Add the following line to ``settings.py`` to override django's default User
model with the 'EmailUser' model:

.. code-block:: Python

  # mysite/settings.py
  AUTH_USER_MODEL = 'emailuser.EmailUser'

Add urls to url conf:

.. code-block:: Python

  # mysite/urls.py
  from django.urls import path, include
  urlpatterns = [
    ...
    path('accounts/', include('emailuser.urls')),
  ]

Using
-----
To create a user programatically:

.. code-block:: Python

  from django.contrib.auth import get_user_model
  normal_user = get_user_model().objects.create_user(
      email='me@example.com',
      name='My Name',
      password='MyPassword'
  )

  superuser = get_user_model().objects.create_superuser(
      email='admin@example.com',
      name='Super Name',
      password='MySuperPassword'
  )

To create a user 
The EmailUser model has the following attributes:
* email
  The email address used as the login username.
* name
  A single field for the name of the user.
* password
  The password is hashed as set by the django settings.
* is_superuser
  A boolean attribute that can only be set programatically.
* is_staff
  A boolean attribute that can be set by the admin site or
  programatically.