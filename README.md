# 🏠 Home Assistant Apps

---

## Apps in this repository

| App | Description |
|--------|-------------|
| [**Unbound DNS**](unbound/README.md) | Validating, recursive, caching DNS resolver with DNSSEC |

---

## Installation

**Option 1 — One-click:**

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FDCx91%2Fha-addons)

**Option 2 — Manual:**

Go to **Settings → Apps → App Store → ⋮ → Repositories** and add:

```
https://github.com/DCx91/ha-addon-unbound
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

## Credits

Adapted from [madnuttah/unbound-docker](https://github.com/madnuttah/unbound-docker).
Unbound is developed by [NLnet Labs](https://nlnetlabs.nl/projects/unbound/about/).
