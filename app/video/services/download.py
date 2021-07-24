import io
import re
import requests

from django.core.files.uploadedfile import InMemoryUploadedFile

from video.services import logic


def download_video(url: str) -> None:
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        file_name = re.findall("filename=(.+)", r.headers['content-disposition'])[0]
        content_type = r.headers['content-type'][1]
        with io.BytesIO() as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

            file = InMemoryUploadedFile(
                file=f,
                field_name=None,
                name=file_name,
                content_type=content_type,
                size=f.tell,
                charset=None
            )
            logic.create_video(file)
