from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def counter():
    name=os.getenv('SECRETNAME', 'This is the default secret name')
    return name
