# Unbound DNS — Home Assistant App

A validating, recursive, caching DNS resolver for your home network.

---

## What is Unbound?

Unbound is a high-performance DNS resolver developed by NLnet Labs. Rather
than forwarding your queries to a third-party DNS service (like 8.8.8.8 or
1.1.1.1), Unbound resolves domains itself by walking the DNS hierarchy: root
servers, then the TLD servers, then the domain's own name servers.

What this means for privacy:

- **No single third party sees all your queries.** A forwarding resolver
  sees everything you look up; here, each server in the chain only sees the
  part it is responsible for.
- **It is not invisible.** The authoritative servers still receive queries
  from your IP address, and your ISP can still see the traffic. Unbound
  sends only as much of the name as each server needs (QNAME minimisation),
  but it does not hide your IP address.

Unbound also validates DNSSEC signatures, so forged answers for signed domains
are rejected with `SERVFAIL` rather than passed on to your devices.

---

## Installation

1. Add this repository to Home Assistant:
   **Settings → Apps → Install App → ⋮ → Repositories**
   Paste in the URL of this repo.

2. Find **Unbound DNS** in the store and click **Install**.

3. Adjust the configuration options to suit your network, then click **Start**.

---

## Configuration

| Option | Default | Description |
|---|---|---|
| `unbound_verbosity` | `1` | Logging detail, 0–5 (see below) |
| `do_ipv6` | `false` | Allow Unbound to use IPv6 when talking to upstream name servers (see [IPv6](#ipv6)) |
| `num_threads` | `1` | Worker threads. Capped automatically to the number of CPU cores |
| `no_persist_cache` | `true` | When `true`, the cache starts empty after every restart. Set to `false` to save the cache on stop and reload it on start |
| `cache_min_ttl` | `0` | Minimum time (seconds) a record stays cached, even if its TTL is shorter |
| `cache_max_ttl` | `86400` | Maximum time (seconds) a record stays cached, even if its TTL is longer |

Options are written to `conf.d/00-ha-options.conf` on every start, so they
always reflect the UI. See [Editing unbound.conf](#editing-unboundconf) for
what that means if you edit the files yourself.

### Verbosity levels

| Level | Output |
|---|---|
| 0 | Errors only |
| 1 | Operational information (default) |
| 2 | Detailed operational information |
| 3 | Query-level information. Also turns on `log-queries` and `log-replies` |
| 4 | Algorithm-level information |
| 5 | Client identification for cache misses |

Levels 3 and above are noisy and log every domain your devices look up.
Use them for troubleshooting, not as a permanent setting.

---

## Using with Pi-hole or AdGuard Home

Point your filtering DNS at Unbound as its only upstream server.

**AdGuard Home** (Settings → DNS settings → Upstream DNS servers):

```
127.0.0.1:5335
```

**Pi-hole** (Settings → DNS → Custom upstream DNS servers) uses `#` for the
port:

```
127.0.0.1#5335
```

`127.0.0.1` works when Pi-hole or AdGuard Home runs on the Home Assistant host
(host network) and this app publishes its port, as it does by default. If
the other app runs in its own container network instead, use this app's
internal hostname, shown on its Info page, in place of `127.0.0.1`.

Disable any other upstream servers, otherwise some queries will bypass
Unbound.

---

## Testing

From any machine that is allowed to query Unbound (replace `<ha-ip>`):

```
dig @<ha-ip> -p 5335 example.com
```

Check DNSSEC validation:

```
dig @<ha-ip> -p 5335 example.com +dnssec
```

A validated answer has the `ad` (authenticated data) flag in the header. A
domain that deliberately fails validation should be rejected:

```
dig @<ha-ip> -p 5335 dnssec-failed.org
```

That should return `SERVFAIL`. If it returns an address, validation is not
working.

---

## Editing unbound.conf

The main configuration lives at
`/addon_configs/61709215_unbound/unbound.conf`. You can edit it with the
File editor, Studio Code Server or Samba apps.

How it is handled on start:

- **No `unbound.conf` yet:** a default one is generated.
- **`unbound.conf` exists and passes `unbound-checkconf`:** it is used
  exactly as you left it. The generated one is not touched.
- **`unbound.conf` exists but fails `unbound-checkconf`:** it is
  **overwritten** with a freshly generated default. Keep a copy of anything
  you want to preserve.

Two things to be aware of:

- **UI options only apply if your file includes `conf.d`.** The generated
  config contains the line `include-toplevel: "/config/conf.d/*.conf"`. If
  you replace `unbound.conf` with your own, keep that line, otherwise the
  options on the Configuration tab (port, threads, TTLs, IPv6, verbosity)
  will silently have no effect.
- **Don't edit `conf.d/00-ha-options.conf`.** It is regenerated from the
  UI on every start.

---

## IPv6

`do_ipv6` controls whether Unbound may use IPv6 when it contacts upstream
name servers (the root, TLD and domain servers). It makes no difference to
whether you can resolve IPv6 addresses (AAAA records): those work either way,
carried over IPv4 when `do_ipv6` is off.

When to enable it:

- Your Home Assistant host has working IPv6 connectivity, or Docker is set
  up to NAT IPv6 for containers.

When to leave it off:

- Your network has no IPv6, or it is unreliable. Unbound may try an IPv6
  server, time out, and only then fall back, which shows up as occasional slow
  lookups.

The benefit is modest. Unbound picks servers by measured response time, not
by address family, so IPv6 is rarely noticeably faster. The main gain is
resilience when an IPv4 path to some server is broken.

To check whether Unbound is actually using IPv6, run this in the app's
container after it has been running for a while:

```
unbound-control -c /config/unbound.conf dump_infra
```

IPv6 server entries with low `rtt` values mean it is working. An `rto` near
120000 means Unbound has given up on that server.

---

## Custom Configuration Files

You can place additional `.conf` files in
`/addon_configs/61709215_unbound/conf.d/`. They are included automatically,
letting you add things like:

- `forward-zone` entries for split-horizon DNS
- `local-data` for custom hostnames
- `stub-zone` entries for internal domains

Each file is read at the top level, so start it with `server:` (or another
clause) as usual. Restart the app after changing files.

Example `conf.d/local.conf`:

```
server:
    local-data: "myserver.home. IN A 192.168.1.50"
    local-data-ptr: "192.168.1.50 myserver.home."
```

### Internal domains that resolve to private IPs

This app enables Unbound's private-address protection, which strips any
answer that points to a private IP (10.x, 172.16–31.x, 192.168.x and so on)
to guard against DNS rebinding. Records you define with `local-data` are not
affected. Answers fetched from a `forward-zone` or `stub-zone` for an
internal domain are, and the lookup will appear to fail. Mark such domains as
private:

```
server:
    private-domain: "home.example.com"

forward-zone:
    name: "home.example.com."
    forward-addr: 192.168.1.1
```

---

## Cache persistence

Set `no_persist_cache` to `false` to keep the cache across restarts. On stop
the cache is saved to `/addon_configs/61709215_unbound/unbound_cache.dump`,
and on the next start it is loaded once Unbound is ready. If the file is
missing or can't be loaded, the app logs a warning and starts with an empty
cache.

---

## Ports

| Port | Protocol | Description |
|---|---|---|
| 5335 | UDP | DNS queries |
| 5335 | TCP | DNS over TCP / large responses |

The port is fixed inside the container. To change which port is exposed on the
host, change the mapping on the app's **Network** section of the Configuration
tab.

---

## Security and resource use

- **Access control:** by default Unbound only answers queries from loopback
  and private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`,
  `127.0.0.0/8`). Everything else is refused. Do not forward port 5335 from
  your router to this app: an open resolver can be abused for DDoS
  amplification.
- **Root hints** are refreshed from InterNIC if they are older than seven
  days. The root zone is also fetched locally so root lookups don't have to
  leave the network each time.
- **Memory:** the defaults allow up to 256 MB for the record cache and
  128 MB for the message cache, plus overhead. On a small device, lower these
  in a `conf.d` file (`rrset-cache-size` and `msg-cache-size`).

---

## Troubleshooting

| Symptom | What to check |
|---|---|
| App won't start | The log shows the `unbound-checkconf` error. Common cause is a custom `unbound.conf` with a typo |
| Options in the UI have no effect | Your `unbound.conf` is missing the `include-toplevel` line (see above) |
| Queries are refused | The client's IP is outside the allowed ranges, or a VPN or NAT is changing its source address |
| Internal names fail to resolve | See *Internal domains that resolve to private IPs* |
| Slow occasional lookups with `do_ipv6` on | IPv6 is unreliable on your network; turn it off |
| `dnssec-failed.org` returns an address | Validation isn't working: check the system clock and the root trust anchor |

---

## Credits

Unbound is developed by [NLnet Labs](https://nlnetlabs.nl/projects/unbound/).
