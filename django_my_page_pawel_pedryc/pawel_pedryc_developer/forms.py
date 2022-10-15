from socket import fromshare
from django import forms

"""
Old version with #
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
        
class UserFeedback(forms.Form): # 3.46.00
    email = forms.EmailField(label='Your email')


