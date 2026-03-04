ARG BUILD_FROM
FROM ${BUILD_FROM}

ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version="${BUILD_VERSION}" \
    maintainer="Your Name <your@email.com>" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Add-on" \
    org.opencontainers.image.authors="Your Name <your@email.com>" \
    org.opencontainers.image.revision="${BUILD_REF}" \
    org.opencontainers.image.created="${BUILD_DATE}"

# Install Unbound and pre-reqs from madnuttah/unbound-docker
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
