# Set up development with Python
## How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 20.04
[click here for the full tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04#step-3-setting-up-a-flask-application)
or by following these steps

* to view this in VS code use `ctrl + shift + v`

1. `sudo apt update`

install pytnon and pip

2. `sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools`

install vertual environment

3. `sudo apt install python3-venv`

creating the environment

4. `python3 -m venv myprojectenv`

actevate the environment

5. `source myprojectenv/bin/activate`

## Setting Up a Flask Application

1. `pip install wheel`

install flask and gunicorn

2. `pip install gunicorn flask`

Creating a Sample App wherever you want

`vim ~/myproject/myproject.py`

then add this to `myproject.py`

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

remimber to allaw access through you firewall

`sudo ufw allow 5000` allaws traffic on port 5000

finally test you flask app

`python myproject.py`
