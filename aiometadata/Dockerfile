ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.10
FROM ghcr.io/cedya77/aiometadata:3.8.3 AS aiometadata
ENV S6_VERBOSITY=0
FROM ${BUILD_FROM}

RUN apk add --no-cache openssl nodejs redis

COPY --from=aiometadata /app /app

COPY rootfs /
