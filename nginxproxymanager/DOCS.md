# Nginx Proxy Manager - Home Assistant app

Nginx Proxy Manager provides an easy-to-use web interface for managing reverse proxies, SSL certificates, and access control without requiring in-depth knowledge of Nginx or Let's Encrypt.

With this app you can:

* Publish Home Assistant, self-hosted applications, or websites behind a reverse proxy.
* Automatically obtain and renew free Let's Encrypt SSL/TLS certificates.
* Protect applications with HTTP Basic Authentication.
* Configure advanced Nginx directives for individual proxy hosts.
* Manage everything from a simple web interface.

## Installation

1. Add this repository to Home Assistant:

   [![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDCx91%2Fha-addons)

2. Find **Nginx Proxy Manager** in the store and click **Install**.

3. Check the app logs to ensure it started successfully.

4. Click **Open Web UI**.

5. Create an account, for example:

   ```
   Email:    admin@example.com
   Password: changeme
   ```

6. Add hosts!

## GeoIP2 support

This app can load the optional GeoIP2 NGINX modules, allowing you to use
MaxMind GeoIP2 databases in custom NGINX configurations.

To enable GeoIP2:

1. Enable the **GeoIP2** option in the app configuration.
2. Download a GeoLite2 or GeoIP2 database from MaxMind.
3. Copy the database to your app configuration directory, for example:

   ```
   /addon_configs/61709215_nginxproxymanager/geoip2/GeoLite2-Country.mmdb
   ```

4. Add the required GeoIP2 directives to the **Advanced** tab of your Proxy Host,
   for example:

   ```nginx
   geoip2 /config/geoip2/GeoLite2-Country.mmdb {
       auto_reload 5m;
       $geoip2_country_code country iso_code;
   }

   add_header X-GeoIP-Country $geoip2_country_code always;
   ```

After saving the Proxy Host, requests will include an `X-GeoIP-Country` response
header containing the ISO country code for the client IP address.

> [!NOTE]
> Enabling the **GeoIP2** option only loads the required NGINX modules. It does
> not install or configure a GeoIP2 database automatically.

## Network configuration

To allow external access, forward the following ports from your router to your Home Assistant system:

| Port | Purpose                                                                                      |
| ---- | -------------------------------------------------------------------------------------------- |
| 80   | HTTP (for Let's Encrypt HTTP-01 certificate validation)                                      |
| 443  | HTTPS                                                                                        |
| 81   | Nginx Proxy Manager administration interface |

If you are using IPv6 instead of IPv4, create the appropriate firewall rules on your router and allow access to your Home Assistant system's global IPv6 address.

## Credits

This app was forked and adapted from the [original](https://github.com/hassio-addons/addon-nginx-proxy-manager) by [Franck Nijhof](https://github.com/frenck).
