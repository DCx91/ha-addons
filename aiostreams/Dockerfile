ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.0
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM ${BUILD_FROM}
RUN apk add --no-cache nodejs openssl gcompat
COPY --from=aiostreams /app /app

ARG SQLITE_VER="12.11.2"
ARG BUILD_ARCH
RUN set -e; \
    case "${BUILD_ARCH}" in \
        amd64)   ARCH="x64"   ;; \
        aarch64) ARCH="arm64" ;; \
        *) echo "Unsupported: ${BUILD_ARCH}"; exit 1 ;; \
    esac; \
    curl -fsSL -o /tmp/better-sqlite3.tar.gz \
      https://github.com/WiseLibs/better-sqlite3/releases/download/v${SQLITE_VER}/better-sqlite3-v${SQLITE_VER}-node-v137-linuxmusl-${ARCH}.tar.gz \
    && tar -xzf /tmp/better-sqlite3.tar.gz -C /tmp \
    && TARGET=$(find /app/node_modules/.pnpm -maxdepth 1 -name "better-sqlite3@*" -type d | head -n1) \
    && cp /tmp/build/Release/better_sqlite3.node \
      "${TARGET}/node_modules/better-sqlite3/build/Release/better_sqlite3.node" \
    && rm -rf /tmp/better-sqlite3.tar.gz /tmp/build

COPY rootfs /
