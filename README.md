# Calculatorservice

Simple HTTP calculator webservice built on Pyramid Webframework

It makes calculation from the JSON input and sending back the result in JSON format.

Example:
```
$ curl -X POST -H "Content-Type: application/json" -d '{"input":"1 + 1"}' http://localhost:6543/calculator
{"result": "2.0"}
```

## How to run

The easiest way to run the aplication is to use the prebulit docker image.
```
docker run --rm -d -p 6543:6543 halimi/calculatorservice
```
It listens on localhost port 6543.

Or you can run it on your machine.
Clone the repository:
```
git clone https://github.com/halimi/calculatorservice.git
```
Create a virtual environment:
```
$ cd calculatorservice
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install --no-cache-dir -r requirements.txt
```
Run the application:
```
$ python app.py
```
It listens on localhost port 6543.

To run the calculation use `curl`:
```
$ curl -X POST -H "Content-Type: application/json" -d '{"input": "1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4"}' http://localhost:6543/calculator
{"result": "4.0"}
```

To run the tests:
```
$ pytest calculatorservice/tests.py
```

To build the docker image:
```
$ docker build -t calculatorservice .
```
