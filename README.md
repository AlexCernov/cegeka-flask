# cegeka-flask

In order to install the application run:

> python setup.py

OR

> pip install -e .

The project is run using the flask run command. In order for this command to work, flask has to know the entrypoint of the flask app. To specify that, we use the environment variable called FLASK_APP.

FLASK_APP has three parts: an optional path that sets the current working directory, a Python file or dotted import path, and an optional variable name of the instance or factory. If the name is a factory, it can optionally be followed by arguments in parentheses.

In our case, while being inside the git repo directory, the environment variable can be set: 
- For linux/mac, in terminal:
```
export FLASK_APP=flaskr.app
```
- For windows(PowerShell)
```
$env:FLASK_APP='flaskr.app'
```
- For windows(CMD)
```
set FLASK_APP=flaskr.app
```

To run the app, type in the terminal:
```
flask run
```
To run the command, type in the terminal:
```
flask print
```