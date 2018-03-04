# Django Tutorial
Learning Django, a Python web framework.

## Useful commands
- Install: `pip install Django`
- Generate project: `django-admin startproject <project_name> .`
	- Notice the `.`(period) at the end. This will generate the project in the current directory.
	- A project generated in the root repo is necessary to deploy on Heroku.
- Run server: `python manage.py runserver`
- Generate new app: `python manage.py startapp <app_name>`
- Run database migrations: `python manage.py migrate`
	- This command creates the necessary database tables needed by the apps listed in `INSTALLED_APPS` setting in `settings.py`.
	- Synchronizes the models with the database schema.
- Save the changes to the model of <app_name> as a migration: `python manage.py makemigrations <app_name>`
	- This will create a python file named something like `<app_name>/migrations/0001_initial.py` which will contain the python code for the migrations.
- See the raw SQL commands that will be run on applying a migration: `python manage.py sqlmigrate <app_name> 0001`
	- This command doesn't actually run the migration. It just outputs what SQL commands will be run on migration.
- Create an admin user who can login to the admin site: `python manage.py createsuperuser`
- Run tests: `python manage.py test`
	- Output verbosity can be set by `verbosity` argument. For example, `--verbosity=2`

## Migration Process
1. Change or create models in `models.py`
2. Create migrations for the changes: `python manage.py makemigrations`
3. Apply migrations to the database: `python manage.py migrate`

## Sending password reset email
- For debugging, the console email backend can be used. This will just print the email to the console.
- To use the console email client add the following line to `settings.py`:
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
- To actually send emails to users, a service like [Sendgrid](https://sendgrid.com/) can be used.
- Follow the below steps to configure Sendgrid:
	1. Create free account on Sendgrid
	2. Once logged in, choose `SMTP Relay` option of sending mail, then create an `API Key`.
	3. Make note of the username and password given.
	4. Add the username and password to environment variables:
		- In Windows this can be done by:
		```
		set SENDGRID_USERNAME=<your_username>
		set SENDGRID_PASSWORD=<your_password>
		```
	4. In the Django application, add the following lines to `settings.py`:
	```
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = 'smtp.sendgrid.net'
	EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
	EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True
	```


## Deploy to Heroku
1. Make an account on [Heroku](https://www.heroku.com/) and install their [CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Install gunicorn server: `pipenv install gunicorn`
3. Set `ALLOWED_HOSTS` in `settings.py` to `['*']`
4. Ensure `Pipfile.lock` is present in repo root
5. Create `Procfile` in repo root
	- Example [here](https://github.com/babu-thomas/django-tutorial/blob/master/Procfile)
6. Login to Heroku account from command line: `heroku login`
7. Create new app on Heroku: `heroku create`
8. Add hook for Heroku within git: `heroku git:remote -a <app_name>`
9. Configure static files
	- Either ignore static files or serve them using [WhiteNoise](http://whitenoise.evans.io/en/stable/)
	- Ignore: `heroku config:set DISABLE_COLLECTSTATIC=1`
	- Use WhiteNoise
		- Install: `pipenv install whitenoise`
		- Add whitenoise to `INSTALLED_APPS` in `settings.py` above the built-in staticfiles app
		```
		INSTALLED_APPS = [
		...
		'whitenoise.runserver_nostatic`, # here
		'django.contrib.staticfiles`,
		...
		]
		```
		- Add whitenoise to `MIDDLEWARE` in `settings.py` after `SecurityMiddleware` and `SessionMiddleware`
		```
		MIDDLEWARE = [
		'django.middleware.security.SecurityMiddleware',
		'django.contrib.sessions.middleware.SessionMiddleware',
		'whitenoise.middleware.WhiteNoiseMiddleware', # here
		...
		```
		- Add `STATIC_ROOT` and `STATICFILES_STORAGE` setting in `settings.py`
		```
		STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
		STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
		```
		
10. Push code to Heroku: `git push heroku master`
11. Make app live: `heroku ps:scale web=1`
12. Open app in browser: `heroku open`
