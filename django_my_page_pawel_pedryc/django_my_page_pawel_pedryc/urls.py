"""apiarena_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from hangman_game.views import easter_egg_hangman_game

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage # for `favicon` -> https://simpleit.rocks/python/django/django-favicon-adding/
from pawel_pedryc_developer.views import home_view_pawel # for pictures

from pawel_pedryc_developer.views import my_essays # for videos

###
# import static so Django can handle uploaded files and images: 
from django.conf.urls.static import static
# acces to settings objects like `MEDIA_ROOT`, `MEDIA_URL`:
from django.conf import settings
###

from django.views.generic.base import RedirectView # 3.58.00


urlpatterns = [
    path('pawel_pedryc_developer/', include('pawel_pedryc_developer.urls')),
    path('', RedirectView.as_view(url='pawel_pedryc_developer/')), # 3.58.00
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('pawel_pedryc\logos\media\favicon.ico'))),
    path('', include('pawel_pedryc_developer.urls')),
    path('', include('hangman_game.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for pictures and files

# at this point it doesn't work:
urlpatterns += staticfiles_urlpatterns() # for pictures 

"""
Debug function related to 'Django Debug Toolbar':

Debugging tools for developer mode.
Script below will add path decribed below to paths that was defined previously.

Documentation: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
Tutorial: https://www.youtube.com/watch?v=qWLk9S6mvAY
"""

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
