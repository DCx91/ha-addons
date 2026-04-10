ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
    python3
WORKDIR /app
COPY alexa_skill /app
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r /app/app/requirements.txt \
    && venv/bin/python /app/scripts/patch_verifier.py
RUN npm install -g ask-cli
COPY rootfs /
