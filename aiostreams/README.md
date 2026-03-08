# AIOStreams

> Self-hosted [AIOStreams](https://github.com/Viren070/AIOStreams) running as a Home Assistant add-on — aggregate, filter, and sort streams from multiple Stremio addons and debrid services in one place.

---

## Installation

1. Go to **Settings → Add-ons → Add-on Store**
2. Click **⋮** (top-right) → **Repositories**
3. Paste this repository URL and click **Add**
4. Find **AIOStreams** in the store and click **Install**

Once installed, click **Open Web UI** to configure AIOStreams and install it into Stremio.

---

## Configuration

| Option | Required | Description |
|---|:---:|---|
| `base_url` | ✅ | Public URL of this add-on, e.g. `https://[domain].duckdns.org`. Most addons require HTTPS. Defaults to `http://homeassistant.local:3000`. |
| `addon_password` | ✅ | Password(s) protecting your instance. Comma-separate multiple passwords. |
| `trakt_api` | ✅ | Trakt client ID for alias lookups. Create one at [trakt.tv/oauth/applications](https://trakt.tv/oauth/applications). Without this, Trakt alias fetching is disabled. |
| `log_level` | 🟡 | Logging verbosity. One of `error`, `warn`, `info`, `http`, `verbose`, `debug`, `silly`. Default: `info`. |
| `secret_key` | 🟡 | 64-character hex key used to encrypt user data. Generate one with `openssl rand -hex 32`. If left blank, one is auto-generated and persisted across restarts. |
| `low_ram` | 🟡 | Reduces cache size and disables detailed anime database entries to lower memory usage. Recommended on devices with less than 1GB free RAM. Default: `false`. |
| `sensitive_info` | ❌ | Includes potentially sensitive values (e.g. API keys) in logs. Only enable temporarily for debugging. Default: `false`. |

> **Note:** `base_url` should be the URL you will use to access AIOStreams from outside your network, as this is what gets embedded into the Stremio addon manifest.

---

## Credits

- [AIOStreams](https://github.com/Viren070/AIOStreams) by [Viren070](https://github.com/Viren070)
