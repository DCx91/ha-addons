ARG BUILD_FROM
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM ${BUILD_FROM}
COPY --from=aiostreams /app /app
COPY rootfs /
RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
 && npm install -g pnpm \
 && chmod a+x /etc/services.d/aiostreams/run \
              /etc/services.d/aiostreams/finish
