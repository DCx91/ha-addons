# Nginx Proxy Manager - Home Assistant app

Nginx Proxy Manager provides an easy-to-use web interface for managing reverse proxies, SSL certificates, and access control without requiring in-depth knowledge of Nginx or Let's Encrypt.

With this app you can:

* Publish Home Assistant, self-hosted applications, or websites behind a reverse proxy.
* Automatically obtain and renew free Let's Encrypt SSL/TLS certificates.
* Protect applications with HTTP Basic Authentication.
* Configure advanced Nginx directives for individual proxy hosts.
* Manage everything from a simple web interface.

## Installation

Installing the app is the same as installing any other Home Assistant app.

1. Open the app page in your Home Assistant instance.

2. Click **Install**.

3. Start the **Nginx Proxy Manager** app.

4. Check the app logs to ensure it started successfully.

5. Click **Open Web UI**.

6. Create an account, for example:

   ```
   Email:    admin@example.com
   Password: changeme
   ```

7. Add hosts!

## GeoIP2 support

This add-on can load the optional GeoIP2 NGINX modules, allowing you to use
MaxMind GeoIP2 databases in custom NGINX configurations.

To enable GeoIP2:

1. Enable the **GeoIP2** option in the add-on configuration.
2. Download a GeoLite2 or GeoIP2 database from MaxMind.
3. Copy the database to your add-on configuration directory, for example:

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