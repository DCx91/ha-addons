ARG BUILD_FROM
FROM ${BUILD_FROM}
COPY rootfs /
RUN apk add --no-cache \
        unbound \
        drill \
        ldns \
        ca-certificates \
        openssl \
        curl \
 && rm -rf /var/cache/apk/* \
 && curl -sSL "https://www.internic.net/domain/named.root" \
        -o /etc/unbound/root.hints \
 && unbound-anchor -a /etc/unbound/root.key || true \
 && chown root:unbound /etc/unbound \
 && chmod 775 /etc/unbound \
 && chmod a+x /etc/s6-overlay/s6-rc.d/init-unbound/up \
              /etc/s6-overlay/s6-rc.d/unbound/run \
              /etc/s6-overlay/s6-rc.d/unbound/finish \
              /usr/local/bin/unbound-healthcheck.sh
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD /usr/local/bin/unbound-healthcheck.sh
