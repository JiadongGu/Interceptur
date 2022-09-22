from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/index")
def index():
    if request.method == "POST":
        rqs = request.form.get("id")
        page = requests.get(f"https://www.nationstates.net/page=faction/fid={rqs}/view=incoming")
        soup = BeautifulSoup(page.content, 'html.parser')
        incoming = soup.find_all("table", _class = "FILLIN")
        if incoming:
            win32api.mouse_click(x, y)
        return render_template("app.py")
    else:
        return render_template("app.py")
