#!/usr/bin/with-contenv bashio
LISTEN_PORT=$(bashio::app.port '5335/udp')

# Check if Unbound is listening on the configured port
if ! dig -p "${LISTEN_PORT}" . NS @127.0.0.1 > /dev/null 2>&1; then
    bashio::log.warning "Healthcheck: DNS query to Unbound on port ${LISTEN_PORT} failed."
    exit 1
fi

bashio::log.info "Healthcheck: Unbound is healthy on port ${LISTEN_PORT}."
exit 0
