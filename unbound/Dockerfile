FROM ghcr.io/hassio-addons/base:21.0.11
ENV S6_VERBOSITY=1
RUN echo "@edge https://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && apk update \
    && apk add --no-cache unbound@edge \
    && curl -fsSL "https://www.internic.net/domain/named.root" -o /etc/unbound/root.hints \
    && { unbound-anchor -a /etc/unbound/root.key || true; }
COPY rootfs /
