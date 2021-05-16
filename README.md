# HitCounter

This project demonstrats a simple Flask app that returns the count of the numer of times it's URL has been POSTed to. It has no persistence and resets the counter every time the server is restarted. It also uses Flask-RESTX to create Swagger docs.

## Installation

Create a Python 3 environment to run the code in:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Running the service

```sh
$ python3 app.py
```

This will bring up the service on http://localhost:5000

If you want to use different port, just pass it in the environment variable `PORT` like this:

```sh
$ PORT=8080 python3 app.py
```

You can then access the service on: http://localhost:8080

## Running the tests

This example uses PyUnit for testing and includes the `nose` runner. You can run gthe unit tests with:

```sh
$ nosetests
```
