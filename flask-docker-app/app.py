# from flask import Flask, escape, request, render_template
from notejam import app
import flask
import datetime
import platform
import os




if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
