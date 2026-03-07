#!/usr/bin/with-contenv bashio

LISTEN_PORT=$(bashio::config 'listen_port')

# Check if Unbound is listening on the configured port
if ! drill -p "${LISTEN_PORT}" unbound.net @127.0.0.1 > /dev/null 2>&1; then
    bashio::log.warning "Healthcheck: DNS query to Unbound on port ${LISTEN_PORT} failed."
    exit 1
fi

bashio::log.info "Healthcheck: Unbound is healthy on port ${LISTEN_PORT}."
exit 0
