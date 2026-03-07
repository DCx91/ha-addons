ARG BUILD_FROM
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM node:24-alpine AS node
FROM ${BUILD_FROM}

COPY --from=node /usr/local /usr/local

RUN corepack enable pnpm

RUN apk add --no-cache \
    openssl \
    libstdc++

COPY --from=aiostreams /app /app

COPY rootfs /

RUN chmod a+x /etc/services.d/aiostreams/run \
 && chmod a+x /etc/services.d/aiostreams/finish