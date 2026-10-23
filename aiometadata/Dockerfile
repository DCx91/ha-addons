FROM ghcr.io/cedya77/aiometadata:3.7.0 AS aiometadata
FROM ghcr.io/hassio-addons/base:21.0.9

RUN apk add --no-cache openssl nodejs redis

COPY --from=aiometadata /app /app
COPY rootfs /
