# Changelog

## v2.30.6-R2 (2026-07-14)

- No pull requests found for this version bump.
## v2.30.6-R2 (2026-07-14)

### Changed
- Added Node ABI detection to install the correct better-sqlite build
- Simplified install process
- Removed leftover gcompat package
- Removed option for manual secret key input

## v2.30.6-R1 (2026-07-13)

### Changed
- Removed `npm`/`pnpm` from the final image, reducing image size by ~90MB
- Added `LOG_FORMAT=text` to restore human-readable logs

### Bug Fixes
- Fixed a startup crash by replacing the glibc-compiled `better-sqlite3` with a musl build

## v2.30.6

## [2.30.6](https://github.com/Viren070/AIOStreams/compare/v2.30.5...v2.30.6) (2026-07-05)


### Bug Fixes

* **builtins/easynews:** accept numeric dlFarm in search response schema ([#1054](https://github.com/Viren070/AIOStreams/issues/1054)) ([e640f63](https://github.com/Viren070/AIOStreams/commit/e640f636d23a0c3ab8a426d0305563c9a198b370))
* **builtins/torbox-search:** adjust error parsing ([64aace5](https://github.com/Viren070/AIOStreams/commit/64aace5ea8c9e84e58e8d8a195722296a9959603))
* **presets/baguettio:** add config for Tr4ker ([#1058](https://github.com/Viren070/AIOStreams/issues/1058)) ([da760e7](https://github.com/Viren070/AIOStreams/commit/da760e79976b1e7e9d2d4eec8c08eb361ea391eb))


## v2.30.5

## [2.30.5](https://github.com/Viren070/AIOStreams/compare/v2.30.4...v2.30.5) (2026-06-29)


### Bug Fixes

* **builtins:** guard detached search-metadata promise against unhandled rejection ([8a1816b](https://github.com/Viren070/AIOStreams/commit/8a1816b55e515df1238f176be276bb6f948c8228))


## v2.30.4

## [2.30.4](https://github.com/Viren070/AIOStreams/compare/v2.30.3...v2.30.4) (2026-06-28)


### Features

* **anime-database:** refactor, add new source, fix fribbs parsing ([#1026](https://github.com/Viren070/AIOStreams/issues/1026)) ([66453b5](https://github.com/Viren070/AIOStreams/commit/66453b5b2e14b7507640089fb00861701cac5ff0))
* **sel:** enable `ceil`, `floor`, `round`, and `trunc` operators/functions ([7cacd75](https://github.com/Viren070/AIOStreams/commit/7cacd753f3a81f48770a51d7fa32d6d279756aef))


### Bug Fixes

* **builtins/newznab:** read indexer field for davex ([#973](https://github.com/Viren070/AIOStreams/issues/973)) ([c886903](https://github.com/Viren070/AIOStreams/commit/c88690307fb9c21ab7ccd34fc79106b5637b866c))
* **presets/mediafusion:** update parser and config ([#1027](https://github.com/Viren070/AIOStreams/issues/1027)) ([4894cde](https://github.com/Viren070/AIOStreams/commit/4894cde55202f648d87ba8e006a634cddc5c3f11))
* **presets/newznab:** correct mojibake-encoded emojis ([#1039](https://github.com/Viren070/AIOStreams/issues/1039)) ([ae21b76](https://github.com/Viren070/AIOStreams/commit/ae21b76194c40e883bcd75a6ed806a3a33180859))
* **server:** return 404 for non-existent SPA routes ([#1015](https://github.com/Viren070/AIOStreams/issues/1015)) ([d84553e](https://github.com/Viren070/AIOStreams/commit/d84553e29609873cb9bf45f1e3e3f5cd4a89bf73))
* **server:** return api error response for missing meta ([5d1ae75](https://github.com/Viren070/AIOStreams/commit/5d1ae75100d9dfecfae70f0d059d71a1dd1cf4c6))


## v2.30.3

## [2.30.3](https://github.com/Viren070/AIOStreams/compare/v2.30.2...v2.30.3) (2026-06-11)


### Features

* **deduplicator:** add tiebreakers configuration ([5832f46](https://github.com/Viren070/AIOStreams/commit/5832f467d0dc22de9204cdef4eeeec52f0bdf670))
* **poster/openposterdb:** support custom query parameters ([#994](https://github.com/Viren070/AIOStreams/issues/994)) ([4ee7fe8](https://github.com/Viren070/AIOStreams/commit/4ee7fe86ac045dc22a03cd707fe87e8a7901be8b))


### Bug Fixes

* prefer tvdb over trakt for season number ([ff1ae0c](https://github.com/Viren070/AIOStreams/commit/ff1ae0c892a8ad8aa5e0ce0e06ce0124dbf18a6c))
* **presets/mediafusion:** include additional parameters in cache key ([41597e1](https://github.com/Viren070/AIOStreams/commit/41597e1706aaae2f316292892846b775fe00f385)), closes [#1012](https://github.com/Viren070/AIOStreams/issues/1012)
* **presets/meteor:** parse usenet indexer correctly ([376a013](https://github.com/Viren070/AIOStreams/commit/376a0138033f2b6c65592d354917b31c74741b9c))


## v2.30.2

## [2.30.2](https://github.com/Viren070/AIOStreams/compare/v2.30.1...v2.30.2) (2026-05-25)


### Features

* remove fun options ([44463c3](https://github.com/Viren070/AIOStreams/commit/44463c360a7f05cadf3fd17b2d8a2e876c0bdd4f))


### Bug Fixes

* **analytics:** use ON CONFLICT in daily rollup upsert ([6ae4bea](https://github.com/Viren070/AIOStreams/commit/6ae4bead38383ffca5e0ee6bc6e6bc630acb9969))
* dont apply non imdb when episode is already absolute ([222d05a](https://github.com/Viren070/AIOStreams/commit/222d05ae73f458f5be1a3551c854f5ee39eda242))
* make RegexAccess/SelAccess cleanup safe to call before init ([#980](https://github.com/Viren070/AIOStreams/issues/980)) ([a63c34e](https://github.com/Viren070/AIOStreams/commit/a63c34efe01ee92325c3219d478882e0eaf943cf))
* **presets/mediafusion:** override cache key via wrapper APi ([ff8edcc](https://github.com/Viren070/AIOStreams/commit/ff8edcc894eed2c4b082c1afcd534e3d3f58332b))
* **presets/stremthru-torz:** bring back overriden stream parser ([#978](https://github.com/Viren070/AIOStreams/issues/978)) ([a210fac](https://github.com/Viren070/AIOStreams/commit/a210fac05b86963c70d078b6a4b31b83ca286151))
* **presets/torbox:** mark as deprecated ([4ea7aa5](https://github.com/Viren070/AIOStreams/commit/4ea7aa5e0a7798a6eb427d533933657ce9af8dd3))


## v2.30.1

## [2.30.1](https://github.com/Viren070/AIOStreams/compare/v2.30.0...v2.30.1) (2026-05-24)


### Bug Fixes

* **chilllink:** pass streams parameter to toFormatterContext ([#974](https://github.com/Viren070/AIOStreams/issues/974)) ([c661ee6](https://github.com/Viren070/AIOStreams/commit/c661ee6f9e3b4adadeac836db9f5e21a9b9383b3))
* **db:** use pg_advisory_xact_lock to prevent migration lock leak ([#976](https://github.com/Viren070/AIOStreams/issues/976)) ([f0eacdc](https://github.com/Viren070/AIOStreams/commit/f0eacdcbbb4c7e6a81442042e795434e72ee36f3)), closes [#975](https://github.com/Viren070/AIOStreams/issues/975)
* **frontend/dashboard:** fix import/export icons ([#972](https://github.com/Viren070/AIOStreams/issues/972)) ([7d3ec1d](https://github.com/Viren070/AIOStreams/commit/7d3ec1d8fa44031f357a196b454ab0830d4f6f49))
* nullify any input kind if allows null and value is empty string ([d98b2e7](https://github.com/Viren070/AIOStreams/commit/d98b2e7164e23f96614a3006eea8517d4ebacf37))
* pass min value through to KeyValueListField ([d98b2e7](https://github.com/Viren070/AIOStreams/commit/d98b2e7164e23f96614a3006eea8517d4ebacf37))
* **server:** add not found handler for api router ([f645677](https://github.com/Viren070/AIOStreams/commit/f645677b562b9cf18493512d454777663c4a9b1d))


## v2.30.0

## [2.30.0](https://github.com/Viren070/AIOStreams/compare/v2.29.6...v2.30.0) (2026-05-22)


### ⚠ BREAKING CHANGES

* remove deprecated service specific default/forced credential env vars
* remove deprecated addon specific host/proxy/protocol rewrite env vars
* remove deprecated proxy URL port/protocol/host rewrite env vars
* deprecate `ADDON_PASSWORD` in favour of using `AIOSTREAMS_AUTH` + `AIOSTREAMS_AUTH_REQUIRED` for both dashboard and config access control
* add [v2.30 migration guide](https://docs.aiostreams.viren070.me/migrations/v2.30/) for breaking changes
* **api/user:** switch to basic auth

### Features

* add `AIOSTREAMS_AUTH_PROXY` ([684ac80](https://github.com/Viren070/AIOStreams/commit/684ac8022b08472b13c2737ca63fab71309f4252))
* add `VC-1` encode ([832072b](https://github.com/Viren070/AIOStreams/commit/832072b9100fdf5ad97dc5b34dfb407aaf8dba8f)), closes [#960](https://github.com/Viren070/AIOStreams/issues/960)
* add admin dashboard with analytics, logs, system info, users, proxy, tasks, cache, and settings pages ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* add transform API to settings store ([9be1928](https://github.com/Viren070/AIOStreams/commit/9be1928692d30b75e580856292d17fea8de6a43c))
* add user-specific addon statistics ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* **api/user:** switch to basic auth ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* **dashboard/settings:** add dropdown menu with import. export, reset, import from env actions ([7a67b93](https://github.com/Viren070/AIOStreams/commit/7a67b93657d03e499bf4870e86516794bcd00c8a))
* **dashboard:** add user details view to dashboard, format numbers ([a8bcd2b](https://github.com/Viren070/AIOStreams/commit/a8bcd2b8d4a35a6a215a5877c7b88db3c8a75c8e))
* deprecate `ADDON_PASSWORD` in favour of using `AIOSTREAMS_AUTH` + `AIOSTREAMS_AUTH_REQUIRED` for both dashboard and config access control ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* **frontend:** add `right` to swipeDirections for toasts ([687a05c](https://github.com/Viren070/AIOStreams/commit/687a05ce51fec7c881132e3a85f8f876b3612d49))
* **frontend:** show dirty alert as bottom style toast on mobile ([180b8f9](https://github.com/Viren070/AIOStreams/commit/180b8f9952ce164fea75188eb93694d573b8b852))
* **frontend:** switch to tanstack router + rspack/rsbuild for improved performance ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* remove deprecated addon specific host/proxy/protocol rewrite env vars ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* remove deprecated proxy URL port/protocol/host rewrite env vars ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* remove deprecated service specific default/forced credential env vars ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* rewrite database layer with migrations. ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* use cleaner, structured logging format, recommended to set `LOG_FORMAT=json`. ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))


### Bug Fixes

* add * to character class for user agent map ([7273135](https://github.com/Viren070/AIOStreams/commit/7273135a4f984eb76f1b96b8bf7d7b43d3325035))
* correct key ([3188f9e](https://github.com/Viren070/AIOStreams/commit/3188f9e012e7c6a447cc1291da7482f8bb474511))
* detect string | array&lt;string&gt; as list kind ([c3d4604](https://github.com/Viren070/AIOStreams/commit/c3d4604148c67599f5487227a546c6ad2712577e))
* dont send access key in user api response ([173609b](https://github.com/Viren070/AIOStreams/commit/173609b75cb7750ac9c299c2644c8f2ed9df4736))
* **frontend:** add note to use env var on login page ([32a6556](https://github.com/Viren070/AIOStreams/commit/32a6556c7e637b27f03594baf6a3e2f824fd548f))
* **frontend:** fix layout shifting on dirty alert ([180b8f9](https://github.com/Viren070/AIOStreams/commit/180b8f9952ce164fea75188eb93694d573b8b852))
* **frontend:** ui issues ([9fc73b3](https://github.com/Viren070/AIOStreams/commit/9fc73b3856affa4fc314672a69264c8f93034dbf))
* handle non admin in routes ([6d129ef](https://github.com/Viren070/AIOStreams/commit/6d129ef92fd7dccac370cb1284183694a6b512e9))
* inject access key in right place ([153cdc5](https://github.com/Viren070/AIOStreams/commit/153cdc5ce9e0af390647056d82ab1ba994545a82))
* migrate accessToken to accessKey ([adfbcaa](https://github.com/Viren070/AIOStreams/commit/adfbcaabed1edfa4102d778c4648397cf2dad01f))
* only apply status defaults once ([87209fd](https://github.com/Viren070/AIOStreams/commit/87209fd6117cd3a121916d60895f8e37f2f7af7f))
* **presets/custom:** allow selecting none for pin position ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))
* short circuit on unequal length ([88a5d08](https://github.com/Viren070/AIOStreams/commit/88a5d083e4c655e71190021d34c7c05320ecb44d))
* show error toast if non admin user attempts login to dashboard ([520dadd](https://github.com/Viren070/AIOStreams/commit/520dadd114cab16346f941ecd35a412afdd474ef))
* support literal \n in serviceCredentialsMap ([78e492e](https://github.com/Viren070/AIOStreams/commit/78e492e3a568c90b40ea5e8fcb7359818beed037))
* support multi addon password in migration ([7c937e8](https://github.com/Viren070/AIOStreams/commit/7c937e81afe1d5d1294749ae091fdef1ba731df2))
* unwrap union options before classifying ([6cd5ad7](https://github.com/Viren070/AIOStreams/commit/6cd5ad7022c44f675fa059dba3be37db8c0c14ac))
* use commaSeparated helper for prowlarr indexers env var and disabled stream types ([e75e82a](https://github.com/Viren070/AIOStreams/commit/e75e82aff8710d9a976ce323c8c8c05065679ed4))
* use task manager for initial runs too ([8c4680f](https://github.com/Viren070/AIOStreams/commit/8c4680f8a62ea79dbb5b6bea7d50379252a373f7))


### Documentation

* add [v2.30 migration guide](https://docs.aiostreams.viren070.me/migrations/v2.30/) for breaking changes ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))


### Miscellaneous Chores

* **Dockerfile:** update frontend output location ([1a9892b](https://github.com/Viren070/AIOStreams/commit/1a9892bb42c8f990a93d5d79dfbf3ea862ab91ca))


## v2.29.6

## [2.29.6](https://github.com/Viren070/AIOStreams/compare/v2.29.5...v2.29.6) (2026-05-14)


### Features

* **sel:** add keyword() stream function ([#942](https://github.com/Viren070/AIOStreams/issues/942)) ([6e73c52](https://github.com/Viren070/AIOStreams/commit/6e73c5240107c43c87546a80a4cd794be689b828))


### Bug Fixes

* **builtins/torrentgalaxy:** use different domain by default ([#940](https://github.com/Viren070/AIOStreams/issues/940)) ([d243cbe](https://github.com/Viren070/AIOStreams/commit/d243cbe73d55457bf80319b7f865c7b97684e04c))
* **core/nab:** redact apikey query param in INFO/DEBUG logs ([#947](https://github.com/Viren070/AIOStreams/issues/947)) ([1c142de](https://github.com/Viren070/AIOStreams/commit/1c142de0ec3377321bf006506600af3669bf920e))
* load subsection sub-option defaults ([#944](https://github.com/Viren070/AIOStreams/issues/944)) ([9d0a2fb](https://github.com/Viren070/AIOStreams/commit/9d0a2fb61e1d0890004c2cb9a571e06552718d02))
* **presets/newznab:** set appropriate fallbacks for singleIp and showUnknown options ([9d0a2fb](https://github.com/Viren070/AIOStreams/commit/9d0a2fb61e1d0890004c2cb9a571e06552718d02))


## v2.29.5

## [2.29.5](https://github.com/Viren070/AIOStreams/compare/v2.29.4...v2.29.5) (2026-05-09)


### Bug Fixes

* **parser/regex:** fix false negatives with HDR ([1c17097](https://github.com/Viren070/AIOStreams/commit/1c17097c3dc8dad879c56a7e3364475433bd3475)), closes [#925](https://github.com/Viren070/AIOStreams/issues/925)


## v2.29.4

## [2.29.4](https://github.com/Viren070/AIOStreams/compare/v2.29.3...v2.29.4) (2026-05-07)


### Bug Fixes

* **precomputer:** persist ranked expression mutations across iterations ([07fc9de](https://github.com/Viren070/AIOStreams/commit/07fc9deb28ed49c063ddb50829d32e8d61299084))


## v2.29.2

## [2.29.2](https://github.com/Viren070/AIOStreams/compare/v2.29.1...v2.29.2) (2026-05-03)


### Bug Fixes

* fix hashNzbUrl for newznab api t=get ([e659578](https://github.com/Viren070/AIOStreams/commit/e6595784ded71d3b5e23819e90f196aec63846ec))


## v2.29.0

## [2.29.0](https://github.com/Viren070/AIOStreams/compare/v2.28.0...v2.29.0) (2026-05-02)


### Features

* add branding section to parent/child merge strategies ([cfaefb3](https://github.com/Viren070/AIOStreams/commit/cfaefb37d326c0b82dec47b00fb812c8a9cdb0d0))
* add per field overrides to parent/child configs ([cfaefb3](https://github.com/Viren070/AIOStreams/commit/cfaefb37d326c0b82dec47b00fb812c8a9cdb0d0))
* add Portuguese (Brazil) to languages ([573cb23](https://github.com/Viren070/AIOStreams/commit/573cb233972de141b62fec4540954b884f61e68b)), closes [#906](https://github.com/Viren070/AIOStreams/issues/906)
* **frontend:** add command palette with search ([35eb545](https://github.com/Viren070/AIOStreams/commit/35eb545be538c60ad07f3d0631439a23033f4c11))
* **presets/nekoBt:** add option to leave auto title tags in filename ([b4538bc](https://github.com/Viren070/AIOStreams/commit/b4538bc073bdb709002001ec16e6a96b5d387994))


### Bug Fixes

* **frontend:** add missing IDs  to builtin-settings page for search bar ([69536e5](https://github.com/Viren070/AIOStreams/commit/69536e57078ba8a7cfe56be6c19dcde7022ce3ba))
* **frontend:** update mode toggle quick action text ([44f9821](https://github.com/Viren070/AIOStreams/commit/44f9821ad3204dca35b7ff581370ffcb88e0f490))
* **media-info:** use title field to narrow down regional variants ([2fef9d3](https://github.com/Viren070/AIOStreams/commit/2fef9d3e20f969ea13a131fbe5df7cf4ff2c7971))
* merge parent config before validation on save/create/catalog refresh ([c8b9f1c](https://github.com/Viren070/AIOStreams/commit/c8b9f1cb796e8abfb0f0616700e93fde19b6c659)), closes [#908](https://github.com/Viren070/AIOStreams/issues/908)
* **presets/mediafusion:** update config ([9a571fe](https://github.com/Viren070/AIOStreams/commit/9a571fe15ac61216744655fc462ace96ca71fb8a))
* **presets/nekoBt:** fix lang tag parsing and handle missing dash ([3a72a24](https://github.com/Viren070/AIOStreams/commit/3a72a248fd91b5d3cf8b7fe28c6c8bc18a9269f8))
* **presets/yastream:** fix yastream catalog id for movie ([#912](https://github.com/Viren070/AIOStreams/issues/912)) ([fb3acf6](https://github.com/Viren070/AIOStreams/commit/fb3acf626dffe2973724b335080695d4269433e2))
* remove notes field from custom source ext manifest ([d598c98](https://github.com/Viren070/AIOStreams/commit/d598c984fd1e641b0db4c171e9c957f1676c47cd))


