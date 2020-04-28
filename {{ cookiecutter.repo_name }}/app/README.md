# HTTP Web Service

This is an HTTP API skeleton to run model inference. The web app is powered by Flask.

## Running the web app

From the project root:

```
inv app.start
```

The app is available at http://localhost:5000/.

If the source code (``*.py` files) is updated, the app is reloaded automatically in development mode.

## Example Usage

```
curl --location --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"data":[[0, 1], [2, 3]]}'
```

```
[
  2,
  2
]
```

## Creating an app on Heroku

From the project root:

```
inv app.create [HEROKU APP NAME]
```

If an app name isn't provided, `inv app.create` attempts to find an APP_NAME environment variable and creates the app using that name.

```
APP_NAME=nlp-disaster-tweets
heroku create -a $APP_NAME
heroku buildpacks:add -a $APP_NAME https://github.com/heroku/heroku-buildpack-multi-procfile
heroku buildpacks:add heroku/python
heroku config:set PROCFILE=app/Procfile
git push heroku master
```
