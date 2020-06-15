from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post')


class Vote(FlaskForm):
    submit = SelectField('Like')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('bio', validators=[Required()])
    submit = SubmitField('Post')