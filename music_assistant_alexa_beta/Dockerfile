ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.3

# ASK-CLI builder
FROM ${BUILD_FROM} AS ask-cli-builder
RUN apk add --no-cache nodejs npm
RUN npm install -g ask-cli

# Final image
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    openssl \
    gnupg \
    python3

COPY --from=ask-cli-builder /usr/local/lib/node_modules/ask-cli /usr/local/lib/node_modules/ask-cli
RUN ln -s /usr/local/lib/node_modules/ask-cli/dist/bin/ask.js /usr/local/bin/ask
WORKDIR /app
COPY alexa_skill/app/requirements.txt app/requirements.txt
RUN python3 -m venv venv \
    && venv/bin/pip install --upgrade pip \
    && venv/bin/pip install --no-cache-dir -r app/requirements.txt
COPY alexa_skill /app
RUN venv/bin/python scripts/patch_verifier.py
COPY rootfs /
