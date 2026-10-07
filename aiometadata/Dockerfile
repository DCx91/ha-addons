ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.8
FROM ghcr.io/cedya77/aiometadata:3.4.1 AS aiometadata
FROM ${BUILD_FROM}

RUN apk add --no-cache --upgrade openssl nodejs redis

COPY --from=aiometadata /app /app

COPY rootfs /
RUN chmod +x /etc/s6-overlay/s6-rc.d/redis/run \
             /etc/s6-overlay/s6-rc.d/aiometadata/run