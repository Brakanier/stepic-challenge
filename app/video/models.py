from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image


class Video(models.Model):
    name = models.CharField(max_length=256)
    raw_video = models.FileField(upload_to='raw')
    preview_img = models.ImageField(upload_to='previews', null=True)
    video_mp4 = models.FileField(upload_to='ready_mp4', null=True)
    video_webm = models.FileField(upload_to='ready_webm', null=True)

    create_dt = models.DateTimeField(auto_now_add=True)

    def set_preview(self, img: InMemoryUploadedFile):
        self.preview_img = img
        self.save(update_fields=('preview_img',))

    def set_video_mp4_path(self, video_path: str):
        self.video_mp4.name = video_path
        self.save(update_fields=('video_mp4',))

    def set_video_webm_path(self, video_path: str):
        self.video_webm.name = video_path
        self.save(update_fields=('video_webm',))
