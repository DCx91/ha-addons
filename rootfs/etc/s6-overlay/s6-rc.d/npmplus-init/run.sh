#!/command/with-contenv bashio
set -euo pipefail

export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

tz="$(bashio::info.timezone || echo 'UTC')"

emit_bool() {
    local name="$1" key="$2" value="false"
    if bashio::config.true "${key}"; then
        value="true"
    fi
    printf '%s=%q\n' "${name}" "${value}"
}

emit_opt() {
    local name="$1" key="$2"
    if bashio::config.has_value "${key}"; then
        printf '%s=%q\n' "${name}" "$(bashio::config "${key}")"
    fi
}

env_tmp="$(mktemp /data/.env.XXXXXX)"
{
    printf 'TZ=%q\n' "${tz}"
    emit_bool DISABLE_IPV6     disable_ipv6
    emit_bool LOGROTATE        logrotate
    emit_bool TRUST_CLOUDFLARE trust_cloudflare
    emit_opt  ACME_EMAIL             acme_email
    emit_opt  INITIAL_ADMIN_EMAIL    initial_admin_email
    emit_opt  INITIAL_ADMIN_PASSWORD initial_admin_password
    emit_opt  TRUST_IP               trust_ip
} > "${env_tmp}"

# Persistent cookie secret (generated once, survives restarts)
secret_file=/data/npmplus/cookie_secret
mkdir -p /data/npmplus
if [ ! -s "${secret_file}" ]; then
    bashio::log.info "Generating new cookie secret"
    if ! openssl rand -hex 32 > "${secret_file}"; then
        rm -f "${secret_file}" "${env_tmp}"
        bashio::exit.nok "Failed to generate cookie secret (is openssl installed?)"
    fi
    chmod 600 "${secret_file}"
fi
printf 'COOKIE_SECRET=%q\n' "$(cat "${secret_file}")" >> "${env_tmp}"

chmod 600 "${env_tmp}"
mv "${env_tmp}" /data/.env

bashio::log.info "Wrote /data/.env ($(wc -c < /data/.env) bytes, $(grep -c . /data/.env) lines): $(grep -o '^[A-Z_]*' /data/.env | tr '\n' ' ')"

if [ -s "/usr/share/zoneinfo/${tz}" ]; then
    ln -sf "/usr/share/zoneinfo/${tz}" /etc/localtime
else
    bashio::log.warning "Timezone '${tz}' not found in /usr/share/zoneinfo; leaving /etc/localtime unchanged"
fi

rm -f /tmp/env.sha512sum

mkdir -p /run/npmplus-shim
cat > /run/npmplus-shim/dinit <<'EOF'
#!/usr/bin/env bash
export -p > /run/npmplus.env
EOF
chmod +x /run/npmplus-shim/dinit
export PATH="/run/npmplus-shim:${PATH}"

cd /app

bashio::log.info "NPM Plus starting..."
exec /usr/local/bin/entrypoint.sh