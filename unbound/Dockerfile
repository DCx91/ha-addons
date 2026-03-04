ARG BUILD_FROM
FROM ${BUILD_FROM}

# Install Unbound and pre-reqs
RUN apk add --no-cache \
        unbound \
        drill \
        ldns \
        ca-certificates \
        openssl \
        curl \
    && rm -rf /var/cache/apk/*

# Download the IANA root hints file
RUN curl -sSL \
    "https://www.internic.net/domain/named.root" \
    -o /etc/unbound/root.hints \
    && chown root:unbound /etc/unbound/root.hints

# Download and verify the DNSSEC root anchor
RUN unbound-anchor -a /etc/unbound/root.key || true

# Copy addon filesystem overlay
COPY rootfs /

# Ensure scripts are executable
RUN chmod +x /etc/services.d/unbound/run \
    && chmod +x /etc/services.d/unbound/finish \
    && chmod +x /usr/local/bin/unbound-healthcheck.sh
