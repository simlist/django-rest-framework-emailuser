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

Requirements
------------

- Python 3.5+
- Django 2.2+
- Djangorestframework 3.10+

Installation
------------

Install using ``pip``::

   $ pip install djangorestframework_emailuser

Add ``'emailuser'`` to ``INSTALLED_APPS``:

.. code-block:: Python

  # myproject/settings.py
  INSTALLED_APPS = [
      ...
      'emailuser',
  ]

Add the following line to ``settings.py`` to override django's default User
model with the 'EmailUser' model:

.. code-block:: Python

  # myproject/settings.py
  AUTH_USER_MODEL = 'emailuser.EmailUser'
