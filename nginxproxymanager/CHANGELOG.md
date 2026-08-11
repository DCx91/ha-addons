# Changelog

## v2.15.1-R2 (2026-08-11)

- Added logging verbosity toggle. Reduces noise by hiding successful requests from the HA log.
- Merged patches.
  
## v2.15.1-R1 (2026-08-07)

  - Fixed patches failing on build.

## v2.15.1

<p>
  <img src="https://img.shields.io/badge/openresty-1.29.2.5-00DED7.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/certbot-5.6.0-00C6DE.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/s6overlay-3.2.1.0-00A8DE.svg?style=for-the-badge">
</p>


## Changes

- Base image reverts to Lua v5.1.5
- Fix #5611 when internal nginx conf files are over mounted

## Docker images

- [jc21/nginx-proxy-manager:latest](https://hub.docker.com/layers/jc21/nginx-proxy-manager/latest/images/sha256-99a885f56ca2203a2eb352a5f9e2cd5c1e25786508debd725ad48ebe955d114f)
- [jc21/nginx-proxy-manager:2](https://hub.docker.com/layers/jc21/nginx-proxy-manager/2/images/sha256-99a885f56ca2203a2eb352a5f9e2cd5c1e25786508debd725ad48ebe955d114f)
- [jc21/nginx-proxy-manager:2.15.1](https://hub.docker.com/layers/jc21/nginx-proxy-manager/2.15.1/images/sha256-99a885f56ca2203a2eb352a5f9e2cd5c1e25786508debd725ad48ebe955d114f)

- No pull requests found for this version bump.
