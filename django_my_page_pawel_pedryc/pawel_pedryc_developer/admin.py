from django.contrib import admin
from .models import EssayCls, ProgLang, SendMeMessage, VideoItem
from embed_video.admin import AdminVideoMixin

## Tweak title of the objects in admin page:
class EssayAdmin(admin.ModelAdmin):
    list_display         = ('title', 'date', 'slug', 'description', 'language')
    list_filter          = ('language', 'date')
    prepopulated_fields  = {'slug': ('title',)} #2:41:00

    
admin.site.register(EssayCls, EssayAdmin)
admin.site.register(ProgLang)
admin.site.register(SendMeMessage)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoItem, MyModelAdmin)