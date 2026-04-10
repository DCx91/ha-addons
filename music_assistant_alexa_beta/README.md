# Music Assistant Alexa Skill — Home Assistant App

>A Home Assistant app that runs the [Music Assistant Alexa Skill](https://github.com/alams154/music-assistant-alexa-skill-prototype) as a native supervised app, replacing the standalone Docker Compose deployment.

## About

This app wraps the Music Assistant Alexa Skill prototype in a Home Assistant app, providing:

- Automatic startup and supervision via s6-overlay
- Persistent ASK CLI credentials across restarts via `/data/.ask`
- Configuration through the Home Assistant app UI
- Log output directly in the Home Assistant Supervisor log viewer

The skill itself is a Flask web service that acts as an endpoint for a custom Alexa skill, allowing Alexa devices to control playback on your Music Assistant server.

## Prerequisites

Before installing this app you will need:

- [Music Assistant](https://music-assistant.io) running in your Home Assistant instance
- An [Amazon Developer account](https://developer.amazon.com/en-US/docs/alexa/ask-overviews/create-developer-account.html) with Skill Access Management enabled
- A publicly reachable HTTPS endpoint pointing at this app's port (e.g. via NGINX Proxy Manager or Cloudflare)
- (Recommended) A second publicly reachable HTTPS endpoint pointing to the Music Assistant's stream port (Default: 8097)

## Installation

1. Navigate to **Settings → apps → app Store** in Home Assistant
2. Click the menu in the top right and select **Repositories**
3. Add this repository URL and click **Add**
4. Find **Music Assistant Alexa Skill** in the store and click **Install**

## Configuration

| Option | Required | Default | Description |
|---|---|---|---|
| `SKILL_HOSTNAME` | ✅ | — | Public HTTPS hostname Alexa will use to reach this app (e.g. `alexa.example.com`). Must be reachable by Amazon. |
| `MA_HOSTNAME` | 🟡 | — | Public HTTPS hostname of your Music Assistant stream. Required if your Alexa devices don't support APL, or if you want album art. |
| `APP_USERNAME` | ✅ | `ma-alexa` | Username for the web UI and API basic authentication. |
| `APP_PASSWORD` | ❌ | — | Password for the web UI and API basic authentication. |
| `PORT` | ✅ | `5000` | Port the Flask app listens on. Update your reverse proxy to match if changed. |
| `LOCALE` | ✅ | `en-GB` | Skill locale (e.g. `en-US`, `de-DE`). |
| `AWS_DEFAULT_REGION` | ✅ | `eu-west-1` | AWS region for SMAPI calls. |

## Setup

Once the app is running and your reverse proxy is configured:

1. Open the app web UI at `http://homeassistant:5000/setup` (or via the **Open Web UI** button)
2. Click **Start Setup** — the app will create the Alexa skill automatically
3. Monitor progress in the setup logs shown on the page
4. Once complete, open the status page at `/status` to verify everything is green

### Persistent ASK Credentials

ASK CLI credentials are stored in `/data/.ask` and persist across app restarts and updates. If you need to re-authenticate, delete the contents of that directory and run setup again.

## Reverse Proxy

Alexa requires a valid HTTPS endpoint. Your `SKILL_HOSTNAME` must resolve to port 443 externally and proxy through to this app's port internally.

Example NGINX Proxy Manager custom location:

| Field | Value |
|---|---|
| Location | `/` |
| Scheme | `http` |
| Forward Hostname | `homeassistant` |
| Forward Port | `5000` |

If you also want album art and non-APL device support (i.e. everything except Echo Show devices), your `MA_HOSTNAME` must similarly proxy to Music Assistant's stream port (`8097` by default).

## Music Assistant Configuration

In Music Assistant, configure the Alexa provider with:

- **API URL**: `https://your-skill-hostname/alexa`
- **API Username**: the value of `APP_USERNAME`
- **API Password**: the value of `APP_PASSWORD`

## Ports

| Port | Description |
|---|---|
| `5000/tcp` | Flask web UI, Alexa skill endpoint, and Music Assistant API |

## Known Limitations

- Alexa groups (including stereo pairs) are not supported
- State reporting from Music Assistant to the Alexa app may not always reflect reality
- See the upstream repository's [LIMITATIONS.md](https://github.com/alams154/music-assistant-alexa-skill-prototype/blob/master/LIMITATIONS.md) for the full list

## Credits

The Alexa skill prototype is developed and maintained by [@alams154](https://github.com/alams154). This app packages that work for Home Assistant Supervisor.
