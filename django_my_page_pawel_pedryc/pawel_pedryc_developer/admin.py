from django.contrib import admin
from .models import EssayCls, ProgLang, SendMeMessage, VideoObject, Tag, Comment, MyEmail
from embed_video.admin import AdminVideoMixin

## Tweak title of the objects in admin page:
class EssayAdmin(admin.ModelAdmin):
    list_display         = ('title', 'date', 'description', 'language', 'slug',) # Keep in mind it's tuple
    list_filter          = ('language', 'date', 'tags',) # Keep in mind it's tuple
    prepopulated_fields  = {'slug': ('title',)} #2:41:00


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

class MyEmailAdmin(admin.ModelAdmin):
    list_display = ("email", "date")

    
admin.site.register(EssayCls, EssayAdmin)
admin.site.register(ProgLang)
admin.site.register(SendMeMessage)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MyEmail, MyEmailAdmin)

# class TagFilter(admin.ModelAdmin):
#     list_filter = ()

admin.site.register(Tag)

class VideoObjectAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoObject, VideoObjectAdmin) # błąd w nazwie raczej