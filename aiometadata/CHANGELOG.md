# Changelog

## v3.5.1

## [3.5.1](https://github.com/cedya77/aiometadata/compare/v3.5.0...v3.5.1) (2026-10-14)


### Bug Fixes

* **catalogs:** give merged catalogs a poster shape that matches their sources by default ([a46b4b1](https://github.com/cedya77/aiometadata/commit/a46b4b11f8dac827533dae605892390737d4a2c9))
* **jellyfin:** follow Simkl anime into their next season ([5101be6](https://github.com/cedya77/aiometadata/commit/5101be6d339b7cc6a41f9e3a817412752b5cd642))
* **jellyfin:** list watchlisted shows in Upcoming ([73fb676](https://github.com/cedya77/aiometadata/commit/73fb6767186585bcddb53173b2bdabd2e5cd9e5c))
* **jellyfin:** reach the stream addon from apps whose device name is not plain ASCII ([d6f4ea0](https://github.com/cedya77/aiometadata/commit/d6f4ea0e97ff3ad9cf284c93db1d03d4a249d09a))
* **jellyfin:** send anime films in the watchlist and favourites as movies ([600cae1](https://github.com/cedya77/aiometadata/commit/600cae196bb72178323dd3455e9c0b4127dd8c75))
* **jellyfin:** show a watchlist change in Upcoming straight away ([2225074](https://github.com/cedya77/aiometadata/commit/222507491418d160deadf47a1f9f0d4e63869420))


## v3.5.0

## [3.5.0](https://github.com/cedya77/aiometadata/compare/v3.4.1...v3.5.0) (2026-10-13)


### Features

* **anime:** show anime episodes as out on their earliest release or their English dub ([e766d94](https://github.com/cedya77/aiometadata/commit/e766d9425d536a2946d7f384599db8f0e80afcdb))
* **catalogs:** let custom manifest catalogs turn caching off with a TTL of 0 ([a2da87c](https://github.com/cedya77/aiometadata/commit/a2da87c23728ef3c5307f9c8abedd55659691c9e))
* **catalogs:** list the titles favourited on the Jellyfin server as watchlist catalogs, sortable and per user ([e82f00d](https://github.com/cedya77/aiometadata/commit/e82f00d795fa4788aa32212087cbecfbc0be7359))
* **catalogs:** option to keep a custom manifest addon's own art ([8b0a281](https://github.com/cedya77/aiometadata/commit/8b0a2812c731fefb643de8fd861ce7d1266b20ec))
* **collections:** studio logo row in Anime Essentials ([4bdbf99](https://github.com/cedya77/aiometadata/commit/4bdbf995b450e6298f787a37fd9f837eadbb9616))
* **configure:** set the poster shape of selected catalogs in bulk ([7d01bd1](https://github.com/cedya77/aiometadata/commit/7d01bd18f1c75840b8178e54e9ed3397ca97125e))
* **jellyfin:** carry audio and subtitle language lists in the user configuration ([7ad1568](https://github.com/cedya77/aiometadata/commit/7ad1568c462b3b42f12457c024d8fec6ddae2554))
* **jellyfin:** choose whether the Upcoming row lists caught-up shows or everything airing ([6e80683](https://github.com/cedya77/aiometadata/commit/6e8068351d71d3b5fefa9cbf2270ca346d88e5a4))
* **jellyfin:** download movies and episodes through the standard Jellyfin endpoint ([be15058](https://github.com/cedya77/aiometadata/commit/be150589b226a01f7ecfb42cd792f04e875bae56))
* **jellyfin:** keep the server's own watchlist alongside picked tracker shelves ([2ee661b](https://github.com/cedya77/aiometadata/commit/2ee661be0dade57f9a0f02af30194aa153daec49))
* **jellyfin:** option to keep unaired episodes playable ([8026134](https://github.com/cedya77/aiometadata/commit/802613490841bbe400bca91dd41b2b68694dedd1))
* **jellyfin:** pick the order skip marker sources are asked in ([3ab80f8](https://github.com/cedya77/aiometadata/commit/3ab80f805f19dc440580ebb9d3cec3cb25b5b955))
* **jellyfin:** protect a user with a PIN ([93938ed](https://github.com/cedya77/aiometadata/commit/93938edd9f376e12e905602e252df0f7cc1eaccc))
* **jellyfin:** suggest titles as you type through Search/Hints, from LumiereDB ([78f5738](https://github.com/cedya77/aiometadata/commit/78f57383fab1b780b778b42cbd170c711bb6d5c0))
* **jellyfin:** tag collection tiles and rows whose title the builder hides ([76a14ca](https://github.com/cedya77/aiometadata/commit/76a14ca8527bbd3906623561bf5bf9882eddf5ea))
* **jellyfin:** tell the stream addon which app the streams are for ([a6b622c](https://github.com/cedya77/aiometadata/commit/a6b622c528986bfaa0bf1409e8627437f5765b36))
* **mal:** add an Enable Jikan (MAL) setting to turn MAL catalogs, search and metadata off ([8f13e68](https://github.com/cedya77/aiometadata/commit/8f13e683767f82ddd929094401269eb64fd3093f))
* **mal:** offer None in the MAL Genres catalog ([52b1d36](https://github.com/cedya77/aiometadata/commit/52b1d36890e5d9dd4b663cfe1da7d76c8455c4b3))
* **manifest:** accept tags as path segments, so each tagged install has its own URL ([7f0684c](https://github.com/cedya77/aiometadata/commit/7f0684c81958fdadf2acb8fe356535ba2f76a1c1))
* **meta:** choose which country's age rating is shown ([#821](https://github.com/cedya77/aiometadata/issues/821)) ([066572b](https://github.com/cedya77/aiometadata/commit/066572b3b6a1d4247bbf76dc921d1328e3aa156f))
* **publicmetadb:** add public lists by link ([5df1294](https://github.com/cedya77/aiometadata/commit/5df1294425f6f5ee8aeb5f9977e2be47ee29aab1)), closes [#791](https://github.com/cedya77/aiometadata/issues/791)
* **simkl:** count a watch at the same progress as the played threshold ([b6ba7e0](https://github.com/cedya77/aiometadata/commit/b6ba7e0f4548ee15a5cea00e751dd6956a33f8a9))


### Bug Fixes

* add missing timezone alias ([#788](https://github.com/cedya77/aiometadata/issues/788)) ([0f339e1](https://github.com/cedya77/aiometadata/commit/0f339e1d7da7e4fa93c2f748c3cac3d0e5eedf84))
* **anilist:** keep the date each list entry was added ([716cbc1](https://github.com/cedya77/aiometadata/commit/716cbc14d4e2dcf1d5b610456d5d8fb5b30ff0f6))
* **catalogs:** keep a merged catalog's user-specific sources when the export includes them ([329136c](https://github.com/cedya77/aiometadata/commit/329136c074f998e64eef265cdfeca6209a0a1cc9))
* **config:** change a saved configuration only with its password or an owning session ([4dd3e24](https://github.com/cedya77/aiometadata/commit/4dd3e246bba937bca7966ee0a9bcd4bbff3d27a1))
* **dashboard:** count each title once in a configuration's played and in-progress figures ([e1c9cc6](https://github.com/cedya77/aiometadata/commit/e1c9cc6a0934e3cef5221d0cbfe1ad75af200332))
* **dashboard:** count only server errors and rate limits in the error rate, and name the routes behind them ([db20ddc](https://github.com/cedya77/aiometadata/commit/db20ddcaf5900c5631d1650b40a6a5874fcb8e7e))
* **dashboard:** give the dashboard tabs a subtler focus ring ([82e71b4](https://github.com/cedya77/aiometadata/commit/82e71b4a38e021c03915f20b18eb0d310b71eeec))
* **dashboard:** read the error rate over the last 24 hours and today's requests by the viewer's own day ([f589b4a](https://github.com/cedya77/aiometadata/commit/f589b4ad9dd867f40c603eb89a9c399e4d912f95))
* **dashboard:** show Lumiere searches in the Performance tab ([1b36993](https://github.com/cedya77/aiometadata/commit/1b36993558078933ff80a57212935900120bfd64))
* **docker:** pull base images from the Docker Hub mirror on mirror.gcr.io ([5a98a4e](https://github.com/cedya77/aiometadata/commit/5a98a4e3d000b7dbad6fcea3e070d28285470753))
* **id-mappings:** only backfill Wikidata TVDB and TVmaze ids into dins series rows ([#798](https://github.com/cedya77/aiometadata/issues/798)) ([3768817](https://github.com/cedya77/aiometadata/commit/37688179d6e1683831119e188f03a1ecc85bbd3e))
* **jellyfin:** ask MDBList for upcoming episodes only when it is the chosen tracker ([93f5c0d](https://github.com/cedya77/aiometadata/commit/93f5c0db3be2be6f7f86a1a481a63820bf5f10af))
* **jellyfin:** clear a resume point that was cleared on the tracker ([2952dfb](https://github.com/cedya77/aiometadata/commit/2952dfb0008d19383a6cb7a852085e99d046a3ab))
* **jellyfin:** count a collection's titles rather than its catalogs ([39fc52b](https://github.com/cedya77/aiometadata/commit/39fc52b6e5813f90527f99a8bf54bbb11b29345a))
* **jellyfin:** count an episode unmarked here as unwatched in its show's total ([31e92a7](https://github.com/cedya77/aiometadata/commit/31e92a7125f8103134624e7925c9539995d1c906))
* **jellyfin:** date favourites by when they were added ([e121674](https://github.com/cedya77/aiometadata/commit/e121674d34a9ab028c21fb68c0599a98394946c0))
* **jellyfin:** drop the show when an episode or season is disliked ([59c4d36](https://github.com/cedya77/aiometadata/commit/59c4d36a461b77681c0e9d55abb39691321e906d))
* **jellyfin:** give a filmography the configured art and watched marks, a page at a time ([89c415b](https://github.com/cedya77/aiometadata/commit/89c415be4bf3cff7a8b2bbe576fc8a5c817d06f2))
* **jellyfin:** give each search suggestion an artists list, as clients built on the Kotlin SDK require ([eaafb06](https://github.com/cedya77/aiometadata/commit/eaafb06fc90e04a23b1774c09f7a2055ae8c2d4f))
* **jellyfin:** give similar titles the configured posters and art ([9df7899](https://github.com/cedya77/aiometadata/commit/9df789940a2195737ad220cae9c470b81dfab8f8))
* **jellyfin:** index started shows a list finds unindexed ([cdc53a6](https://github.com/cedya77/aiometadata/commit/cdc53a6c4a920bcd90a8851e070c435f6ddd42f2))
* **jellyfin:** keep a trailer's YouTube link to the video's own id ([e556163](https://github.com/cedya77/aiometadata/commit/e55616335e70a18d444023ae5825f0e80e7d6eca))
* **jellyfin:** keep an aired episode in Upcoming until Next Up lists it ([fe17561](https://github.com/cedya77/aiometadata/commit/fe1756173cdd2583866836c9ebc9a549480583f3))
* **jellyfin:** keep media source ids in their bare form ([7562a6b](https://github.com/cedya77/aiometadata/commit/7562a6b2b1d516826743fa62583f507d34c7e712))
* **jellyfin:** keep titles that read as unwatched out of the activity history ([153f2fb](https://github.com/cedya77/aiometadata/commit/153f2fb0609f10cb1d719f564c3cab124c7f6e84))
* **jellyfin:** list a person's whole filmography when no limit is asked ([265c95f](https://github.com/cedya77/aiometadata/commit/265c95f8591cc5b916140cb64645db7aec53b7df))
* **jellyfin:** list a title's fetched streams when it is opened again ([03c94df](https://github.com/cedya77/aiometadata/commit/03c94dff31d73c1e9cf6c6ac964cee873f301216))
* **jellyfin:** list each watch once in the activity history ([e1c9cc6](https://github.com/cedya77/aiometadata/commit/e1c9cc6a0934e3cef5221d0cbfe1ad75af200332))
* **jellyfin:** list unreleased movies from every watchlist in Upcoming ([d4fa4fe](https://github.com/cedya77/aiometadata/commit/d4fa4fe42728d2b1e02889f719441849e4175919))
* **jellyfin:** mark watched titles in similar items ([e743ebd](https://github.com/cedya77/aiometadata/commit/e743ebd01c055744a598af61626ab29a2d11e45a))
* **jellyfin:** open a title at once when its versions are resolved on open ([5449a11](https://github.com/cedya77/aiometadata/commit/5449a118dac2905c50bc60393cdc280bacb2c8e3))
* **jellyfin:** pick up MDBList watches marked with a past date ([596a1f5](https://github.com/cedya77/aiometadata/commit/596a1f562e05466db3f8a9f5773c6fa60ba1f85b))
* **jellyfin:** play the default version when "Load the stream list" is picked ([fe70827](https://github.com/cedya77/aiometadata/commit/fe70827a014b065e8a9a1bdbbb0968bca205eeab))
* **jellyfin:** refresh MDBList Up Next when a followed show's next episode airs ([7826c17](https://github.com/cedya77/aiometadata/commit/7826c17ebad9ea1bfaa75d5a95703a8bf234db95))
* **jellyfin:** return the neighbouring episodes for AdjacentTo ([3b102b0](https://github.com/cedya77/aiometadata/commit/3b102b0ef41ce6f43d03621e5b42f5344a0e8f9d))
* **jellyfin:** reuse a title's stream list for three minutes by default ([28610bb](https://github.com/cedya77/aiometadata/commit/28610bb3837d6f27085198406e2a44c4a8ff2998))
* **jellyfin:** send artwork at the width the client asks for ([679fdbf](https://github.com/cedya77/aiometadata/commit/679fdbf42e3dc41d8d2c349f5f6206e821d1ef27))
* **jellyfin:** serve profile pictures at /UserImage ([8552807](https://github.com/cedya77/aiometadata/commit/855280752d863c9784625a0b723db6f1acf73ec6))
* **jellyfin:** show a title once when several watchlists list it ([3be7c06](https://github.com/cedya77/aiometadata/commit/3be7c06f063a1c79d78c9504cc15b635027bc6ea))
* **jellyfin:** show watchlisted movies on the calendar ([5c51996](https://github.com/cedya77/aiometadata/commit/5c51996b70f4421291f8c60daa4cb788f222c921))
* **jellyfin:** sign out devices of a user removed from the configuration ([d29bd1a](https://github.com/cedya77/aiometadata/commit/d29bd1a8e2bfd57caddce5619266655b4d26004e))
* **jellyfin:** use the PublicMetaDB watchlist for favourites without its catalog ([fc14f9d](https://github.com/cedya77/aiometadata/commit/fc14f9d9f9f8a10ceb1bdb7a0fbb36a52662a94a))
* **mal:** pick up a new season's episodes once it premieres ([d85b4e1](https://github.com/cedya77/aiometadata/commit/d85b4e10d232e66cce10dd1555c92e8f4c9c7e60))
* **mal:** read MAL from the public Tenrai API now that the public Jikan API has shut down ([8f13e68](https://github.com/cedya77/aiometadata/commit/8f13e683767f82ddd929094401269eb64fd3093f))
* **mal:** show a whole decade when its catalog's genre is None ([6239804](https://github.com/cedya77/aiometadata/commit/6239804e284359dac39d84eb06a9ec91df10698a))
* **manifest:** leave the Rate Me button out of Catalog Mode Only installs, so it shows once from the install that supplies meta ([62403be](https://github.com/cedya77/aiometadata/commit/62403be176401f66d62c9c7d67ee9063aac33b3d))
* **mdblist:** skip MDBList until a long Retry-After passes instead of waiting it out ([68cd967](https://github.com/cedya77/aiometadata/commit/68cd96766bb6d3cc05a94540d79181e0c2754b67))
* **search:** resolve Lumiere and IMDb search results with the configured meta provider ([#795](https://github.com/cedya77/aiometadata/issues/795)) ([a4c67c3](https://github.com/cedya77/aiometadata/commit/a4c67c30a489d087b63bc23e7a0ecac2a9743e2e))
* serve rating page titles, imported manifests and proxied art in their own formats ([6a2fe46](https://github.com/cedya77/aiometadata/commit/6a2fe4611040dce8bd54bd617430eabf2d518aaa))
* **tmdb:** try pt-PT before English for pt-BR metadata ([#796](https://github.com/cedya77/aiometadata/issues/796)) ([189718c](https://github.com/cedya77/aiometadata/commit/189718c625d57a0d317c730799d9a5d15db069ed))
* **tvdb:** read Alternate Order 2 and Alternate DVD Order from their seasons ([4697283](https://github.com/cedya77/aiometadata/commit/4697283145c9db569978017a889d00d2518d3d48))
* **watch-tracking:** lower AniList and MyAnimeList progress when episodes are unwatched ([97cf591](https://github.com/cedya77/aiometadata/commit/97cf591070d8fc07717bce2108eee955b9074f4c))
* **watch-tracking:** unwatch a season on PublicMetaDB one episode at a time ([b76802e](https://github.com/cedya77/aiometadata/commit/b76802e5c1e1880c41cbe9fb6bef0bad99ebfa87))


