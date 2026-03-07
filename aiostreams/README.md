# AIOStreams — Home Assistant Add-on

One addon to rule them all. Runs [AIOStreams](https://github.com/Viren070/AIOStreams) as a
Home Assistant add-on so you can self-host it alongside your HA instance.

---

## Installation

1. Go to **Settings → Add-ons → Add-on Store**.
2. Click **⋮** (top-right) → **Repositories**.
3. Paste this repository's URL and click **Add**.
4. Find **AIOStreams** and click **Install**.

---

## Configuration

| Option | Required | Description |
|---|---|---|
| `secret_key` | ✅ | 64-character hex key. Generate with `openssl rand -hex 32`. |
| `base_url` | ✅ | Public URL of this addon, e.g. `http://homeassistant.local:3000`. |
| `addon_password` | No | Password(s) protecting your instance (comma-separated). |
| `log_level` | No | `error` / `warn` / `info` / `http` / `verbose` / `debug` / `silly`. Default: `http`. |
| `log_timezone` | No | e.g. `Europe/London`. Default: `Etc/UTC`. |
| `addon_name` | No | Display name. Default: `AIOStreams`. |
| `addon_id` | No | Unique identifier. Default: `aiostreams.viren070.com`. |
| `tmdb_access_token` | No | TMDB token for the Title Matching filter. |
| `builtin_stremthru_url` | No | StremThru URL for built-in addons. |
| `proxy_id` | No | `mediaflow` or `stremthru`. |
| `proxy_url` | No | URL of your MediaFlow / StremThru proxy. |
| `proxy_credentials` | No | Proxy credentials: `username:password`. |
| `addon_proxy` | No | HTTP proxy for outgoing requests (if your HA IP is blocked upstream). |

### Generating a secret key

```bash
openssl rand -hex 32
```

---

## Accessing the UI

Open `http://homeassistant.local:3000/stremio/configure` to set up AIOStreams and install it into Stremio.

## Data Persistence

All data is stored in the addon's `/data` directory and is included in HA backups automatically.

---

## Credits

- [AIOStreams](https://github.com/Viren070/AIOStreams) by [Viren070](https://github.com/Viren070)
