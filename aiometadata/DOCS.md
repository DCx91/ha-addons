# AIOMetadata

AIOMetadata is a metadata service for retrieving movie and TV information, artwork, posters and ratings from a variety of external metadata providers.

This app runs AIOMetadata directly within Home Assistant and provides access to its web interface and API.

## Configuration

### Hostname

The public URL used to access AIOMetadata.

For example:

```text
https://metadata.example.com
```

This should be the URL that clients use to connect to the service. If you are using a reverse proxy, enter the externally accessible URL rather than the internal Home Assistant address.
This will be used for the manifest URL that will be installed as an addon to Stremio/Nuvio.

### Admin Key

The password used to access the `/dashboard` administration interface.

If this is left blank, AIOMetadata will generate an administrator key automatically on first startup. The generated key can then be viewed from the app configuration UI.

Keep this key private.

### Verbosity

Controls the amount of information written to the app logs.

Use a higher verbosity level when troubleshooting problems. For normal operation, the default level is recommended.

### TMDb API Key

An API key for [The Movie Database (TMDb)](https://www.themoviedb.org/).

AIOMetadata uses TMDb to retrieve movie and TV metadata.

A TMDb API key is recommended for normal operation.

### TVDb API Key

A TheTVDB API v4 key.

This can be used by AIOMetadata to retrieve additional movie and TV metadata.

### FanArt API Key

An API key for [Fanart.tv](https://fanart.tv/).

Fanart.tv provides high-quality artwork such as:

- Movie and TV backgrounds
- Logos
- Clear art
- Character artwork
- Additional promotional artwork

The key is optional, but is recommended if you want access to Fanart.tv artwork.

### RPDb API Key

An API key for the Rating Poster Database (RPDb).

RPDb provides posters and other artwork containing ratings and additional information.

The key is optional.

### Single User

Optimises AIOMetadata for personal use.

When enabled, features and overhead intended for publicly accessible or multi-user instances are disabled or reduced.

This is recommended when the app is only being used by you or by devices on your own network.

### Cache Posters

Caches downloaded posters, artwork and icons locally.

Enabling this can significantly improve subsequent requests and reduce the number of requests made to external providers.

The cache also reduces repeated downloads of the same artwork.

This is recommended for most installations.

### Cache Warming

A list of user UUIDs to use when performing cache-warming operations.

Up to three UUIDs can be specified.

Cache warming allows commonly requested artwork and metadata to be populated in advance, reducing the delay experienced when content is requested for the first time.

If disabled, cache warming still occurs, but less specifically.

## API Keys

AIOMetadata can use several external metadata providers. API keys are generally optional, but enabling additional providers can increase the amount and variety of metadata and artwork available.

You do not need to configure every provider.

At minimum, configure the providers required by the clients and features you intend to use.

## Accessing AIOMetadata

Once the app has started, use the configured hostname to access AIOMetadata.

The administration dashboard is available at:

```text
https://<your-hostname>/dashboard
```

For example:

```text
https://metadata.example.com/dashboard
```

The dashboard requires the configured **Admin Key**.

## Reverse Proxy

If AIOMetadata is being exposed through a reverse proxy, the `host_name` option should contain the public URL clients use to access the service.

For example:

```text
host_name: https://metadata.example.com
```

The hostname should include the protocol (`https://`) and should not point to an internal Docker or Home Assistant address.

## Troubleshooting

### The app will not start

Check the app logs for configuration or startup errors.

If you have recently changed an API key or another configuration option, restart the app after saving the configuration.

### Metadata or artwork is missing

Check that the relevant provider API key has been configured and that the key is valid.

Increasing the **Verbosity** setting can provide additional information in the logs.

### Requests are slow

Enable **Cache Posters** to avoid repeatedly downloading the same artwork.

If you use cache warming, configure the relevant user UUIDs under **Cache Warming**.

### I have forgotten the Admin Key

If the Admin Key was automatically generated, check the app logs for the generated key.

If you configured the key yourself, update the app configuration with a new key and restart the app.
