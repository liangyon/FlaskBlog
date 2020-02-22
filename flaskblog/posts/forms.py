from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import requests


class PostForm(FlaskForm):
    APIKey = "RGAPI-234ec76f-0cd6-4095-8286-deaa6e3103a0"
    summoner = StringField('Summoner', validators=[DataRequired()])
    submit = SubmitField('Search')


class SummonerForm(FlaskForm):
    title = StringField('Summoner Name (no spaces)',
                        validators=[DataRequired()])
    submit = SubmitField('Post')
