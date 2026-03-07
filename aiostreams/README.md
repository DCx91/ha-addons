# AIOStreams — Home Assistant App

Runs [AIOStreams](https://github.com/Viren070/AIOStreams) as a
Home Assistant app so you can self-host it alongside your HA instance.

---

## Installation

1. Go to **Settings → Add-ons → Add-on Store**.
2. Click **⋮** (top-right) → **Repositories**.
3. Paste this repository's URL and click **Add**.
4. Find **AIOStreams** and click **Install**.

---

## Configuration

| Option | Recommended | Description |
|---|---|---|
| `base_url` | ✅ | Public URL of this addon, e.g. `https://[domain].duckdns.org`. Addons may require HTTPS. Default: `http://homeassistant.local:3000`|
| `log_level` | 🟡 | `error` / `warn` / `info` / `http` / `verbose` / `debug` / `silly`. Default: `info`. |
| `trakt_id` | ✅ | Provide a Trakt client ID for authorised requests to get trakt aliases. Create one here: https://trakt.tv/oauth/applications |
| `low_ram` | 🟡 | Reduces cache size & prevents anime db entries to reduce memory consumption. Default: `false` |
| `addon_password` | ✅ | Password(s) protecting your instance (comma-separated). |
| `sensitive_info` | ❌ | Includes potentially sensitive info (like API keys) in logs for debugging. |
| `secret_key` | 🟡 | 64-character hex key. Generate with `openssl rand -hex 32`. Default: `blank` (auto-generate) |

---

## Accessing the UI

Click `Open web UI` to set up AIOStreams and install it into Stremio.

---

## Credits

- [AIOStreams](https://github.com/Viren070/AIOStreams) by [Viren070](https://github.com/Viren070)
