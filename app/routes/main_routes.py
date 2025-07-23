from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/menu")
def menu():
    return render_template("menu.html")


@main.route("/gallery")
def gallery():
    return render_template("gallery.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")
