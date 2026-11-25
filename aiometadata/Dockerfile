ARG VERSION="4.1.0"
FROM ghcr.io/cedya77/aiometadata:${VERSION} AS aiometadata
FROM ghcr.io/hassio-addons/base:21.0.12
ENV S6_VERBOSITY=0

RUN apk add --no-cache openssl nodejs redis

COPY --from=aiometadata /app /app
COPY rootfs /
