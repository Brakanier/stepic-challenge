from django.conf import settings
from django.core import files, exceptions


def size_validator(value: files.File):
    limit = 1024 * 1024 * settings.MAX_VIDEO_SIZE
    if value.size > limit:
        raise exceptions.ValidationError(f'Video file too large, file should be less then {settings.MAX_VIDEO_SIZE}')
