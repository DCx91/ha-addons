# Unbound DNS — Home Assistant App

A validating, recursive, caching DNS resolver for your home network, adapted
from [madnuttah/unbound-docker](https://github.com/madnuttah/unbound-docker).

---

## What is Unbound?

Unbound is a high-performance DNS resolver developed by NLnet Labs. Rather
than forwarding queries to a third-party DNS server (like 8.8.8.8), Unbound
resolves domains recursively by walking the DNS hierarchy itself — starting from
the root nameservers. This means no third party ever sees your DNS queries.

It also validates DNSSEC signatures, protecting you from DNS spoofing attacks.

---

## Installation

1. Add this repository to Home Assistant:
   **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
   Paste in the URL of this repo.

2. Find **Unbound DNS** in the store and click **Install**.

3. Adjust the configuration options to suit your network, then click **Start**.

---

## Configuration

| Option | Default | Description |
|---|---|---|
| `log_level` | `1` | Logging verbosity (0–5) |
| `listen_port` | `5335` | Port Unbound listens on (UDP + TCP) |
| `do_ipv6` | `false` | Enable IPv6 resolution |
| `num_threads` | `1` | Worker thread count |
| `access_control` | RFC 1918 ranges | Subnets allowed to query Unbound |
| `hyperlocal` | `true` | Stores a local copy of the DNS root zone for faster resolution |
| `persist_cache` | `true` | Dumps & restores cache on restart |
| `cache_min_ttl` | `300` | Minimum TTL for cached records (seconds) |
| `cache_max_ttl` | `86400` | Maximum TTL for cached records (seconds) |
| `custom_config` | `""` | Raw Unbound config appended to `unbound.conf` |

---

## Using with Pi-hole or AdGuard Home

Set upstream DNS server to:

```
<your-HA-IP>:5335 or 127.0.0.1:5335
```

This routes all DNS queries through Unbound for fully private, recursive
resolution.

---

## Custom Configuration Files

You can place additional `.conf` files in the persistent config directory
(`/addon_configs/<slug>/conf.d/`). These are included automatically, letting
you add things like:

- `forward-zone` entries for split-horizon DNS
- `local-data` for custom hostnames
- `stub-zone` entries for internal domains

Example `conf.d/local.conf`:
```
server:
    local-data: "myserver.home. IN A 192.168.1.50"
    local-data-ptr: "192.168.1.50 myserver.home."
```

---

## Ports

| Port | Protocol | Description |
|---|---|---|
| 5335 | UDP | DNS queries |
| 5335 | TCP | DNS over TCP / large responses |

---

## Credits

This add-on is a Home Assistant adaptation of the excellent
[madnuttah/unbound-docker](https://github.com/madnuttah/unbound-docker) project.
Unbound itself is developed by [NLnet Labs](https://nlnetlabs.nl/projects/unbound/).
