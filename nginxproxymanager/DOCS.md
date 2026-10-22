# Nginx Proxy Manager - Home Assistant app

Nginx Proxy Manager (NPM) provides an easy-to-use web interface for managing reverse proxies, SSL certificates, and access control, without requiring in-depth knowledge of Nginx or Let's Encrypt.

With this app you can:

* Publish Home Assistant, self-hosted applications, or websites behind a reverse proxy.
* Automatically obtain and renew free Let's Encrypt SSL/TLS certificates.
* Protect applications with HTTP Basic Authentication.
* Configure advanced Nginx directives for individual proxy hosts.
* Manage everything from a simple web interface.

## Installation

1. Add this repository to Home Assistant:

   [![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDCx91%2Fha-addons)

2. Find **Nginx Proxy Manager** in the app store and click **Install**.
3. Click **Start**, then check the **Log** tab to confirm it started successfully.
4. Click **Open Web UI**.
5. Create your administrator account when prompted, for example:

   ```
   Email:    admin@example.com
   Password: <a strong, unique password>
   ```

6. Add your first proxy host.

> [!IMPORTANT]
> Use a strong, unique password. Anyone who can log in to NPM can control every
> proxy host and certificate you manage.

> [!NOTE]
> By default, no ports are exposed, so nothing outside Home Assistant can reach NPM.
> To allow external access, set ports **80** and **443** on the app's **Configuration**
> page (see [Network configuration](#network-configuration)).

> [!NOTE]
> [Cloudflared](https://github.com/homeassistant-apps/app-cloudflared) users can set
> the "Catch-all Service" to `http://61709215-nginxproxymanager:80` without exposing
> any ports.

## Auto-login

For auto-login to work, you must first create an account in the NPM UI. Afterwards,
NPM accepts a token from Home Assistant's ingress for authentication.

* Any user with access to Home Assistant (admins by default) gets full access to NPM.
* Connections from anywhere except Home Assistant's ingress are denied.

## Network configuration

To allow external access, first expose ports 80 and 443 in the app configuration, then
forward the following ports from your router to your Home Assistant system:

| Port | Purpose                                                  |
| ---- | -------------------------------------------------------- |
| 80   | HTTP (required for Let's Encrypt HTTP-01 validation)     |
| 443  | HTTPS                                                    |

If you use IPv6, create the appropriate firewall rules on your router and allow access
to your Home Assistant system's global IPv6 address.

## Proxying Home Assistant itself

If you proxy Home Assistant through NPM, Home Assistant will reject the requests unless
it trusts the proxy. Add the following to your `configuration.yaml` and restart Home
Assistant:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 172.30.33.0/24
```

`172.30.33.0/24` is the internal Supervisor network that apps run on. Also enable
**Websockets Support** on the proxy host, or the Home Assistant frontend will not work
properly.

## GeoIP2 support

This app can load the optional GeoIP2 NGINX modules, allowing you to use MaxMind GeoIP2
databases in custom NGINX configurations.

To enable GeoIP2:

1. Enable the **GeoIP2** option in the app configuration.
2. Download a GeoLite2 or GeoIP2 database from MaxMind (a free MaxMind account is
   required for GeoLite2).
3. Copy the database to your app configuration directory, for example:

   ```
   /addon_configs/61709215_nginxproxymanager/geoip2/GeoLite2-Country.mmdb
   ```

4. Add the required GeoIP2 directives to the **Advanced** tab of your Proxy Host, for
   example:

   ```nginx
   geoip2 /config/geoip2/GeoLite2-Country.mmdb {
       auto_reload 5m;
       $geoip2_country_code country iso_code;
   }

   add_header X-GeoIP-Country $geoip2_country_code always;
   ```

After saving the Proxy Host, responses will include an `X-GeoIP-Country` header
containing the ISO country code of the client IP address.

> [!NOTE]
> Enabling the **GeoIP2** option only loads the required NGINX modules. It does not
> install or configure a GeoIP2 database automatically.

## Troubleshooting

**Let's Encrypt certificate requests fail**

* Confirm ports 80 and 443 are exposed in the app configuration and forwarded on your router.
* Confirm your domain's DNS record points to your public IP address.
* Some ISPs block inbound port 80. If yours does, use the DNS challenge instead.

**502 Bad Gateway**

* Check that the scheme (`http`/`https`), hostname or IP, and port of the proxy host are correct.
* Make sure the target service is running and reachable from the app.

**"400: Bad Request" when proxying Home Assistant**

* Add the `trusted_proxies` configuration shown in [Proxying Home Assistant itself](#proxying-home-assistant-itself).

**Cannot open the Web UI**

* Check the app logs for errors. The Web UI is only available through Home Assistant's ingress, not through the exposed ports.

## Credits

This app was forked and adapted from the [original](https://github.com/hassio-addons/addon-nginx-proxy-manager)
by [Franck Nijhof](https://github.com/frenck).
