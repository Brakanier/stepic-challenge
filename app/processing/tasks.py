from core import helpers
from processing import services


@helpers.celery_shared_task
def create_preview(video_id: int):
    services.create_preview(video_id)


@helpers.celery_shared_task
def encode_to_mp4(video_id: int):
    services.encode_to_mp4(video_id)


@helpers.celery_shared_task
def encode_to_webm(video_id: int):
    services.encode_to_webm(video_id)
