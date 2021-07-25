import io
import os
import pathlib

from django.core.files.uploadedfile import InMemoryUploadedFile
from moviepy import editor
from moviepy.video.fx import resize
from PIL import Image
from video import models


def create_preview(video_id: int) -> None:
    video_model = models.Video.objects.get(id=video_id)

    with io.BytesIO() as image_io:
        # create thumbnail
        with editor.VideoFileClip(video_model.raw_video.path) as video:
            frame = video.get_frame(video.duration // 2)
            image = Image.fromarray(frame)
            image.thumbnail((640, 360), Image.ANTIALIAS)
            image.save(image_io, format='JPEG')

        basename, _ = os.path.splitext(os.path.basename(video_model.raw_video.path))

        file = InMemoryUploadedFile(
            file=image_io,
            field_name=None,
            name=f'{basename}_preview.jpg',
            content_type='image/jpeg',
            size=image_io.tell,
            charset=None
        )

        video_model.set_preview(file)


def encode_to_mp4(video_id: int) -> None:
    video_model = models.Video.objects.get(id=video_id)

    with editor.VideoFileClip(video_model.raw_video.path) as video:
        new_video = resize.resize(video, (640, 360))

        basename, _ = os.path.splitext(os.path.basename(video_model.raw_video.path))

        location = video_model.video_mp4.storage.location
        upload_to = models.Video.video_mp4.field.upload_to

        filename = f'{basename}.mp4'

        if upload_to:
            file_name_for_save = f'{upload_to}/{filename}'
            path = os.path.join(location, upload_to, filename)
            dir_path = os.path.join(location, upload_to)
        else:
            file_name_for_save = filename
            path = os.path.join(location, filename)
            dir_path = os.path.join(location)

        create_dirs(dir_path)
        new_video.write_videofile(path)
        video_model.set_video_mp4_path(file_name_for_save)


def encode_to_webm(video_id: int) -> None:
    video_model = models.Video.objects.get(id=video_id)

    with editor.VideoFileClip(video_model.raw_video.path) as video:
        new_video = resize.resize(video, (640, 360))

        basename, _ = os.path.splitext(os.path.basename(video_model.raw_video.path))

        location = video_model.video_webm.storage.location
        upload_to = models.Video.video_webm.field.upload_to

        filename = f'{basename}.webm'

        if upload_to:
            file_name_for_save = f'{upload_to}/{filename}'
            path = os.path.join(location, upload_to, filename)
            dir_path = os.path.join(location, upload_to)
        else:
            file_name_for_save = filename
            path = os.path.join(location, filename)
            dir_path = os.path.join(location)


        create_dirs(dir_path)
        new_video.write_videofile(path)
        video_model.set_video_webm_path(file_name_for_save)


def create_dirs(path: str):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
