# Nginx Proxy Manager - Home Assistant app

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDCx91%2Fha-addons)

Manage reverse proxies, free SSL certificates, and access control for your Home
Assistant setup through a simple web interface, no Nginx or Let's Encrypt expertise
required.

## Features

* Publish Home Assistant, self-hosted applications, or websites behind a reverse proxy.
* Automatically obtain and renew free Let's Encrypt SSL/TLS certificates.
* Protect applications with HTTP Basic Authentication.
* Configure advanced Nginx directives for individual proxy hosts.
* Single sign-on style **auto-login** through Home Assistant's ingress.
* Optional **GeoIP2** modules for country-based rules with MaxMind databases.
* Secure by default: no ports are exposed until you enable them.

## Quick start

1. Click the button above to add this repository to Home Assistant (or add
   `https://github.com/DCx91/ha-addons` manually in the app store's repository settings).
2. Install **Nginx Proxy Manager** from the store and start it.
3. Click **Open Web UI** and create your administrator account.
4. Add your first proxy host.

To make your services reachable from the internet, expose ports **80** and **443** in
the app's **Configuration** page and forward them from your router.

## Documentation

Full setup instructions, including network configuration, proxying Home Assistant,
GeoIP2, and troubleshooting, are in [DOCS.md](DOCS.md).

## Support

Found a bug or have a question? Please
[open an issue](https://github.com/DCx91/ha-addons/issues) and include your app logs.

## Credits

This app was forked and adapted from the
[original](https://github.com/hassio-addons/addon-nginx-proxy-manager) by
[Franck Nijhof](https://github.com/frenck). Built on
[Nginx Proxy Manager](https://nginxproxymanager.com/).
