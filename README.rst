=====
QBOX
=====

Qbox is a Django app for anonymous question boxes

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'qboxapp',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('qbox/', include('qboxapp.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a answer the questions

5. Visit http://127.0.0.1:8000/qboxapp/ to ask questions.