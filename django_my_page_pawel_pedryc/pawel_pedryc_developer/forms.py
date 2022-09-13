from socket import fromshare
from django import forms

"""
Old version with #
"""
# from .models import SendMeMessage

# class UserFeedback(forms.ModelForm):
#     class Meta: # 3.11.00
#         model = SendMeMessage
#         fields = ['email']
        
class UserFeedback(forms.Form): # 3.46.00
    email = forms.EmailField(label='Your email')


