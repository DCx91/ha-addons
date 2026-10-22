# Changelog

## v1.25.2-R4 (2026-10-22)

- #### Breaking change: Removed default port assignment.
  Set your upstream DNS in AdGuard to `61709215-unbound:5335` and boostrap DNS to `172.30.32.3` (HA's Docker DNS IP).
  
  Or add `5335` to the ports in the Configuration tab (required if your LAN uses Unbound as DNS directly).

## v1.25.2-R3 (2026-10-20)

- Fixed app being killed by Docker (exit code 137)
- Reworked cache persistence

## v1.25.2-R2 (2026-10-16)

- Simplified run script
- Fix global IPv6 address retrieval
- Update ghcr.io/hassio-addons/base Docker tag to v21.0.8

## v1.25.2-R1 (2026-08-10)

- Update ghcr.io/hassio-addons/base Docker tag to v21.0.1 (#32)

## v1.25.1-R7 (2026-07-18)

- Split HA GUI config options from main unbound.conf file so changes will be reflected in Unbound, but unbound.conf can still be manually edited.
- Enabling IPv6 now detects HA's IPv6 prefix and adds it to access-control allow list.

## v1.25.1-R6 (2026-07-02)

- Add check for existing unbound.conf (#28)

## v1.25.1-R5 (2026-06-20)

- No pull requests found for this version bump.
## v1.25.1-R4 (2026-06-20)

- Added serve-expired-client-timeout: 0 (#26)

## v1.25.1-R3 (2026-06-12)

- Removed healthcheck (#25)
- Various tweaks (#24)

## v1.25.1-R2 (2026-06-11)

- Various tweaks (#24)

## 1.25.1-R1 (2026-06-11)

 - Updated to Alpine 3.14 and Unbound 1.25.1

## v1.24.2-R1 (2026-05-01)

- Initial release (1a2b3c4)
