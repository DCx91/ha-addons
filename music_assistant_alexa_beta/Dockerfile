ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.8

# ASK-CLI builder
FROM ${BUILD_FROM} AS ask-cli-builder
RUN apk add --no-cache nodejs npm
RUN npm install -g ask-cli

# Alexa skill assets
FROM ghcr.io/alams154/music-assistant-skill:0.0.39-beta AS alexa-skill
RUN rm -rf  /app/assets \
            /app/src \
            /app/venv

# Final image
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    openssl \
    gnupg \
    python3

COPY --from=ask-cli-builder /usr/local/lib/node_modules/ask-cli /usr/local/lib/node_modules/ask-cli
COPY --from=alexa-skill /app /app
WORKDIR /app
RUN ln -s /usr/local/lib/node_modules/ask-cli/dist/bin/ask.js /usr/local/bin/ask \
    && python3 -m venv venv \
    && venv/bin/pip install --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r requirements.txt
#RUN venv/bin/python scripts/patch_verifier.py
COPY rootfs /
