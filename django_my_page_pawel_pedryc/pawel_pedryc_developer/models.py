from dataclasses import field
from distutils.command import upload
# from faulthandler import disable
# from tkinter import DISABLED
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class ProgLang(models.Model):
    prog_lang_category = models.CharField(max_length=200)
    prog_lang_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.prog_lang_category}: {self.prog_lang_name}'


class SendMeMessage(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class VideoObject(models.Model):
    """
    Embed videos (youtube, vimeo).
    Documentation: https://django-embed-video.readthedocs.io/en/latest/examples.html
    Tutorial: https://www.youtube.com/watch?v=-AOPAqxAFJk
    """
    video_item_url = EmbedVideoField()  # same like models.URLField()
    # added_date = models.DateTimeField(auto_now_add=True, null=True)
    # title_video = models.CharField(max_length=200)

    # def __str__(self):
    #     return  str(self.tutorial_Title) if  self.tutorial_Title  else  " "

    # class Meta:
    #     ordering = ['-added_date']



class EssayCls(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(null=True)
    date = models.DateField(null=True)
    slug  = models.SlugField(unique=True, db_index=True) # db_index=True Improuve performance since it's part of my html path S6:91 2:30 
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to='images')
    # language = models.CharField(max_length=200)
    video = models.ForeignKey(VideoObject, blank=True, null=True, on_delete=models.SET_NULL) # One-to-many relationship
    language = models.ForeignKey(ProgLang, null=True, on_delete=models.SET_NULL) # One-to-many relationship
    guest = models.ManyToManyField(SendMeMessage, blank=True) # null=True not needed -> 2.57.20
    
    
        
#################
    ## Tweak title of the objects in admin page:
    # def __str__(self):
    #     return f'{self.title} - {self.slug}'

