ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.2
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# Copy patches
COPY patches/*.patch /usr/src/

# Setup base
ARG NGINX_PROXY_MANAGER_VERSION="v2.15.1"

# hadolint ignore=DL3003,DL3042
RUN \
    # 1) Install build-time and runtime dependencies
    apk add --no-cache --virtual .build-dependencies \
        build-base \
        git \
        libffi-dev \
        openssl-dev \
        patch \
        python3-dev \
    && apk add --no-cache \
        apache2-utils \
        certbot \
        libcap \
        logrotate \
        nginx-mod-stream \
        nginx-mod-http-geoip2 \
        nginx-mod-stream-geoip2 \
        nginx \
        nodejs \
        npm \
        openssl \
        py3-pip \
        python3 \
        yarn \
    && yarn global add modclean \
    \
    # 2) Fetch and unpack Nginx Proxy Manager sources
    && curl -J -L -o /tmp/nginxproxymanager.tar.gz \
        "https://github.com/NginxProxyManager/nginx-proxy-manager/archive/${NGINX_PROXY_MANAGER_VERSION}.tar.gz" \
    && mkdir /app \
    && tar zxf \
        /tmp/nginxproxymanager.tar.gz \
        --strip 1 -C /app \
    \
    # 3) Apply patches and bump backend version
    && for i in /usr/src/*.patch; do \
        patch -d /app -p 1 < "${i}"; \
       done \
    && sed -i "s/\"version\": \"2.0.0\"/\"version\": \"${NGINX_PROXY_MANAGER_VERSION#v}\"/" \
        /app/backend/package.json \
    \
    # 4) Build frontend assets
    && cd /app/frontend \
    && yarn install --ignore-engines --network-timeout 100000 \
    && yarn locale-compile \
    && yarn build \
    && rm -rf node_modules \
    \
    # 5) Prepare backend and runtime layout
    && mkdir -p /opt/nginx-proxy-manager/frontend \
    && cp -a /app/frontend/dist/. /opt/nginx-proxy-manager/frontend/ \
    && cp -a /app/backend/. /opt/nginx-proxy-manager/ \
    \
    && cd /opt/nginx-proxy-manager \
    && yarn install --production \
    && sed -i \
        's|const cmd = `. /opt/certbot/bin/activate && pip install --no-cache-dir ${quotedDeps} '\''${plugin.package_name}${plugin.version}'\'' && deactivate`|const cmd = `python3 -m pip install --no-cache-dir ${quotedDeps} '\''${plugin.package_name}${plugin.version}'\''`|' \
        /opt/nginx-proxy-manager/lib/certbot.js \
    && rm -rf /etc/services.d/frontend \
    && rm -rf /opt/nginx-proxy-manager/config \
    \
    # 6) Configure Nginx and related files
    && rm -rf /etc/nginx \
    && cp -r /app/docker/rootfs/etc/nginx /etc/nginx \
    && rm -f /etc/nginx/conf.d/dev.conf \
    \
    && cp /app/docker/rootfs/etc/letsencrypt.ini /etc \
    && cp /app/docker/rootfs/etc/logrotate.d/nginx-proxy-manager /etc/logrotate.d \
    \
    && sed -i "s#user npm;#user root;#" /etc/nginx/nginx.conf \
    && sed -i "s#root /app/frontend;#root /opt/nginx-proxy-manager/frontend;#" \
        /etc/nginx/conf.d/production.conf \
    && sed -i "s#table.string('id').notNull().primary();#table.string('id', 32).notNull().primary();#" \
        /opt/nginx-proxy-manager/migrations/20190227065017_settings.js \
    \
    && mkdir -p \
        /run/nginx \
        /tmp/nginx/cache/public \
        /tmp/nginx/cache/private \
    \
    # 7) Clean up build artifacts, caches, and dev dependencies
    && modclean \
        --path /opt/nginx-proxy-manager \
        --no-progress \
        --keep-empty \
        --run \
    \
    && yarn global remove modclean \
    && yarn cache clean \
    \
    && apk del --purge .build-dependencies \
    \
    && rm -rf \
        /app \
        /etc/init.d/nginx \
        /opt/nginx-proxy-manager/node_modules/bcrypt/build \
        /root/.cache \
        /root/.node-gyp \
        /tmp/.[!.]* \
        /tmp/* \
        /usr/lib/node_modules \
        /usr/local/share/.cache \
        /var/lib/nginx \
        /var/log/nginx \
        /var/tmp/nginx \
        /var/www

# Copy root filesystem
COPY rootfs /

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION