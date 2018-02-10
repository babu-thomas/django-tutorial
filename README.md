# Django Tutorial
Learning Django, a Python web framework.

## Useful commands
- Install: `pip install Django`
- Generate project: `django-admin startproject <project_name>`
- Run server: `python manage.py runserver`
- Generate new app: `python manage.py startapp <app_name>`
- Run database migrations: `python manage.py migrate`
	- This command creates the necessary database tables needed by the apps listed in `INSTALLED_APPS` setting in `settings.py`.
	- Synchronizes the models with the database schema.
- Save the changes to the model of <app_name> as a migration: `python manage.py makemigrations <app_name>`
	- This will create a python file named something like `<app_name>/migrations/0001_initial.py` which will contain the python code for the migrations.
- See the raw SQL commands that will be run on applying a migration: `python manage.py sqlmigrate <app_name> 0001`
	- This command doesn't actually run the migration. It just outputs what SQL commands will be run on migration.

## Migration Process
1. Change or create models in `models.py`
2. Create migrations for the changes: `python manage.py makemigrations`
3. Apply migrations to the database: `python manage.py migrate`