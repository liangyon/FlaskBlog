from flask import render_template, request, Blueprint
from flaskblog.models import Post, Player

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    players = Player.query.all()
    return render_template('home.html', players=players)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
