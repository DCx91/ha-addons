ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
    && npm install -g pnpm
COPY --from=aiostreams /app /app
COPY rootfs /
