from django.contrib import admin
from video import models


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'raw_video', 'video_mp4', 'video_webm', 'create_dt')


admin.site.register(models.Video, VideoAdmin)
