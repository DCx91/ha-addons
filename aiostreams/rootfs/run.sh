#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
set -e

# Persistent storage
mkdir -p /data

# Helper for optional config values with defaults
config_or_default() {
    local key="$1" default="$2"
    bashio::config.has_value "${key}" && bashio::config "${key}" || echo "${default}"
}

# Database selection
POSTGRESQL=$(bashio::config 'postgresql_enabled')
if [ "$POSTGRESQL" == "true" ]; then
    HOST=$(bashio::config 'postgresql_host')
    PORT=$(bashio::config 'postgresql_port')
    USERNAME=$(bashio::config 'postgresql_username')
    PASSWORD=$(bashio::config 'postgresql_password')
    DATABASE=$(bashio::config 'postgresql_database')

    MISSING=()
    [ -z "$HOST" ]     && MISSING+=("postgresql_host")
    [ -z "$PORT" ]     && MISSING+=("postgresql_port")
    [ -z "$USERNAME" ] && MISSING+=("postgresql_username")
    [ -z "$PASSWORD" ] && MISSING+=("postgresql_password")
    [ -z "$DATABASE" ] && MISSING+=("postgresql_database")

    if [ ${#MISSING[@]} -gt 0 ]; then
        bashio::log.error "PostgreSQL is enabled but the following fields are missing: ${MISSING[*]}"
        exit 1
    fi

    bashio::log.info "Using PostgreSQL at ${HOST}:${PORT}"
    export DATABASE_URI=postgres://${$USERNAME}:${PASSWORD}@${HOST}:$PORT/$DATABASE
else
    bashio::log.info "PostgreSQL not enabled, defaulting to SQLite."
    export DATABASE_URI="sqlite:///data/db.sqlite"
fi

# Secret key - use the value from config if set, otherwise auto-generate
# and persist it to /data/secret_key so it survives restarts.
SECRET_KEY_FILE="/data/secret_key"

bashio::log.info "Checking secret key..."
if bashio::config.has_value 'secret_key'; then
    SECRET_KEY=$(bashio::config 'secret_key')
    bashio::log.info "Using secret_key from app configuration."
else
    if [[ -f "${SECRET_KEY_FILE}" ]]; then
        SECRET_KEY=$(cat "${SECRET_KEY_FILE}")
        bashio::log.info "Using existing auto-generated secret_key from ${SECRET_KEY_FILE}."
    else
        bashio::log.info "Generating new secret_key..."
        SECRET_KEY=$(openssl rand -hex 32)
        echo "${SECRET_KEY}" > "${SECRET_KEY_FILE}"
        chmod 600 "${SECRET_KEY_FILE}"
        bashio::log.info "Generated new secret_key and saved to ${SECRET_KEY_FILE}."
    fi
fi
export SECRET_KEY="${SECRET_KEY}"

# Map app options to AIOStreams environment variables
bashio::log.info "Reading configuration..."

export LOG_LEVEL=$(bashio::config 'log_level')
export LOG_TIMEZONE=$(bashio::info.timezone)
export PORT=$(bashio::addon.port "3000/tcp")
export ADDON_NAME="AIOStreams"
export ADDON_ID="aiostreams"
export BUILTIN_STREMTHRU_URL="https://stremthru.13377001.xyz"
export LOG_SENSITIVE_INFO="$(config_or_default 'sensitive_info' false)"
export NODE_OPTIONS="--max-old-space-size=500"

# Base URL
if bashio::config.has_value 'base_url'; then
    export BASE_URL="$(bashio::config 'base_url')"
else
    export BASE_URL="http://homeassistant.local:${PORT}"
fi

# Password protection
bashio::config.has_value 'addon_password' && export ADDON_PASSWORD="$(bashio::config 'addon_password')"

# Trakt Client ID
if bashio::config.has_value 'trakt_id'; then
    export TRAKT_CLIENT_ID="$(bashio::config 'trakt_id')"
else
    export FETCH_TRAKT_ALIASES=false
fi

# Anime API
ANIME_API=$(bashio::config 'anime_api')
if [[ "${ANIME_API}" == "false" ]]; then
    export ANIME_DB_LEVEL_OF_DETAIL=none
    export DEFAULT_MAX_CACHE_SIZE=5000
fi

# Trusted UUID
bashio::config.has_value 'trusted_uuid' && export TRUSTED_UUIDS="$(bashio::config 'trusted_uuid')"

# Log basic info
bashio::log.info "Starting AIOStreams..."
bashio::log.info "Base URL       : ${BASE_URL}"
bashio::log.info "Port           : ${PORT}"
bashio::log.info "Database       : ${DATABASE_URI}"
bashio::log.info "Log Level      : ${LOG_LEVEL}"
bashio::log.info "Timezone       : ${LOG_TIMEZONE}"
bashio::log.info "Anime DB       : ${ANIME_API}"
bashio::log.info "Sensitive Info : ${LOG_SENSITIVE_INFO}"
bashio::log.info "Password       : $(bashio::config.has_value 'addon_password' && echo 'enabled' || echo 'disabled')"
bashio::log.info "Trakt          : $(bashio::config.has_value 'trakt_id' && echo 'configured' || echo 'not set (aliases disabled)')"
bashio::log.info "Trusted UUID   : $(bashio::config.has_value 'trusted_uuid' && echo 'configured' || echo 'unconfigured')"

# Start AIOStreams
cd /app
exec pnpm run start
