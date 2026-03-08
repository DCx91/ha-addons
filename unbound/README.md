# 🔒 Unbound DNS — Home Assistant App

> A validating, recursive, and caching DNS resolver for your home network.  
> No third party. No tracking. Just fast, private DNS.

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Add--on-41BDF5?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![Alpine Linux](https://img.shields.io/badge/Alpine%20Linux-3.22-0D597F?logo=alpine-linux&logoColor=white)](https://alpinelinux.org/)
[![Unbound](https://img.shields.io/badge/Unbound-1.23.1-00897B)](https://nlnetlabs.nl/projects/unbound/about/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What is Unbound?

Instead of forwarding your DNS queries to Google (8.8.8.8) or Cloudflare (1.1.1.1), **Unbound resolves domains recursively** — walking the DNS hierarchy itself, starting from the root nameservers. No single upstream provider ever sees your full query history.

It also **validates DNSSEC signatures**, protecting against DNS spoofing and cache poisoning attacks.

### Why run it on Home Assistant?

- 🏠 **Always on** — runs alongside your existing HA setup, no extra hardware needed
- ⚡ **Fast** — responses cached locally, shared across every device on your network
- 🔏 **Private** — your DNS queries never leave your network
- 🛡️ **Secure** — full DNSSEC validation out of the box
- 🧩 **Pi-hole / AdGuard compatible** — use as upstream DNS for your ad blocker

---

## Installation

**Option 1 — One-click:**

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDCx91%2Fha-addons)

**Option 2 — Manual:**

Go to **Settings → Apps → App Store → ⋮ → Repositories** and add:

```
https://github.com/DCx91/ha-addons
```

Then find **Unbound DNS** in the store and click **Install**.

---

## Using with AdGuard Home / Pi-hole

Set your upstream DNS server to:

```
127.0.0.1:5335
```

This routes all queries through Unbound for fully private, recursive resolution — AdGuard/Pi-hole handles blocking, Unbound handles resolution.

---

## Check health

Using SSH:

```
docker ps | grep "unbound"
```

---

## Credits

Adapted from [madnuttah/unbound-docker](https://github.com/madnuttah/unbound-docker).  
Unbound is developed by [NLnet Labs](https://nlnetlabs.nl/projects/unbound/about/).
