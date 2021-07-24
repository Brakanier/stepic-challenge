from typing import List

from video import models


def video_all() -> List[models.Video]:
    return list(models.Video.objects.all())
