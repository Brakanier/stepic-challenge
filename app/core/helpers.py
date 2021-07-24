import functools
from typing import Any, Callable

import celery
from django.conf import settings


def celery_shared_task(func: Callable[..., Any]) -> Callable[..., Any]:
    celery_task = celery.shared_task(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if settings.USE_CELERY:
            return celery_task.delay(*args, **kwargs)
        else:
            return celery_task(*args, **kwargs)
    return wrapper
