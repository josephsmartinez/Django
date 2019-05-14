# Django notes

## Project Set Up

### Python, VS Code and Linter Env Setup

Make sure to select the correct python interpreter.
> ctlr+shift+p
> python select interpreter
The setting in the .vscode file should change to reflect the correct python path

### Git Repo Set Up 

Use the django ignore file  
[gitignore files](https://gitignore.io/)

## Command line tool 

Django admin tool
> django-admin

Create a project
> django-admin startproject first_project

Create apps
> python manage.py startapp products
> python manage.py startapp blog
> python manage.py startapp profile
> python manage.py startapp cart

Manage webserver
> python manage.py runserver

Create a sacffold for the application
> python manage.py startapp first_app

NOTE: Django needs to be notified about the new application @ /project/settings.py

Syncs the current setting
> python manage.py migrate

Create admin users
> python manage.py createsuperuser

Sync databases changes or update
> python manage.py makemigrations
> python manage.py migrate

NOTE: Always run updates the models when changes are made

Using the manage.shell for code testing
> python manage.py shell

## Templates

- Remember to add the default directory path for the templates when starting a new project

## URL and Paths

## Modeles

- Remeber to update/migrate the database when changes are made
- Update the admin.py file with the newly added models, make sure to import


### Resources:

Models Fields
https://docs.djangoproject.com/en/2.2/ref/models/fields/

Views
https://docs.djangoproject.com/en/2.2/topics/http/views/

Starter Video
https://www.youtube.com/watch?v=F5mRW0jo-U4

Architecture django templates
https://oncampus.oberlin.edu/webteam/2012/09/architecture-django-templates

Example for a blog
``` text
gazette/
    __init__.py
    models.py
    views.py
    static/
        ...
    templates/
        gazette/
            __base.html
            __l_single_col.html
            __l_right_sidebar.html
            __l_left_sidebar.html
            _article_full.html
            _article_summary.html
            _author_list.html
            _author_name.html
            _category_list.html
            _navigation.html
            _tag_list.html
            article_detail.html
            article_list.html
            author_list.html
            category_list.html
            tag_list.html
```

Built in filter tags
https://docs.djangoproject.com/en/2.2/ref/templates/builtins/# Django
