# from socket import fromshare # I need to hash it because AWS Elastic Beanstalk throws an error. More about error here: https://stackoverflow.com/questions/70964967/python-django-heroku-importerror-cannot-import-name-fromshare-from-so
from django import forms

from .models import Comment

"""
Old version with #
Changed because I don't use `send_me_message = user_feedback.save()` in views.py
That's why I swap argument in my class from `forms.ModelForm` to `forms.Form` in a new version 3:45:00
"""
# from .models import SendMeMessage

# class UserFeedback(forms.ModelForm):
#     class Meta: # 3.11.00 we connect this form model to our model in models.py
#         model = SendMeMessage
"""
if you want to have some fields from model that shouldn't be populated by user,
then list here only fields that you want to have av for user in this `fields` property
"""
#         fields = ['email']

# Below a new model (3:45:00):

class UserFeedback(forms.Form): # 3.46.00
    """
    `forms.EmailField` points out which html input field should be created
    and how it should be validated. 
    It's not related to `models.EmailField(unique=True)` in models.py. 3:46:20
    """
    email = forms.EmailField(label='Your email') # 'Your email' is html label form templates.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "text": "Your Comment"
        }

