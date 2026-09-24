# Changelog

## v2.16.0

<p>
  <img src="https://img.shields.io/badge/openresty-1.31.1.1-00DED7.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/certbot-5.8.0-00C6DE.svg?style=for-the-badge">
  <img src="https://img.shields.io/badge/s6overlay-3.2.3.0-00A8DE.svg?style=for-the-badge">
</p>

> [!WARNING]
> Certbot has been updated. Exercise caution with this upgrade as your DNS plugins may not work as expected and require tweaks to dependencies.  See the [Certbot Doc](https://nginxproxymanager.com/certbot/) for more info.


## New Features

- Add a Logs viewer to the UI (thanks @carlosalbertorg)
- Per-path access lists in Proxy Host modal (thanks @drakhaw)


## Changes

- Add reuseport to improve performance and reduce packet drops (thanks @7heMech)
- Update s6 overlay to support podman socket activation (thanks @fo5for)
- Changed order of escape to prevent RCE (thanks @Yasha-ops)
- Fix missing new on PermissionError so denied requests return 403, not 404 (thanks @timothestoifl24)
- Fix Insufficient private key permissions (thanks @vgoer)
- Use local QR code generation to prevent leaking 2FA keys to third-parties (thanks @vgoer)
- Fix Tencent Cloud apex and wildcard certificate issuance (thanks @xzy103)
- Collapse custom locations into a filterable list (thanks @fatihemre)
- Fix config changes not taking effect (thanks @vgoer)
- Fixed Estonian flag bug (thanks @quokkawiki)
- Keep the failed nginx config as a .conf.err file (thanks @vzagorovskiy)
- Invalidate tokens issued before a password change (thanks @jmrplens)
- Remove broken sorting from Audit Logs (thanks @12LuA)
- Redirect authenticated login visits to dashboard (thanks @hulkbig)
- Remove DNS provider credentials from disk after certbot runs (thanks @shawnhank)
- Use the row's own model and host type in regenerate-config (thanks @vzagorovskiy)
- Fix streams bracket IPv6 forward host for valid nginx upstream (thanks @addielaruee)
- Add LWS DNS certbot plugin (thanks @zergflag)
- Add Tencent Cloud EdgeOne DNS certbot plugin (thanks @hurole)
- Updated Timeweb Cloud certbot plugin (thanks @frenck)
- Updated Websupport DNS plugin (thanks @setrin)
- Updated Azure DNS certbot plugin to certbot-dns-azure-modern (thanks @cloudchristoph)
- 🇦🇿 Add Azerbaijani locale (thanks @jamalkamaladdin)
- 🇺🇦 Add Ukrainian locale (thanks @tapacko88)
- 🇮🇷 Add Persian locale (thanks @zalaghi)
- 🇩🇪 Updated German locale (thanks @CallMeLeon167)
- 🇪🇪 Updated Estonian locale (thanks @siimaarmaa)
- 🇹🇷 Updated Turkish locale (thanks @qwist1233-cpu)

## Docker images

- [jc21/nginx-proxy-manager:latest](https://hub.docker.com/layers/jc21/nginx-proxy-manager/latest/images/sha256-57d85bffc776c01909c7b24e127a69a72b7d8c75d387e6cb26c762978fc43e4c)
- [jc21/nginx-proxy-manager:2](https://hub.docker.com/layers/jc21/nginx-proxy-manager/2/images/sha256-57d85bffc776c01909c7b24e127a69a72b7d8c75d387e6cb26c762978fc43e4c)
- [jc21/nginx-proxy-manager:2.16.0](https://hub.docker.com/layers/jc21/nginx-proxy-manager/2.16.0/images/sha256-57d85bffc776c01909c7b24e127a69a72b7d8c75d387e6cb26c762978fc43e4c)

## v2.15.1-R5 (2026-09-10)

- Changed to multi-stage build to reduce installed dependencies and size of the final image.
- Added GeoIP2 config file creation.

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
