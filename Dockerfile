FROM python:3.8-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # venv:
    VENV_PATH="/opt/stepik/.venv" \
    PATH="$PATH:/opt/stepik/.venv/bin" \
    TZ=UTC

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        python3-dev \
        default-libmysqlclient-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*


WORKDIR /opt/stepik
COPY ./deploy/requirements.txt ./requirements.txt
RUN python -m venv $VENV_PATH \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install uwsgi \
    && useradd -d /opt/stepik -s /bin/bash stepik \
    && chown -R stepik:stepik /opt/stepik


COPY ./deploy/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /opt/stepik/app
USER stepik
CMD ["python", "manage.py", "migrate"]