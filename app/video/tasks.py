from core import helpers
from video.services import download


@helpers.celery_shared_task
def download_video(url: str):
    download.download(url)
