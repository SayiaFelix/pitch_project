from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


class PitchForm(FlaskForm):
    title = StringField('Pitch Name')
    category = SelectField(u'Pitch Category', choices=[('Inspiration', 'inspiration'), ('Pickup_lines', 'pickup_lines'), ('Memes', 'memes'),('POLITICAL', 'love'), ('RELIGIOUS', 'religious'), ('SPORTY', 'sporty')])
    pitch = TextAreaField('Drop Pitch')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Drop Comment')
    submit = SubmitField('Post Comments')

class UpvoteForm(FlaskForm):
    submit = SubmitField()

class Downvote(FlaskForm):
    submit = SubmitField()
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')