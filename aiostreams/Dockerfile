ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.10
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams

FROM ${BUILD_FROM} AS prune
COPY --from=aiostreams /app /app
COPY --chmod=755 prune-deps.sh /tmp/prune-deps.sh
RUN /tmp/prune-deps.sh

FROM ${BUILD_FROM}
ENV S6_VERBOSITY=0
RUN apk add --no-cache openssl nodejs
COPY --from=prune /app /app

COPY rootfs /
