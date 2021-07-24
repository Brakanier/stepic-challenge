import uuid

from django.core import files

from video import models, tasks
from processing import tasks as processing_tasks


def create_video(file: files.File) -> None:
    video = models.Video.objects.create(
        name=file.name,
        raw_video=file
    )
    start_processing(video.id)


def start_processing(video_id: int) -> None:
    processing_tasks.create_preview(video_id)
    processing_tasks.encode_to_mp4(video_id)
    processing_tasks.encode_to_webm(video_id)


def download_video(video_url: str) -> None:
    tasks.download_video(video_url)
