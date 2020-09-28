#!/usr/bin/python3

# genHosts-WSGI.py
# Sabi. Simple, Lightweight, but Not Beautiful

# See LICENSE for a copy of the MIT License (found in the /tools directory)
# that should be distributed with this software

# For more check out https://github.com/sabi

from flask import Flask
import os

version = 1.0

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello try entering /ansible_category/hostname\n"

@app.route("/<category>/<hostname>")
def add_newhost(category, hostname):
    out = os.popen("genHosts.py " + hostname + " " + category).read()
    return out

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='11110', debug=True)
