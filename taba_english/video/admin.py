from django.contrib import admin
from video.models import Video


class VideoAdmin(admin.ModelAdmin):
	list_display = ('name', 'file')


admin.site.register(Video, VideoAdmin)
