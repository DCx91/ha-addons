# NPMplus

> [NPMplus](https://github.com/ZoeyVid/NPMplus) is an enhanced fork of Nginx Proxy Manager. 
This app runs it as a Home Assistant app, letting you manage reverse proxy hosts, redirects, 
streams, and Let's Encrypt certificates from within Home Assistant.

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-App-41BDF5?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![Alpine Linux](https://img.shields.io/badge/Alpine%20Linux-3.24-0D597F?logo=alpine-linux&logoColor=white)](https://alpinelinux.org/)
![NPMplus](https://img.shields.io/badge/NPMplus-2026_11_18_r1-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


---

## Features

- Web UI on port `81` for managing proxy hosts, streams, redirections, and 404 hosts
- Automatic Let's Encrypt / ACME certificates (including wildcard via DNS challenge)
- Free and paid user management, custom SSL certificates, access lists
- IPv6 support and configurable options (Cloudflare trusted proxy, GeoIP2, log rotation)

## Installation

1. Add this repository to Home Assistant: go to **Settings → Apps → App Store → ⋮ → Repositories** and enter:

   ```
   https://github.com/DCx91/ha-addons
   ```

2. Find **NPMplus** in the app store and click **Install**.
3. Configure the options if needed (see below), then start the app.

## Accessing the web UI

The admin interface is available on port `81`:

```
http://homeassistant.local:81
```

If "Show in sidebar" is enabled, you can also open it directly from the Home Assistant sidebar.

## Logging in

The app uses Home Assistant's authentication API, so log in using your **Home Assistant username and password**. 

An admin account is created on the initial launch. The account details can be overridden 
by setting `initial_admin_email` and `initial_admin_password` before launching.

## Ports

| Port | Purpose |
| ---- | ------- |
| `80` | HTTP traffic for proxied hosts (and ACME challenges) |
| `443` | HTTPS traffic for proxied hosts |
| `81` | NPMplus admin web UI |

Do not change these if NPMplus is your main reverse proxy in front of Home Assistant.

## Configuration options

| Option | Description |
| ------ | ----------- |
| `trust_cloudflare` | Trust Cloudflare IPs as real client IPs (enable if you proxy through Cloudflare) |
| `geoip2` | Enable the GeoIP2 database (requires MaxMind .mmdb files) |
| `disable_ipv6` | Disable IPv6 support |
| `acme_email` | Email address used for Let's Encrypt certificate requests |
| `initial_admin_email` | Email for the initial admin user. Default: admin@npmplus.local |
| `initial_admin_password` | Password for the initial admin user. Default: randomly generated key |
| `logrotate` | Enable log rotation for NPMplus and Let's Encrypt logs |

## Getting started with a proxy host

1. Open the web UI and log in with your Home Assistant credentials.
2. Go to **Hosts → Proxy Hosts** and click **Add Proxy Host**.
3. Enter your domain name, point it at your Home Assistant instance (e.g. `homeassistant.local:8123`), and enable **Block Common Exploits** if desired.
4. Under the **SSL** tab, request a Let's Encrypt certificate and enable **Force SSL**.
5. Forward port `443` on your router to your Home Assistant machine (or use the app behind another proxy).

## Credits

- NPMplus is developed and maintained by [ZoeyVid](https://github.com/ZoeyVid/NPMplus)
- Nginx Proxy Manager was originally created by [Jamie Curnow](https://github.com/jc21/nginx-proxy-manager)
- This app packaging is maintained by [DCx91](https://github.com/DCx91)

## Support

For issues with this app packaging, please open an issue at [DCx91/ha-addons](https://github.com/DCx91/ha-addons/issues). For issues with NPMplus itself, see the [upstream project](https://github.com/ZoeyVid/NPMplus).
