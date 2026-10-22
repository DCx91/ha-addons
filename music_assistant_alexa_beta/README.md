# Music Assistant Alexa Skill: Home Assistant App

Run the [Music Assistant Alexa Skill](https://github.com/alams154/music-assistant-alexa-skill-prototype) as a native, supervised Home Assistant app, with no standalone Docker Compose deployment required.

## About

This app packages the Music Assistant Alexa Skill prototype for Home Assistant, giving you:

- **Automatic startup and supervision** through s6-overlay
- **Persistent ASK CLI credentials** across restarts and updates, stored in `/data/.ask`
- **Configuration in the Home Assistant UI**, with no config files to edit by hand
- **Unified logging** in the Home Assistant Supervisor log viewer

The skill is a Flask web service that acts as the endpoint for a custom Alexa skill, letting your Alexa devices control playback on your Music Assistant server.

## Prerequisites

Before installing, make sure you have:

- [Music Assistant](https://music-assistant.io) running in your Home Assistant instance
- An [Amazon Developer account](https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html) with Skill Access Management enabled
- A static IPv4 address
- A publicly reachable HTTPS endpoint pointing at your Home Assistant IP on port 5000 (the default)
- *(Optional)* A second publicly reachable HTTPS endpoint pointing at your Music Assistant IP on port 8097 (the default)
- *(Optional)* A third publicly reachable HTTPS endpoint pointing at your Music Assistant IP on port 8095 (the default)

> **Note:** IPv6-only endpoints will fail when called from Amazon's servers. If you're behind CGNAT, use Cloudflared, Tailscale Funnel, or a similar tunnelling service.

## Installation

1. In Home Assistant, go to **Settings → Apps → App Store**.
2. Open the menu in the top right and select **Repositories**.
3. Paste in this repository's URL and click **Add**.
4. Find **Music Assistant Alexa Skill** in the store and click **Install**.

## Configuration

| Option | Required | Default | Description |
|---|---|---|---|
| `skill_hostname` | Yes | none | Public HTTPS hostname Alexa uses to reach this app (e.g. `alexa.example.com`). Must be reachable by Amazon. |
| `ma_hostname` | No | none | Public HTTPS hostname of your Music Assistant stream (e.g. `stream.example.com`). Needed for album art and for Alexa devices without a touch screen. |
| `app_username` | Yes | none | Username for the web UI and API basic authentication. |
| `app_password` | No | none | Password for the web UI and API basic authentication. |
| `locale` | Yes | `en-GB` | Skill locale (e.g. `en-US`, `de-DE`). |
| `aws_default_region` | Yes | `eu-west-1` | AWS region used for SMAPI calls. |
| `skill_id` | No | none | Your skill's ID (`amzn1.ask.skill...`). Shown once setup has run. |
| `ma_api_url` | No | none | Music Assistant web server hostname (e.g. `ma.example.com`). Required for voice-controlled Next/Previous. |
| `ma_api_token` | No | none | Long-lived token created through Music Assistant's own auth flow. Required alongside `ma_api_url`. |
| `skip_url_validation` | No | `false` | Skip the server-side HEAD/GET validation of the rewritten stream URL before it is sent to the Echo. |
| `enable_apl` | No | `false` | Enable rich APL rendering (cover art, title, on-screen playback controls) on Echo Show and other APL-capable devices. |
| `debug` | No | `false` | Enable Flask debug mode. |

## Setup

Once the app is running and your reverse proxy is configured:

1. Open the app's web UI at `http://homeassistant.local:5000/setup`, or click **Open Web UI**.
2. Click **Start Setup**. The app creates the Alexa skill for you.
3. Follow progress in the setup log shown on the page.
4. When it finishes, open `/status` and confirm everything is green.

### Persistent ASK Credentials

ASK CLI credentials live in `/data/.ask` and survive app restarts and updates. To re-authenticate, delete the contents of that directory and run setup again.

## Reverse Proxy

Alexa requires a valid HTTPS endpoint. Your `skill_hostname` must resolve to port 443 externally and proxy through to this app's port internally.

Example for Nginx Proxy Manager:

| Field | Value |
|---|---|
| Scheme | `http` |
| Forward Hostname | `homeassistant.local` |
| Forward Port | `5000` |

For album art and support for non-APL devices (those without a touch screen), `ma_hostname` must likewise proxy to Music Assistant's stream port (`8097` by default).

## Voice Controls

Voice-controlled next/previous track requires `ma_api_url` to be a publicly reachable HTTPS address pointing at Music Assistant's web server port (`8095` by default). You can enable the web server under **Music Assistant → Settings → System → Webserver**.

Then:

1. Play music on an Alexa device.
2. Open `http://homeassistant.local:5000/devices`.
3. Under `MA player_id`, enter the device's name exactly as it appears in Music Assistant, then click **Save**.

## Music Assistant Configuration

In Music Assistant, configure the Alexa provider with:

- **API URL:** `https://your-skill-hostname`
- **API Username:** the value of `app_username`
- **API Password:** the value of `app_password`

## Ports

| Port | Description |
|---|---|
| `5000/tcp` | Flask web UI, Alexa skill endpoint, and Music Assistant API |

## Known Limitations

- Alexa groups (including stereo pairs) are not supported.
- State reporting from Music Assistant to the Alexa app may not always match reality.
- Album art and track info only update when a new stream URL is issued, so they may occasionally be out of date.
- For the full list, see the upstream [LIMITATIONS.md](https://github.com/alams154/music-assistant-alexa-skill-prototype/blob/master/LIMITATIONS.md).

## Credits

The Alexa skill prototype is developed and maintained by [@alams154](https://github.com/alams154). This app packages that work for Home Assistant Supervisor.
