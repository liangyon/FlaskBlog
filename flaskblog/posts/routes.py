from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post, Player
from flaskblog.posts.forms import PostForm
import requests

posts = Blueprint('posts', __name__)
players = Blueprint('players', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    APIKey = "RGAPI-234ec76f-0cd6-4095-8286-deaa6e3103a0"
    # if form.validate_on_submit():
    #     post = Post(title=form.title.data,
    #                 content=form.content.data, author=current_user)
    #     db.session.add(post)
    #     db.session.commit()
    #     flash('Your post has been created!', 'success')
    #     return redirect(url_for('main.about'))

    if form.validate_on_submit():
        summonerName = form.summoner.data
        print(summonerName)
        responseJson = requestSummonerData('na1', summonerName, APIKey)
        print(responseJson)
        player = Player(id=summonerName,
                        player_id=responseJson['id'], name=responseJson['name'])
        db.session.add(player)
        db.session.commit()
        flash('player added!', 'success')
        return redirect(url_for('main.about'))
    return render_template('create_post.html', title='Search Summoner', form=form, legend='Search Summoner')


@posts.route("/post/<int:post_id>")
def post(post_id):
    summoner = Player.query.get_or_404(post_id)
    return render_template('summoner.html', title=summoner.name, post=post)


# @posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# @login_required
# def update_post(post_id):
#     post = Post.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


def requestSummonerData(region, summonerName, APIKey):
    URL = "https://" + region + ".api.riotgames.com/lol/" + \
        "summoner/v4/summoners/by-name/" + summonerName + '?api_key=' + APIKey
    # https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/ori%C3%B3n
    print(URL)
    response = requests.get(URL)
    return response.json()


def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + \
        ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + '?api_key=' + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()


def requestLiveData(region, ID, APIKey):
    URL = "https://" + region + \
        ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + \
        ID + '?api_key=' + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()
