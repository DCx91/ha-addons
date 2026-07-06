ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.0
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
    gnupg \
    python3
WORKDIR /app
COPY alexa_skill/app/requirements.txt app/requirements.txt
RUN python3 -m venv venv \
    && venv/bin/pip install --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r app/requirements.txt
COPY alexa_skill /app
RUN venv/bin/python scripts/patch_verifier.py
RUN npm install -g ask-cli
COPY rootfs /