from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import re
import random

app = Flask(__name__)
CORS(app) # This line enables CORS for all routes.


@app.route('/summarize', methods=['POST'])  
def summarize():
    
if __name__ == '__main__':
    app.run(port = 8080)

