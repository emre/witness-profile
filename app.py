import json

from flask import Flask, jsonify, render_template
from config import WITNESS_PROFILE_JSON_FILE

app = Flask(__name__)

def get_witness_data():
    with open(WITNESS_PROFILE_JSON_FILE, "r") as infile:
        witness_data = json.loads(infile.read())

    return witness_data

@app.route("/")
def index():

    return render_template(
        "profile.html",
        witness_data=get_witness_data()
    )

@app.route("/api/v1/witness_profile")
def witness_profile():
    return jsonify(get_witness_data())