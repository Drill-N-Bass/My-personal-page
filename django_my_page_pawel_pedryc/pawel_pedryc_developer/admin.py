from django.contrib import admin
from .models import EssayCls, ProgLang, SendMeMessage, VideoObject, Tag, Comment
from embed_video.admin import AdminVideoMixin

## Tweak title of the objects in admin page:
class EssayAdmin(admin.ModelAdmin):
    list_display         = ('title', 'date', 'description', 'language', 'slug',) # Keep in mind it's tuple
    list_filter          = ('language', 'date', 'tags',) # Keep in mind it's tuple
    prepopulated_fields  = {'slug': ('title',)} #2:41:00


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

    
admin.site.register(EssayCls, EssayAdmin)
admin.site.register(ProgLang)
admin.site.register(SendMeMessage)
admin.site.register(Comment, CommentAdmin)

# class TagFilter(admin.ModelAdmin):
#     list_filter = ()

admin.site.register(Tag)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoObject, MyModelAdmin)