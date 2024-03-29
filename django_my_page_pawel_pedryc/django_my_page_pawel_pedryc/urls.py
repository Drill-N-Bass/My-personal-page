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

from pawel_pedryc_developer.views import home_view_pawel # for pictures

from pawel_pedryc_developer.views import MyEssaysView
# from pawel_pedryc_developer.views import my_essays

###
# import static so Django can handle uploaded files and images (without that it won't allow): 
from django.conf.urls.static import static
# acces to settings objects like `MEDIA_ROOT`, `MEDIA_URL`:
from django.conf import settings
###

from django.views.generic.base import RedirectView # 3.58.00

"""
all `static` in `urlpatterns` has to be here (in main project `urls.py`),
not in app's urls.py. Bcause it's main entry point for all requests where
I need to enable this static serving
"""

urlpatterns = [
    path('pawel_pedryc_developer/', include('pawel_pedryc_developer.urls')),
    path('', RedirectView.as_view(url='pawel_pedryc_developer/')), # 3.58.00
    path('', include('pawel_pedryc_developer.urls')),
    path('', include('hangman_game.urls')),
    path('admin/', admin.site.urls)]


"""
part below hashed because static files will be served 
by Nginx now with django_my_page_pawel_pedryc\.ebextensions\static-files.config
Previously those lines of code was needed for development
"""
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for pictures and files `settings.MEDIA_URL` part. Second for js
#   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # The simplest way to serve static files (low performance) s15e210 00:00 

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
