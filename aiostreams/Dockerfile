ARG BUILD_FROM
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    nodejs \
    npm \
    openssl \
    libstdc++
RUN npm install -g pnpm

COPY --from=aiostreams /app /app
COPY rootfs /

RUN chmod a+x /etc/services.d/aiostreams/run \
 && chmod a+x /etc/services.d/aiostreams/finish
