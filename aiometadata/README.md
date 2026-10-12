# AIOMetadata

> Self-hosted [AIOMetadata](https://github.com/cedya77/AIOMetadata) running as a Home Assistant add-on — aggregate, filter, and sort streams from multiple Stremio addons and debrid services in one place.

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-App-41BDF5?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![Alpine Linux](https://img.shields.io/badge/Alpine%20Linux-3.24-0D597F?logo=alpine-linux&logoColor=white)](https://alpinelinux.org/)
[![AIOMetadata](https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2FDCx91%2Fha-addons%2Frefs%2Fheads%2Fmain%2FAIOMetadata%2Fconfig.yaml&query=%24.version&label=AIOMetadata)](https://github.com/cedya77/AIOMetadata)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


---

## Installation

1. Go to **Settings → Apps → App Store**
2. Click **⋮** (top-right) → **Repositories**
3. Paste this repository URL and click **Add**
4. Find **AIOMetadata** in the store and click **Install**

Once installed, click **Open Web UI** or go to your public URL to configure AIOMetadata and install it into Stremio/Nuvio.

---

## Configuration

| Option | Recommended | Description |
|---|:---:|---|
| `host_name` | ✅ | Public URL of this app, e.g. `https://[domain].duckdns.org`. |
| `tmdb_api_key` | ✅ | API key for The Movie Database (TMDb), used to retrieve movie and TV metadata. |
| `single_user` | 🟡 | Optimises the app for personal use by disabling features and overhead intended for public instances. |
| `poster_cache` | 🟡 | Caches posters, artwork and icons locally to improve performance and reduce repeated downloads. |
| `verbosity` | ✅ | Controls the amount of detail included in the HA UI logs. |
| `tvdb_api_key` | ✅ | TVDB API v4 key, used to retrieve movie and TV metadata |
| `admin_key` | ❌ | Password used to gain access to /dashboard as admin. If left blank, a key will be generated on first run and can be viewed here. |
| `fanart_api_key` | ✅ | Fanart.tv API key, used to retrieve high-quality artwork. |
| `rpdb_api_key` | ✅ | Rating Poster Database (RPDb) API key, used to retrieve posters with ratings and other artwork overlays. |
| `warming_uuids` | 🟡 | User UUIDs to use for cache warming operations (max: 3 UUIDs). |

> **Note:** `host_name` should be the URL you will use to access AIOMetadata from outside your network, as this is what gets embedded into the addon manifest.

---

## Credits

- [AIOMetadata](https://github.com/cedya77/AIOMetadata) by [cedya77](https://github.com/cedya77)
