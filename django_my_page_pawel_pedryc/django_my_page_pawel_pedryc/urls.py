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

###
# import static so Django can handle uploaded files and images: 
from django.conf.urls.static import static
# acces to settings objects like `MEDIA_ROOT`, `MEDIA_URL`:
from django.conf import settings
###


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view, name='home'),
    # path('home/', home_view, name='home'),
    path('', include('hangman_game.urls')),
    path('', include('pawel_pedryc_developer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for pictures and files

# at this point it doesn't work:
urlpatterns += staticfiles_urlpatterns() # for pictures 