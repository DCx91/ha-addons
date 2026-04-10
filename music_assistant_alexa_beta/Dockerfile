ARG BUILD_FROM
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
    python3
WORKDIR /app
COPY alexa_skill/app /app/app
COPY alexa_skill/assets /app/assets
COPY alexa_skill/scripts /app/scripts
RUN python3 -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r /app/app/requirements.txt \
    && venv/bin/python /app/scripts/patch_verifier.py
RUN npm install -g ask-cli
COPY rootfs /
RUN chmod a+x \
    /app/scripts/ask_create_skill.sh \
    /etc/s6-overlay/s6-rc.d/init-alexa-skill/up \
    /etc/s6-overlay/s6-rc.d/alexa-skill/run \
    /etc/s6-overlay/s6-rc.d/alexa-skill/finish
