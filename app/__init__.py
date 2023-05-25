from flask import Flask, request, render_template
import requests

app = Flask(__name__)
from config import Config
app.config.from_object(Config)
from app import routes