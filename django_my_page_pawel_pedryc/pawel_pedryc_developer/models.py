from dataclasses import field
from distutils.command import upload
# from faulthandler import disable
# from tkinter import DISABLED
from django.db import models

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

class EssayCls(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(null=True)
    date = models.DateField(null=True)
    slug  = models.SlugField(unique=True) 
    description = models.TextField()
    details = models.TextField()
    image = models.ImageField(upload_to='images')
    # language = models.CharField(max_length=200)
    language = models.ForeignKey(ProgLang, null=True, on_delete=models.SET_NULL)
    guest = models.ManyToManyField(SendMeMessage, blank=True) # null=True not needed -> 2.58.00


    ## Tweak title of the objects in admin page:
    # def __str__(self):
    #     return f'{self.title} - {self.slug}'