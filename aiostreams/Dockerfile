ARG BUILD_FROM=ghcr.io/hassio-addons/base:21.0.0
FROM ghcr.io/viren070/aiostreams:latest AS aiostreams
FROM ${BUILD_FROM}
RUN apk add --no-cache nodejs openssl
COPY --from=aiostreams /app /app

ARG SQLITE_VER="12.11.2"
ARG BUILD_ARCH
RUN set -eux; \
    case "${BUILD_ARCH}" in \
        amd64)   ARCH="x64"   ;; \
        aarch64) ARCH="arm64" ;; \
        *) echo "Unsupported: ${BUILD_ARCH}"; exit 1 ;; \
    esac; \
    NODE_ABI=$(node -e "console.log(process.versions.modules)"); \
    echo "Detected Node ABI: ${NODE_ABI}"; \
    PKG_DIR="$(find /app/node_modules/.pnpm -maxdepth 1 -name "better-sqlite3@*" -type d | head -n1)/node_modules/better-sqlite3" \
    && curl -fsSL -o /tmp/better-sqlite3.tar.gz \
      "https://github.com/WiseLibs/better-sqlite3/releases/download/v${SQLITE_VER}/better-sqlite3-v${SQLITE_VER}-node-v${NODE_ABI}-linuxmusl-${ARCH}.tar.gz" \
    && tar -xzf /tmp/better-sqlite3.tar.gz -C "${PKG_DIR}" \
    && rm -f /tmp/better-sqlite3.tar.gz

COPY rootfs /
