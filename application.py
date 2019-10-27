from flask import Flask, render_template
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html","index.css")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
