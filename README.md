# Heroku, Django & Bokeh

A fork of [Getting Started with Python on Heroku](https://github.com/heroku/python-getting-started), with Bokeh added. A barebones Django site with Bokeh plots, which can easily be deployed to Heroku.

Here's an [example](https://heroku-django-bokeh.herokuapp.com/test/) output.


## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Bokeh](https://bokeh.pydata.org/en/latest/docs/installation.html).


```sh
$ git clone https://github.com/dpebert7/heroku-django-bokeh
$ cd heroku-django-bokeh

$ pipenv install

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/), with a Bokeh demo at [localhost:5000/test/](http://localhost:5000/test/)

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

For more information about deploying Bokeh, see these links:

 - [Helpful Stack Exchange Answer](https://stackoverflow.com/a/29524050/5322379)
 - [Bokeh Docs](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
