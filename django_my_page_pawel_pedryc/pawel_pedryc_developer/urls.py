from django.urls import path
from django.views.generic.base import RedirectView # 3.58.00
from django.contrib.staticfiles.storage import staticfiles_storage # for `favicon` -> https://simpleit.rocks/python/django/django-favicon-adding/
from . import views


"""
part added below `slug:` is a Django converter that
enforces the dynamic value of the 'home_view_pawel_slug'
which in my path should have the `slug` format
from `views.py` `home_view_pawel` function.
Any other format will be rejected. 1.17.00
"""
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('pawel_pedryc\logos\media'))),
    path('', views.home_view_pawel, name='developer-home'), # my-domain.com/pawerl_pedryc_developer
    path('<slug:home_view_pawel_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:home_view_pawel_slug>', views.MyEssaysView.as_view(), name='essay-path')
    # path('<slug:home_view_pawel_slug>', views.my_essays, name='essay-path') # my-domain.com/pawel_pedryc_developer/<dynamic-path-segment> 1:16:00
]
