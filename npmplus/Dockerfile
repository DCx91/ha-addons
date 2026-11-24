ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.11
ARG NPMPLUS_VERSION=2026-11-18-r1

# Frontend
FROM alpine:3.24 AS npmplus-frontend
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
ARG NODE_ENV=production \
    NODE_OPTIONS=--use-openssl-ca \
    NPMPLUS_VERSION
WORKDIR /app
RUN apk add --no-cache nodejs pnpm patch curl tar \
    && curl -fsSL "https://github.com/ZoeyVid/NPMplus/archive/refs/tags/${NPMPLUS_VERSION}.tar.gz" -o /tmp/npmplus.tgz \
    && tar -xzf /tmp/npmplus.tgz -C /tmp \
    && cp /tmp/NPMplus-${NPMPLUS_VERSION}/frontend/package.json \
          /tmp/NPMplus-${NPMPLUS_VERSION}/frontend/pnpm-lock.yaml \
          /tmp/NPMplus-${NPMPLUS_VERSION}/frontend/pnpm-workspace.yaml /app/ \
    && pnpm install --frozen-lockfile \
    && cp -a /tmp/NPMplus-${NPMPLUS_VERSION}/frontend/. /app/ \
    && rm -rf /tmp/NPMplus-${NPMPLUS_VERSION} /tmp/npmplus.tgz
COPY patch/npmplus-ha-auth-api-frontend.patch /tmp/
RUN patch -d /app -p 1 < /tmp/npmplus-ha-auth-api-frontend.patch \
    && sed -i 's/"email-address"/"username"/g' /app/src/pages/Login/index.tsx \
    && pnpm formatjs compile-folder src/locale/src src/locale/lang \
    && pnpm tsc \
    && pnpm vite build

# Backend
FROM ghcr.io/zoeyvid/npmplus:${NPMPLUS_VERSION} AS npmplus-backend

COPY patch/npmplus-ha-auth-api-backend.patch /usr/src/
RUN apk add --no-cache patch \
    && patch -d /app -p 1 < /usr/src/npmplus-ha-auth-api-backend.patch \
    && sed -i 's/Invalid email or password/Invalid username or password/' /app/internal/token.js \
    && sed -i 's/if (logger !== express) logger.debug(...args);/return;/' /app/logger.js \
    && rm -f /usr/local/bin/git-clone-commit.sh \
        /usr/local/bin/ech.sh \
        /usr/local/bin/bssl \
        /usr/local/nginx/modules/ngx_http_auth_ldap_module.so \
        /usr/local/nginx/modules/ngx_http_js_module.so \
        /usr/local/nginx/modules/ngx_stream_js_module.so \
        /usr/local/nginx/modules/ngx_http_upstream_ntlm_module.so \
        /usr/local/nginx/modules/ngx_http_vhost_traffic_status_module.so \
    && mkdir -p /stage/etc /stage/usr \
    && rm -rf /app/frontend \
    && cp -a /app /usr/local /stage \
    && cp -a /etc/certbot.ini /etc/logrotate \
       /etc/crowdsec.conf.example /etc/crowdsec.conf.original \
       /etc/ban.html.original /etc/captcha.html.original \
       /stage/etc/

# Final image
FROM ${BUILD_FROM}

RUN apk add --no-cache \
      libstdc++ llvm-libunwind libc++ \
      pcre2 luajit zlib-ng brotli zstd lua5.1-cjson libmaxminddb-libs \
      coreutils findutils grep openssl tzdata \
      logrotate nodejs python3 uv

COPY --from=npmplus-backend /stage/ /
COPY --from=npmplus-frontend /app/dist /app/frontend
COPY --chmod=755 rootfs /

ENV NODE_ENV=production \
    NODE_OPTIONS=--use-openssl-ca \
    UV_CONSTRAINT=/etc/pip-constraints.txt \
    UV_OVERRIDE=/etc/pip-overrides.txt \
    S6_VERBOSITY=0

WORKDIR /app
