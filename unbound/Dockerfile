FROM ghcr.io/hassio-addons/base:21.0.9
RUN apk add --no-cache unbound
RUN curl -fsSL "https://www.internic.net/domain/named.root" -o /etc/unbound/root.hints \
  && { unbound-anchor -a /etc/unbound/root.key || true; }
COPY rootfs /
