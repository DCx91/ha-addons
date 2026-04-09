ARG BUILD_FROM
FROM ${BUILD_FROM}
RUN apk add --no-cache \
  drill \
  ldns \
  openssl \
  unbound
RUN curl -sSL "https://www.internic.net/domain/named.root" -o /etc/unbound/root.hints \
  && unbound-anchor -a /etc/unbound/root.key || true
RUN chown root:unbound /etc/unbound \
  && chmod 775 /etc/unbound \
  && chmod a+x /etc/s6-overlay/s6-rc.d/init-unbound/up \
    /etc/s6-overlay/s6-rc.d/init-unbound/run \
    /etc/s6-overlay/s6-rc.d/unbound/run \
    /etc/s6-overlay/s6-rc.d/unbound/finish \
    /etc/s6-overlay/s6-rc.d/unbound-load-cache/up \
    /etc/s6-overlay/s6-rc.d/unbound-load-cache/run \
    /usr/local/bin/unbound-healthcheck.sh
COPY rootfs /
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD /usr/local/bin/unbound-healthcheck.sh
