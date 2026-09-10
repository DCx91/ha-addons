ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.5

# Fetch + patch source
FROM ${BUILD_FROM} AS source
ARG NGINX_PROXY_MANAGER_VERSION="v2.15.1"

COPY patches/*.patch /usr/src/
RUN apk add --no-cache tar patch \
    && curl -J -L -o /tmp/nginxproxymanager.tar.gz \
        "https://github.com/NginxProxyManager/nginx-proxy-manager/archive/${NGINX_PROXY_MANAGER_VERSION}.tar.gz" \
    && mkdir /app \
    && tar zxf /tmp/nginxproxymanager.tar.gz --strip 1 -C /app \
    && for i in /usr/src/*.patch; do \
        patch -d /app -p 1 < "${i}"; \
       done \
    && sed -i "s/\"version\": \"2.0.0\"/\"version\": \"${NGINX_PROXY_MANAGER_VERSION#v}\"/" \
        /app/backend/package.json \
    && chmod 644 /app/docker/rootfs/etc/logrotate.d/nginx-proxy-manager

# Build
FROM ${BUILD_FROM} AS build

# hadolint ignore=DL3042
RUN apk add --no-cache \
        build-base \
        libffi \
        nodejs \
        python3 \
        py3-pip \
        yarn \
    && yarn global add modclean

COPY --from=source /app /app

# Build frontend
RUN cd /app/frontend \
    && yarn install --ignore-engines --network-timeout 100000 \
    && yarn locale-compile \
    && yarn build

# Build backend
RUN mkdir -p /opt/nginx-proxy-manager \
    && cp -a /app/backend/. /opt/nginx-proxy-manager/ \
    && cd /opt/nginx-proxy-manager \
    && yarn install --production \
    && sed -i \
        's|const cmd = `. /opt/certbot/bin/activate && pip install --no-cache-dir ${quotedDeps} '\''${plugin.package_name}${plugin.version}'\'' && deactivate`|const cmd = `python3 -m pip install --no-cache-dir --break-system-packages ${quotedDeps} '\''${plugin.package_name}${plugin.version}'\''`|' \
        /opt/nginx-proxy-manager/lib/certbot.js \
    && sed -i "s#table.string('id').notNull().primary();#table.string('id', 32).notNull().primary();#" \
        /opt/nginx-proxy-manager/migrations/20190227065017_settings.js \
    && rm -rf /opt/nginx-proxy-manager/config \
    && modclean \
        --path /opt/nginx-proxy-manager \
        --no-progress \
        --keep-empty \
        --run \
    && rm -rf /opt/nginx-proxy-manager/node_modules/bcrypt/build \
    && yarn cache clean

# Final image
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

RUN apk add --no-cache \
        apache2-utils \
        certbot \
        libcap \
        logrotate \
        nginx \
        nginx-mod-stream \
        nginx-mod-http-geoip2 \
        nginx-mod-stream-geoip2 \
        nodejs \
        openssl \
        python3 \
        py3-pip

COPY --from=source /app/docker/rootfs/etc/nginx /etc/nginx
COPY --from=source /app/docker/rootfs/etc/letsencrypt.ini /etc/letsencrypt.ini
COPY --from=source /app/docker/rootfs/etc/logrotate.d/nginx-proxy-manager /etc/logrotate.d/nginx-proxy-manager
COPY --from=build /app/frontend/dist /opt/nginx-proxy-manager/frontend
COPY --from=build /opt/nginx-proxy-manager /opt/nginx-proxy-manager

RUN rm -f /etc/nginx/conf.d/dev.conf \
    && sed -i "s#user npm;#user root;#" /etc/nginx/nginx.conf \
    && sed -i "s#root /app/frontend;#root /opt/nginx-proxy-manager/frontend;#" /etc/nginx/conf.d/production.conf \
    && mkdir -p \
        /run/nginx \
        /tmp/nginx/cache/public \
        /tmp/nginx/cache/private \
    && rm -rf \
        /etc/init.d/nginx \
        /etc/nginx/conf.d/stream.conf \
        /etc/nginx/modules/*.conf \
        /etc/services.d/frontend \
        /var/lib/nginx \
        /var/log/nginx \
        /var/tmp/nginx \
        /var/www

COPY rootfs /
