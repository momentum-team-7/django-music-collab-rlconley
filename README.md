# Project
We will be re-creating your iTunes app, using Django this time.
The big difference is that you will be storing the data about songs,
albums, and artists *in your database* rather than pulling them from
the Spotify API. 

## Monday Morning & Break
- Start the Project
- Create the Album model
- Add some test albums to the database via the admin
- Write URL/view/template to render all the albums

# Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- A starting Django app named `core` is provided.
- There is a custom user model defined in `core.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is used to manage dependencies.

## Using this template

In an empty directory, run:

```
django-admin startproject --template=https://github.com/momentumlearn/django-project-template/archive/main.zip --name=Pipfile project .
pipenv install
pipenv shell
cp project/.env.sample project/.env
./manage.py makemigrations
./manage.py migrate
```

If you want to use another directory for your project directory, replace `project` above with the name of your directory.


