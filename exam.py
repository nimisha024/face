# * --------- IMPORTS --------- *
# All the imports that we will need in our API
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import psycopg2
import cv2
import numpy as np
import re

# We define the path of the current file, we will use it later
FILE_PATH = os.path.dirname(os.path.realpath(__file__))


# * ---------- Create App --------- *
# Init the app
app = Flask(__name__)
# To avoid cors erros
CORS(app, support_credentials=True)


# * -------------------- Run Server -------------------- *
if __name__ == '__main__':
    # * --- DEBUG MODE: --- *
    app.run(host='127.0.0.1', port=5000, debug=True)
