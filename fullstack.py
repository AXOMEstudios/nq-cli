import os, requests, random

def build(d):
    print("No build for this template available.")

def _switch(d):
    try:
        os.mkdir(d)
    except FileExistsError:
        pass
    os.chdir(d)

def _leave():
    os.chdir("..")

def _add(f, c, m="w"):
    with open(f, m) as f:
        f.write(c)
        f.close()

def i(*msg):
  print(" ".join(msg))

def create(d):
    i("Setting up fullstack application")
    _switch(d)
    i("Setting up static folder...")
    _switch("static")
    i("\tDownloading dependencies...")
    _add("bulma.min.css", requests.get(
        "https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css"
    ).text)
    i("\t\tBulma: download complete")
    _add("jquery.min.js", requests.get(
        "https://code.jquery.com/jquery-3.6.0.min.js"
    ).text)
    i("\t\tjQuery: download complete")
    _add("icon.png", requests.get(
        "https://www.axome.de/img/logo_small.png"
    ).content, "wb")
    i("\t\tExample icon: download complete")
    i("\tWriting extra files...")
    _add("styles.css", "")
    _add("script.js", "")
    _add("prerequisite.js", '''$(document).ready(function() {$(".navbar-burger").click(function() {$(".navbar-burger").toggleClass("is-active");$(".navbar-menu").toggleClass("is-active");});});''')
    i("Setup of static folder complete")
    _leave()
    i("Setting up template folder...")
    _switch("templates")
    i("\tWriting base.html...")
    _add("base.html", '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="title" content="{% block meta_title %}{% endblock %}">
    <meta name="description" content="{% block meta_description %}{% endblock %}">

    <title>{% block title %}{% endblock %}</title>

    <link rel="stylesheet" href="/static/bulma.min.css">
    <link rel="stylesheet" href="/static/styles.css">
    <script src="/static/jquery.min.js"></script>
    <script src="/static/prerequisite.js"></script>
    <script src="/static/script.js"></script>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>''')
    i("\tWriting index.html...")
    _add("index.html", '''{% extends "base.html" %}

{% block title %}Page title{% endblock %}
{% block meta_title %}Example Page{% endblock %}
{% block meta_description %}This is an example page.{% endblock %}

{% block content %}
{% include "components/navbar.html" %}

<div class="section content">
    <h1>Hello, world!</h1>
</div>

{% endblock %}''')
    i("\tSetting up component folder...")
    _switch("components")
    i("\t\tWriting navbar.html...")
    _add("navbar.html", '''<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="/static/icon.png" width="28" height="28">
      </a>
  
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
  
    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <a class="navbar-item">
          Home
        </a>
  
        <a class="navbar-item">
          Documentation
        </a>
  
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            More
          </a>
  
          <div class="navbar-dropdown">
            <a class="navbar-item">
              About
            </a>
            <a class="navbar-item">
              Jobs
            </a>
            <a class="navbar-item">
              Contact
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item">
              Report an issue
            </a>
          </div>
        </div>
      </div>
  
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light">
              Log in
            </a>
          </div>
        </div>
      </div>
    </div>
  </nav>''')
    i("\tSetup of component folder complete")
    i("\tSetup of template folder complete")
    for _ in [0,0]: _leave()
    i("Writing main.py...")
    _add("main.py", '''from flask import Flask, render_template, redirect, session, g, request, flash
from os import getenv

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

app.run()''')
    i("Generating secret key...")
    _add(".env", 'SECRET_KEY="'+__import__("secrets").token_hex(64)+'"')
    i("Setup of fullstack application complete!")

def run(d):
  os.chdir(d)
  os.system("python3 main.py")

templates = {
  "page": ("page.html", '''{% extends "base.html" %}

{% block title %}Page title{% endblock %}
{% block meta_title %}Example Page{% endblock %}
{% block meta_description %}This is an example page.{% endblock %}

{% block content %}
{% include "components/navbar.html" %}

<div class="section content">
    <h1>Hello, world!</h1>
</div>

{% endblock %}'''),
  "todo": ("TODO", '''TODO List:
  -
  -
  -
    -
    -
    -'''),
  "mit-license": ("LICENSE", '''Copyright <YEAR> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''),
  "apache-license": ("LICENSE", '''Copyright <YEAR> <COPYRIGHT HOLDER>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''),
  "text": ("-text.txt", "")
}

def add(n, d="."):
  file = templates[n]
  print("Adding "+file[0]+"...")
  os.chdir(d if d != "." else ".")
  filename = file[0]
  while os.path.isfile(filename):
    filename = str(random.randint(1,999))+"-"+file[0]
  _add(filename, file[1])