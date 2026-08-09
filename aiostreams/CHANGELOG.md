# Changelog

## v2.33.0

## [2.33.0](https://github.com/Viren070/AIOStreams/compare/v2.32.1...v2.33.0) (2026-08-09)


### Features

* add configuration variants with CEL ([b912080](https://github.com/Viren070/AIOStreams/commit/b912080a7ec11fb709c9d4ba3a7b7caa4acc34d4))


### Bug Fixes

* **builtins/nab:** apply seasonEpisodeStrategy for indexers without ID support ([#1165](https://github.com/Viren070/AIOStreams/issues/1165)) ([877b6c4](https://github.com/Viren070/AIOStreams/commit/877b6c4ff821fd5865343c821670779c2076e7be))
* **builtins/nab:** break down ID search support by media type in connection test ([#1166](https://github.com/Viren070/AIOStreams/issues/1166)) ([1ddb54a](https://github.com/Viren070/AIOStreams/commit/1ddb54a1346a21b1da750385461c041cace6846e))


## v2.32.1

## [2.32.1](https://github.com/Viren070/AIOStreams/compare/v2.32.0...v2.32.1) (2026-08-05)


### Bug Fixes

* **config/oidc:** preserve trailing slashes ([36bd3a9](https://github.com/Viren070/AIOStreams/commit/36bd3a9b50b0516d359d115e69f7b2a603732599)), closes [#1157](https://github.com/Viren070/AIOStreams/issues/1157)
* preserve addon-provided subtitles field on Stream objects ([#1155](https://github.com/Viren070/AIOStreams/issues/1155)) ([6f8b078](https://github.com/Viren070/AIOStreams/commit/6f8b07841e417b3ca062333e81b2d3b2736d4b81)), closes [#1154](https://github.com/Viren070/AIOStreams/issues/1154)
* **sel:** update service list for `service()` ([ee3d39b](https://github.com/Viren070/AIOStreams/commit/ee3d39be9aa71fc9db253b49ab4b1a20c2fd52e9))


## v2.32.0

## [2.32.0](https://github.com/Viren070/AIOStreams/compare/v2.31.1...v2.32.0) (2026-08-05)


### Features

* add `repack` and `proper` to smart detect attributes ([8aab913](https://github.com/Viren070/AIOStreams/commit/8aab913206142cdd65df651fbc6fe2dbcfe10638)), closes [#1110](https://github.com/Viren070/AIOStreams/issues/1110)
* **builtins/nab:** send daily params (season=YYYY&ep=MM/DD) for date-based shows instead of numeric season/ep ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **builtins:** absolute-episode search for non-anime titles ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **builtins:** add `scene` as spec for title lang map ([50c0734](https://github.com/Viren070/AIOStreams/commit/50c07341dd411326a4cc06fdc310fde76585f530))
* **builtins:** drop non-Latin-script titles from search queries ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **builtins:** query scene, year and country variants for same-name series ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **config-profiles:** initial implementation ([5bcfe34](https://github.com/Viren070/AIOStreams/commit/5bcfe347a4554f4b109c809bfc22780d82b5624c))
* **core:** add `ambiguousResults` option to title matching ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** add `country` and `episodeTitle` to smart detect attributes ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** add `idMatched` to flag results a source identified by external ID ([d25c781](https://github.com/Viren070/AIOStreams/commit/d25c7815e08e0a645b2cc1dc11b3253c06807183))
* **core:** add episode title matching filter ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** add language inference toggle ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** apply year matching strict mode to any request type ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** consume `proper` field from parser ([d0e0a47](https://github.com/Viren070/AIOStreams/commit/d0e0a4747cc333df6cd5a9a071d6ee28b6e5da81))
* **core:** detect date-based series and search/match them by episode air date ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **core:** infer stream language from a matched episode title ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** passthrough all behaviorHints on stream object ([3e13704](https://github.com/Viren070/AIOStreams/commit/3e13704ec4573ee1031f3df2226da9accb6054fd)), closes [#1129](https://github.com/Viren070/AIOStreams/issues/1129)
* **dashboard/usenet:** add per page option to library ([1bcff8b](https://github.com/Viren070/AIOStreams/commit/1bcff8bb7609bc2320cf0dcedc916f8873d1f7b1))
* **dashboard:** add unblock release button to usenet library ([8f98dff](https://github.com/Viren070/AIOStreams/commit/8f98dff3f77301d35b662e09527f017857199395))
* **dashboard:** reorganise settings and improve settings search ([2ee6ba3](https://github.com/Viren070/AIOStreams/commit/2ee6ba334cc199ec7eb702324034492be2d0b859))
* **dashboard:** unify proxy and usenet stream tracking ([059dd28](https://github.com/Viren070/AIOStreams/commit/059dd28a93ba79a8a9a5f6134f6d46b87dbcfc95))
* db backed task state ([f5496b8](https://github.com/Viren070/AIOStreams/commit/f5496b87ca007aa018feb068fcaee6cdaa05c3b9))
* **debrid:** add torrin service ([d465e6b](https://github.com/Viren070/AIOStreams/commit/d465e6bf2443e0e131dc4c22bf3ad118d2f9b43a)), closes [#1014](https://github.com/Viren070/AIOStreams/issues/1014)
* **deduplicator:** add `idMatched` to the merged metadata fields ([d25c781](https://github.com/Viren070/AIOStreams/commit/d25c7815e08e0a645b2cc1dc11b3253c06807183))
* **formatter:** add `{stream.idMatched}` ([f1c17fe](https://github.com/Viren070/AIOStreams/commit/f1c17fee9a55977f573ed8bc436a2488dbddfb20))
* **formatter:** add `country` and `episodeTitle` variables ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **formatter:** add `languagecode` and `languageemoji` string/array modifiers ([abc2e6c](https://github.com/Viren070/AIOStreams/commit/abc2e6c22f631ea4c3cc1992165c97428c605721))
* **formatter:** add all metadata fields ([23ef02f](https://github.com/Viren070/AIOStreams/commit/23ef02fad9377c1c5fdc6ca500d9333910efaf98))
* **formatter:** add better diagnostics ([412a14a](https://github.com/Viren070/AIOStreams/commit/412a14a4e9d467743016f115a5b79b306be65f93))
* **formatter:** add rich editor and update snippets ([5d81720](https://github.com/Viren070/AIOStreams/commit/5d817201a1ebb52091fe2414514bae6be6765f7f))
* **formatter:** rewrite template engine with parser, compiler and new syntax ([bbf1098](https://github.com/Viren070/AIOStreams/commit/bbf1098cfdaead0cb68f299ae3bcd3bce592b062))
* **frontend/menu-tabs:** switch to standard motion tabs ([80629e1](https://github.com/Viren070/AIOStreams/commit/80629e1ae83be0b1819f25e67749484cf461dc34))
* **frontend:** redesign formatter preview and include all inputs ([96cbf96](https://github.com/Viren070/AIOStreams/commit/96cbf96ffabd25b22d78bf6406b47b210ce8f859))
* **frontend:** shift-click filter list arrows to move to top/bottom ([73889af](https://github.com/Viren070/AIOStreams/commit/73889af68917660e883b8dfcae02a8d62000b446))
* **frontend:** support drag-and-drop for filter input lists ([#1123](https://github.com/Viren070/AIOStreams/issues/1123)) ([09e6013](https://github.com/Viren070/AIOStreams/commit/09e6013f14fbe99d11d902efc98de3b500d8395e))
* **metadata/skyhook:** fall back when a keyed tvdb lookup fails ([e1f1681](https://github.com/Viren070/AIOStreams/commit/e1f168101b7d43024e7220d131ac50f5bd6393f0))
* **metadata:** add episode-facts resolver (numbering-agnostic date-based detection + per-episode air-date resolution via TVDB/TMDB/Cinemeta) ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** add Wikidata imdb/tvdb/tmdb id-mapping dataset (IdMappingDataset) ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** choose primary title by explicit per-media-type provider priority ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** detect same-name series conflicts and origin country ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **metadata:** fetch Sonarr scene-mapping title aliases (SceneMappingDataset) ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** resolve each field by explicit source priority ([e1f1681](https://github.com/Viren070/AIOStreams/commit/e1f168101b7d43024e7220d131ac50f5bd6393f0))
* **metadata:** resolve episode titles in every language a source provides ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6)), closes [#1126](https://github.com/Viren070/AIOStreams/issues/1126) [#749](https://github.com/Viren070/AIOStreams/issues/749) [#635](https://github.com/Viren070/AIOStreams/issues/635) [#741](https://github.com/Viren070/AIOStreams/issues/741)
* **metadata:** resolve the years a release may legitimately be tagged with ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **metadata:** resolve TVDB English translation instead of the original-language name ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** skyhook TVDB metadata fallback ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* **metadata:** surface tmdb air dates and tvdb original language ([85a4c61](https://github.com/Viren070/AIOStreams/commit/85a4c6164c0ff77328562c7dc7ce183549922b2b))
* **nab:** add test button and remove apiPath setting ([a84432a](https://github.com/Viren070/AIOStreams/commit/a84432af6bf0cefb406e16d6e33ee3926a75969e)), closes [#1124](https://github.com/Viren070/AIOStreams/issues/1124)
* **oidc:** initial support ([c8b725e](https://github.com/Viren070/AIOStreams/commit/c8b725ee568d082d9d53c50579933e75897271de))
* **parser:** expose `country` and `episodeTitle` from release names ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **release-blocklist:** blocklist compressed/solid/unsupported archives globally ([78ed29a](https://github.com/Viren070/AIOStreams/commit/78ed29a42cf7529a64197e3452dc8d0e27ee6f52))
* **release-blocklists:** support batch source operations ([#1109](https://github.com/Viren070/AIOStreams/issues/1109)) ([68edbe9](https://github.com/Viren070/AIOStreams/commit/68edbe98fc37700246791003fdcd1e7987b5fce3))
* **sel:** add `idMatched()` stream expression function ([d25c781](https://github.com/Viren070/AIOStreams/commit/d25c7815e08e0a645b2cc1dc11b3253c06807183))
* **streams:** add bandwidth accounting with optional global and per-user limits ([059dd28](https://github.com/Viren070/AIOStreams/commit/059dd28a93ba79a8a9a5f6134f6d46b87dbcfc95))
* **streams:** add temporary user and per-title stream blocks ([059dd28](https://github.com/Viren070/AIOStreams/commit/059dd28a93ba79a8a9a5f6134f6d46b87dbcfc95))
* **streams:** count the connection limit across proxy and usenet together ([059dd28](https://github.com/Viren070/AIOStreams/commit/059dd28a93ba79a8a9a5f6134f6d46b87dbcfc95))
* **usenet/pool:** add negative cache ([2eb84eb](https://github.com/Viren070/AIOStreams/commit/2eb84ebdc968736fc028ed3953cf280795733120))
* **usenet:** add indexer metrics ([0331ef5](https://github.com/Viren070/AIOStreams/commit/0331ef54f8b3e9b4bc6fc0748c543d5973795035))
* **usenet:** add short-lived failing stream cache ([8b92b2b](https://github.com/Viren070/AIOStreams/commit/8b92b2b62ea48fdfd4a7dc311b080d21ad56eca2))
* **usenet:** repair MKV holes with EBML Void fill instead of raw zeros ([faf9542](https://github.com/Viren070/AIOStreams/commit/faf95422fd799f8cfd8f7ad78e9ac84968fd1b56))
* **usenet:** rework strict damage policy to skip degraded releases ([4f0c4aa](https://github.com/Viren070/AIOStreams/commit/4f0c4aace62d5981f495f42659b1ae4e83764b11)), closes [#1101](https://github.com/Viren070/AIOStreams/issues/1101)
* **usenet:** support failover/hole-filling for undecodable articles ([3351417](https://github.com/Viren070/AIOStreams/commit/3351417b04ad041b8262dae5eaf2e5b0042dc128))


### Bug Fixes

* add `releaseGroup` to default smart detect attributes ([45a111b](https://github.com/Viren070/AIOStreams/commit/45a111b34b8ddc8550e4d4a1cfc0dc17299fa474))
* allow hiding fields from command pallete ([f1d70fa](https://github.com/Viren070/AIOStreams/commit/f1d70fac46af70968700dfa2b7d52dc9beaab39a))
* **builtins/nab:** add numeric param fallback for daily searches ([73c0e3b](https://github.com/Viren070/AIOStreams/commit/73c0e3b196676a4f2fefcc98097993b109a5902a))
* **builtins/nab:** make guid optional ([0954fc8](https://github.com/Viren070/AIOStreams/commit/0954fc80ac5473e4f732aa2db78b53e530b853be))
* **builtins/nab:** retain repeated attrs and region-qualified languages ([941f5dd](https://github.com/Viren070/AIOStreams/commit/941f5dd5bc788cec23cf6509f90f0c533810e827)), closes [#1152](https://github.com/Viren070/AIOStreams/issues/1152)
* **builtins/newznab:** loosen enclosure check ([7f9a9b6](https://github.com/Viren070/AIOStreams/commit/7f9a9b6620104205155d1f4349d5490c3c9cd707))
* **builtins/newznab:** parse prowlarr indexer name field ([2ab8d48](https://github.com/Viren070/AIOStreams/commit/2ab8d48dcc51d15dfbd7811b92fa277acda6731c))
* **builtins:** always search non-prefixed absolute episode ([cbf8761](https://github.com/Viren070/AIOStreams/commit/cbf87618c3531a6ca15f9a379090b69ca860a505))
* **builtins:** only use sceneTitles for date based ([5c22564](https://github.com/Viren070/AIOStreams/commit/5c22564e00ec07fb79b41f6be3cde527d50febfe))
* **cache:** add max cached value size ([1668652](https://github.com/Viren070/AIOStreams/commit/16686521518d8feb306969549b1c3607ad05d21b))
* **config:** add sane min/step values for `usenet.streamingPriority` ([6900423](https://github.com/Viren070/AIOStreams/commit/69004232c4839faefde816b5e73f304bbb11f7a2))
* **core:** discard results whose country tag names a different series ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **core:** match series years pointwise instead of across the whole run ([7e0c268](https://github.com/Viren070/AIOStreams/commit/7e0c268642d22f75df331c470d82c85e28a067b6))
* **dashboard/blocklist:** disable certain batch actions on local source selection ([#1122](https://github.com/Viren070/AIOStreams/issues/1122)) ([90717a4](https://github.com/Viren070/AIOStreams/commit/90717a4589add2ed18f3fe775f680bd6d6fc3e79))
* **dashboard/overview:** update section links ([f8637a5](https://github.com/Viren070/AIOStreams/commit/f8637a540c95c74b053e77c908a4dd203a145a5c))
* **dashboard/streams:** fix bandwidth graph, add per-user view, adjust mobile active streams view ([01171d2](https://github.com/Viren070/AIOStreams/commit/01171d27ce30712e59031838510bbdad5e9f1d02))
* **dashboard:** fix speed reporting ([cbea712](https://github.com/Viren070/AIOStreams/commit/cbea712c2bb3c2ca95f95f6f3e01f6c3fcdae888))
* **debrid:** improve error video mapping ([670d931](https://github.com/Viren070/AIOStreams/commit/670d93170a03eec89f10c6f8a11118c45a3c4bbc))
* **debrid:** map timeout to downloading video ([929aabd](https://github.com/Viren070/AIOStreams/commit/929aabd1b3add70315d8851655a92abeb7549fdb))
* disable trakt alias fetching by default and require client ID ([ba5d9eb](https://github.com/Viren070/AIOStreams/commit/ba5d9eb7c5861316e4b711260166679b21584fcb))
* **filterer:** match date-named releases in seasonEpisodeMatching ([3cf7f84](https://github.com/Viren070/AIOStreams/commit/3cf7f84862be964e2298b07ef0b22f308ffedb63))
* fix some typing issues ([7c66a13](https://github.com/Viren070/AIOStreams/commit/7c66a133231573261f23fbeb730efa8d17093456))
* **formatter:** add render budget ([0878f35](https://github.com/Viren070/AIOStreams/commit/0878f35aa65ebe440bc877847e8dfe70c469d317))
* **formatter:** make boolean-chain presence independent of operator mix ([e072e0a](https://github.com/Viren070/AIOStreams/commit/e072e0a52848b34ebe971e207aa4f0dc2ea72d2d))
* **formatter:** normalise duration in time modifier to support metadata.runtime ([7315281](https://github.com/Viren070/AIOStreams/commit/7315281d6732c919d017127eafb5b0e546ab5f4e))
* **frontend/checkbox:** stop calling a stale onValueChange ([ad02abe](https://github.com/Viren070/AIOStreams/commit/ad02abef71eb1f0a6bf6956c7792f70d70a6f535))
* **frontend/config-modal:** focus password input when initialUuid present ([2c1e303](https://github.com/Viren070/AIOStreams/commit/2c1e3037908e72155803c86b9770bb800155178c))
* **frontend/formtter:** re-order tabs ([3c24ba9](https://github.com/Viren070/AIOStreams/commit/3c24ba9dd9a6280e9a9badd47e270b210b68819b))
* **frontend:** walk through subOptions when redacting/removing preset options ([13deafc](https://github.com/Viren070/AIOStreams/commit/13deafc23e4dac6c3d255e4e632f393a3468aa28))
* **metadata/cinemeta:** check number field for episode too ([6672990](https://github.com/Viren070/AIOStreams/commit/667299033db8af3a485253f3c509bd7ea17e9b95))
* **metadata/cinemeta:** parse en dash year ranges ([e1f1681](https://github.com/Viren070/AIOStreams/commit/e1f168101b7d43024e7220d131ac50f5bd6393f0))
* **metadata/id-mappings:** drop conflicting records ([4834b70](https://github.com/Viren070/AIOStreams/commit/4834b7078077496cd2beada87bbab37858171120))
* **metadata/tmdb:** keep primary title the en-US title ([29596a2](https://github.com/Viren070/AIOStreams/commit/29596a25d2864605688f0af73415df6fb257fb56))
* **metadata/tvdb:** allow nullable averageRuntime ([1c7cc83](https://github.com/Viren070/AIOStreams/commit/1c7cc833d08e6c873a02c6ab266995cb683c850a))
* **metadata:** always fetch skyhook ([a8b7184](https://github.com/Viren070/AIOStreams/commit/a8b7184fbff4c75a054fc891feec8caad6c72a86))
* **metadata:** keep original-language tag on ambiguously-tagged titles ([4f7e815](https://github.com/Viren070/AIOStreams/commit/4f7e81503731128260cf82808cedfcc88b482231))
* **metadata:** only fetch skyhook for series ([e4610b5](https://github.com/Viren070/AIOStreams/commit/e4610b5045438c66cd67bb73da15e7c1dc14275f))
* **metadata:** resolve episode titles in the request's own numbering ([2ca7a08](https://github.com/Viren070/AIOStreams/commit/2ca7a08c316c05cf57396b3084192bb2abf7a044))
* **presets/debridioScraper:** override parser and set indexer regex to undefined ([035d685](https://github.com/Viren070/AIOStreams/commit/035d685f78eefffd8074dae077885019391abbb1))
* **presets:** show addon name in service error  ([#1117](https://github.com/Viren070/AIOStreams/issues/1117)) ([8a7cf49](https://github.com/Viren070/AIOStreams/commit/8a7cf49c5e54f6d4644302fa9b484760b2ecbb9f))
* **release-blocklists:** update backbone map ([d5629e1](https://github.com/Viren070/AIOStreams/commit/d5629e19ef8675deefa83c952d04256ab1140b89))
* **server:** apply rate limit middleware before user data ([a6f850b](https://github.com/Viren070/AIOStreams/commit/a6f850b8bb152ec89de8e8f32ad0463cc1749e66))
* **server:** await initialisation tasks on startup ([16dbda4](https://github.com/Viren070/AIOStreams/commit/16dbda4fe14c259d3d6a00debab1d19482c8d6d1))
* **serviceWrapper:** only use fileIdx when no metadata available ([b652c4e](https://github.com/Viren070/AIOStreams/commit/b652c4e742031e6114386f5160dd62650c40d226))
* some fixes ([3f8396b](https://github.com/Viren070/AIOStreams/commit/3f8396b6eaaaf0c94701be75af3b211f81c8f2d6))
* **streams:** some fixes ([67b7dcb](https://github.com/Viren070/AIOStreams/commit/67b7dcb78787fc4b790c985c01627a67a1f72997))
* **usenet:** adjust segment timeout settings ([9fec385](https://github.com/Viren070/AIOStreams/commit/9fec385c1e5a21e85115059c2f8bcd47bf753bb9))
* **usenet:** group unnamed rar volumes by header identity ([dfc4428](https://github.com/Viren070/AIOStreams/commit/dfc442892056589dd7ea3550b3ac79d3cf93eae7)), closes [#1113](https://github.com/Viren070/AIOStreams/issues/1113)
* **usenet:** only report playable files and fail imports lacking one ([5f91bcb](https://github.com/Viren070/AIOStreams/commit/5f91bcb11a8681c9cd673b4910de1418322f944f))
* **usenet:** redirect to static video on byte-serving path errors ([9983f87](https://github.com/Viren070/AIOStreams/commit/9983f877f027b29d9de8cc72d3447af04a8430c5))
* **usenet:** resolve backing sets from the captured archive layout ([55bedba](https://github.com/Viren070/AIOStreams/commit/55bedbacbc5ac0e3ca44aae9d0b9a864d78e443e))
* **wrapper:** ensure timeout is cleared in _request method ([fd05cf6](https://github.com/Viren070/AIOStreams/commit/fd05cf65999c27694e16301222801c0028d3bc82))
* **wrapper:** limit background requests and negative cache manifest failures ([0abc7a2](https://github.com/Viren070/AIOStreams/commit/0abc7a2eda9c93fd116a55bddf0ada1a03e909c1))


### Performance Improvements

* **auth:** cache the derived config key per credential ([b0bf5f4](https://github.com/Viren070/AIOStreams/commit/b0bf5f4943c6ee2aa8034af1c632e97e53e2ed20))
* extend derived key cache ttl ([1846d0a](https://github.com/Viren070/AIOStreams/commit/1846d0a2f234a64254820b81e60e2651c7b9326d))
* memoise title parsing ([f9e202a](https://github.com/Viren070/AIOStreams/commit/f9e202ac7b016324030b65682911722ebc21eac7))
* only build pipeline cache key when necessary ([82087a8](https://github.com/Viren070/AIOStreams/commit/82087a876aafb6eee4be87185f296663773b92ba))
* only compile resource regex once ([6e2053d](https://github.com/Viren070/AIOStreams/commit/6e2053ded5b170ae7987c7ec7ab2c3bce329cd5d))
* **usenet:** match par2 descriptors during the probe pass ([c34cff5](https://github.com/Viren070/AIOStreams/commit/c34cff5f1c357395d10103819f0e8f052793f1a9))


### Reverts

* **dashboard:** remove proxy and usenet streams page ([a313869](https://github.com/Viren070/AIOStreams/commit/a31386940aab2de909e0f4fd266bfa48da741333))


## v2.31.1

## [2.31.1](https://github.com/Viren070/AIOStreams/compare/v2.31.0...v2.31.1) (2026-07-17)


### Features

* add `DISK_CACHE_DIR` for overriding disk backed cache directory ([d27bbab](https://github.com/Viren070/AIOStreams/commit/d27bbab0c864cf6b3ea053b8c19a84521b9745f4)), closes [#1100](https://github.com/Viren070/AIOStreams/issues/1100)
* **config:** support marking settings as deprecated ([f0e6eea](https://github.com/Viren070/AIOStreams/commit/f0e6eea85d95cf1977f8e7734982f6377fe04973))
* **dashboard:** add clear logs button ([#1076](https://github.com/Viren070/AIOStreams/issues/1076)) ([2159015](https://github.com/Viren070/AIOStreams/commit/21590151e10cab558f1b122899ec042b1f92fb65))
* **parser/regex:** add `DVD REMUX` quality ([#1103](https://github.com/Viren070/AIOStreams/issues/1103)) ([d0ce2a3](https://github.com/Viren070/AIOStreams/commit/d0ce2a30b21a8030982b26708641506a20b95e5d))
* **seadex:** always apply group matching and expose match method ([28c82eb](https://github.com/Viren070/AIOStreams/commit/28c82eb6b0fcee4b5a58e69bd737c23ead7147e9)), closes [#990](https://github.com/Viren070/AIOStreams/issues/990)


### Bug Fixes

* **api/nab:** handle rss request and other fixes ([8c08077](https://github.com/Viren070/AIOStreams/commit/8c080770aeb4cc99c6d927ea3a2ece6810febdfd))
* **blocklists:** derivce source name from username for raw gist urls automatically ([8ae4914](https://github.com/Viren070/AIOStreams/commit/8ae49146e8bd2d9fc53d9df6d1fce2bd753804d4)), closes [#1102](https://github.com/Viren070/AIOStreams/issues/1102)
* **builtins/knaben:** calculate age based on lastSeen ([21814d4](https://github.com/Viren070/AIOStreams/commit/21814d43399e9e01f4dad62345c742a38239bbbf))
* **builtins:** only create infoHash field for torrents ([06256f7](https://github.com/Viren070/AIOStreams/commit/06256f768e430c8fa027ab5a15ab97032b5420bc))
* **config:** fix parsing for builtin title lang setting ([f9afa75](https://github.com/Viren070/AIOStreams/commit/f9afa75b289cbd2c978dbed159d884e67a2d77a0))
* **core/formatter:** update small caps map ([edf9ca5](https://github.com/Viren070/AIOStreams/commit/edf9ca5a3480a0f8723c8ed47bad92747380fa45)), closes [#1112](https://github.com/Viren070/AIOStreams/issues/1112)
* **debrid:** encode webdav path for webdav based playback services ([50d199f](https://github.com/Viren070/AIOStreams/commit/50d199fd450a90c791671268d4a1910b8d2c962a)), closes [#1006](https://github.com/Viren070/AIOStreams/issues/1006)
* **deduplicator:** handle stremio-usenet type when detecting usenet stream ([c0be37d](https://github.com/Viren070/AIOStreams/commit/c0be37d74600d8561155294b93d5be727c115e42))
* **filterer:** only apply digital release tolerance to unreleased content ([35315d1](https://github.com/Viren070/AIOStreams/commit/35315d108350f1f2d1f57da85309e7484c5c5145))
* **filterer:** re-evaluate included stream expressions on the full result set ([e7aee6b](https://github.com/Viren070/AIOStreams/commit/e7aee6bb863cabc0bc3e043f8047ea31f86a04f8)), closes [#387](https://github.com/Viren070/AIOStreams/issues/387)
* **frontend:** try to improve password manager compatibility ([a9542b6](https://github.com/Viren070/AIOStreams/commit/a9542b605a96c2bddcddc1dabb0b16cd2e4e208a))
* **http:** follow redirects manually to re-evaluate header/proxy rules ([8d582af](https://github.com/Viren070/AIOStreams/commit/8d582af3ae06d9703edc22437d0f74dcf6f69702))
* improve failover logs ([5585ee7](https://github.com/Viren070/AIOStreams/commit/5585ee7d7c9614c7e790be0812ce3acd3790c2e6))
* **logging:** redact sensitive info in all log sinks and hash credentials in cache/lock keys ([3f2a970](https://github.com/Viren070/AIOStreams/commit/3f2a9701fb0534bd87aa24827c0b2e96a2de9310)), closes [#849](https://github.com/Viren070/AIOStreams/issues/849) [#952](https://github.com/Viren070/AIOStreams/issues/952)
* loosen released schema to string instead of strict datetime ([87967d2](https://github.com/Viren070/AIOStreams/commit/87967d29987e12170e5707e66a95cddc2a54dbaf)), closes [#831](https://github.com/Viren070/AIOStreams/issues/831)
* **metadata/tmdb:** use `original_name` field for TVDetails ([f3aea6b](https://github.com/Viren070/AIOStreams/commit/f3aea6b03ed21cd5c51dd543310c82ffe55b2593))
* **parser/regex:** adjust `AI` filter and add separate `Upscaled` filter ([#1105](https://github.com/Viren070/AIOStreams/issues/1105)) ([4db1272](https://github.com/Viren070/AIOStreams/commit/4db12724d2ce576366b5b3e9a844075cbe4c9b3e))
* **parser:** adjust bluray regex ([bf80194](https://github.com/Viren070/AIOStreams/commit/bf80194cb62e1a79fa98c3c4215e0a104994071c))
* **parser:** check for plus symbol separately to avoid false positives in service parser ([f5c84b1](https://github.com/Viren070/AIOStreams/commit/f5c84b1ada59da27144b0288b8028d53bcec449d))
* **parser:** use language-aware transliteration for scrape queries and title matching ([7c51cec](https://github.com/Viren070/AIOStreams/commit/7c51cec9837d7453d14781b3c7cb5bcdce6771d7)), closes [#1030](https://github.com/Viren070/AIOStreams/issues/1030)
* **presets/argentinaTv:** only override streams with URL as live ([4cae141](https://github.com/Viren070/AIOStreams/commit/4cae14179e7bada45dc3cb6acdc6423646cc4242)), closes [#859](https://github.com/Viren070/AIOStreams/issues/859)
* **release-blocklist:** only write an override when a remote source flags the release ([#1104](https://github.com/Viren070/AIOStreams/issues/1104)) ([b527742](https://github.com/Viren070/AIOStreams/commit/b52774277cc65aa33ebb02072cb122653a5dbd18))
* split at first colon only to allow passwords with colons in `AIOSTREAMS_AUTH` ([041a2c3](https://github.com/Viren070/AIOStreams/commit/041a2c3c272188c682bf5dbacf73b81311eedec4))
* update parser ([4f4a866](https://github.com/Viren070/AIOStreams/commit/4f4a8661512a91ff88ae9611b3166e99523aba7c))
* **usenet:** name archive-inner downloads by their display name ([dc05750](https://github.com/Viren070/AIOStreams/commit/dc05750409f4669e8482b5ef51badb2c634187d3))
* **usenet:** recognize old-style .sNN–.zNN rar volume rollover ([98c33db](https://github.com/Viren070/AIOStreams/commit/98c33dbf304028bce72530806ab36094dd61c0b6))
* **usenet:** report the specific reason for unstreamable archives ([9569bc5](https://github.com/Viren070/AIOStreams/commit/9569bc58d42f036374dd91d46868517a5848e3bd))
* **usenet:** use PAR2 names when obfuscation fragments a rar set ([7fd76c1](https://github.com/Viren070/AIOStreams/commit/7fd76c1c49416567f29ecde2283d302e6998ba38))


### Code Refactoring

* centralise auth check and give detailed reason ([16d3e09](https://github.com/Viren070/AIOStreams/commit/16d3e0998bb08160d8421a547ecfec2d00051049))


## v2.31.0

## [2.31.0](https://github.com/Viren070/AIOStreams/compare/v2.30.6...v2.31.0) (2026-07-14)


### Features

* add newznab/torznab indexer endpoints ([5e5ee1c](https://github.com/Viren070/AIOStreams/commit/5e5ee1cea6316d68ed40fe5d72a1e2141f6ac554))
* add option to enable failover during pre-caching ([#1038](https://github.com/Viren070/AIOStreams/issues/1038)) ([bc42579](https://github.com/Viren070/AIOStreams/commit/bc425794f57c085b696e41c5fe21f29bf48b173e))
* **altmount:** use native /api/nzb/streams API instead of SABnzbd+WebDAV ([#1023](https://github.com/Viren070/AIOStreams/issues/1023)) ([8886054](https://github.com/Viren070/AIOStreams/commit/8886054e1551963b442bf096ad0a35145cdf9516))
* **builtins/easynews-search:** attach probed media info and support v3 api ([df1539e](https://github.com/Viren070/AIOStreams/commit/df1539efc053578a32e8f7f19db88142032ab50d))
* **builtins/nab:** add configurable season pack search strategy for auto-mode series search ([#1061](https://github.com/Viren070/AIOStreams/issues/1061)) ([46eb329](https://github.com/Viren070/AIOStreams/commit/46eb329298615a8553e5b3a18852441ed773a987))
* **builtins:** adjust for aiostreams service ([7dabf46](https://github.com/Viren070/AIOStreams/commit/7dabf4625fc5a375651dbcdef5bd837c897c5fdc))
* **config:** alias renamed setting keys to preserve DB-stored values ([9b60a13](https://github.com/Viren070/AIOStreams/commit/9b60a13e7f42856820c7c5fc1c0c605fe63fa32f))
* **config:** support multiple env names ([6a2c31d](https://github.com/Viren070/AIOStreams/commit/6a2c31d31f2d4563deb0c2c0067b147e991fc289))
* **config:** usenet configuration schema & env metadata ([163198f](https://github.com/Viren070/AIOStreams/commit/163198f7dc8db7f9da7c626e2fa03ce33b16b1c0))
* **core:** add full-pipeline stream result cache ([#1075](https://github.com/Viren070/AIOStreams/issues/1075)) ([a0a82c9](https://github.com/Viren070/AIOStreams/commit/a0a82c96941981d935b218e11c11e613873a716f))
* **core:** consolidate env vars, user-agent & proxy settings ([eecfdbe](https://github.com/Viren070/AIOStreams/commit/eecfdbe1117d0e5c937b1e4c113397db55a9f51a))
* **core:** shared utils for usenet (xml, disk-backed cache, caches) ([6e191f0](https://github.com/Viren070/AIOStreams/commit/6e191f08e174b8b63dd7579494d18fdc046b4552))
* **dashboard/usenet:** move actions into dropdown menu, add requeue action, allow bulk requeue and block ([4910054](https://github.com/Viren070/AIOStreams/commit/4910054e728388ac87f22589d5012ba69fdb3c5e))
* **dashboard/usenet:** show hostname and full nzb url on hover ([aa2eec5](https://github.com/Viren070/AIOStreams/commit/aa2eec5c5328d02bf865675939b145bdd3a5bddc))
* **dashboard/usenet:** show nzb url in entry info modal ([8802e6f](https://github.com/Viren070/AIOStreams/commit/8802e6f2177b76849ab54deb92ef90e0894299ba))
* **dashboard:** add action menu to usenet settings page ([47cbf20](https://github.com/Viren070/AIOStreams/commit/47cbf208258b0cf76461350f950bafdf7b149a3c))
* **dashboard:** add command palette ([#1095](https://github.com/Viren070/AIOStreams/issues/1095)) ([55b1412](https://github.com/Viren070/AIOStreams/commit/55b1412448221a40f295b9999dc3356e75f3b8e2))
* **dashboard:** add confirmation dialog to clear all overrides ([41e20a2](https://github.com/Viren070/AIOStreams/commit/41e20a276d01fc945f723610c496936f19060b4f))
* **db:** usenet persistence (migrations & repositories) ([d2a490f](https://github.com/Viren070/AIOStreams/commit/d2a490fdc9beb81645e7f219af84e440a9d9e1d3))
* **debrid:** usenet streaming & aiostreams provider ([25d33c9](https://github.com/Viren070/AIOStreams/commit/25d33c971b9d396683b0ac248540a491c041c6c5))
* deduplicator merging, allow adding duplicates to failover list, allow external debrid addons for failover targets. fix proxying for failover targets ([dafbd53](https://github.com/Viren070/AIOStreams/commit/dafbd532fbdeaa60616e995733f56d9531435680))
* **formatter:** add `stream.preloading` variable for preload streams transparency ([79c6e28](https://github.com/Viren070/AIOStreams/commit/79c6e28f9bda432fb8afc0dd815d534ee088e13d))
* **frontend:** add logo and link to some compatible clients in install page ([fce8d42](https://github.com/Viren070/AIOStreams/commit/fce8d42ae5c8416fb02913cdfd73a821dd84d13e))
* **frontend:** simplify provider ordering/grouping ([d978aaa](https://github.com/Viren070/AIOStreams/commit/d978aaa73942b3ef42f070e6595735473d3a7a9a))
* **frontend:** UI primitives & dashboard wiring ([a72e945](https://github.com/Viren070/AIOStreams/commit/a72e945619d796a90c5d7fce684c1aee95b69b28))
* **frontend:** usenet dashboard ([c0c3ae9](https://github.com/Viren070/AIOStreams/commit/c0c3ae9d817acb991c7b796b3de28ca69d8d47f5))
* **main:** make failover generic, parallel and cross-type ([8aa62d7](https://github.com/Viren070/AIOStreams/commit/8aa62d7aef1f87b2e7657290ae7673c9d921b6b4))
* make log level and format runtime settings ([f4240df](https://github.com/Viren070/AIOStreams/commit/f4240dff3f969727b8105c249f4ea11c1ab62c14))
* move result limiting after SEL ([b4d513c](https://github.com/Viren070/AIOStreams/commit/b4d513c91eb847eb0e2ffd346978e05708c4755a))
* **presets:** add davex preset ([a7596d8](https://github.com/Viren070/AIOStreams/commit/a7596d8a0d396b8a37a5e4d41a3956d349ebe65a))
* **proxy:** serve nzbs from download manager ([3a5258e](https://github.com/Viren070/AIOStreams/commit/3a5258e318447c8179f720be98cec868ec3ca396))
* **release-blocklists:** add publishing page with gist provider ([e052cad](https://github.com/Viren070/AIOStreams/commit/e052cad8292b76b38171b836943de89450ff4b0b))
* **release-blocklists:** move public export settings to publishing page ([31fc06a](https://github.com/Viren070/AIOStreams/commit/31fc06a3234888874024c4bba52c308621f0d4ee))
* **release-blocklists:** shareable verdicts for dead and fake releases ([#1086](https://github.com/Viren070/AIOStreams/issues/1086)) ([41e20a2](https://github.com/Viren070/AIOStreams/commit/41e20a276d01fc945f723610c496936f19060b4f))
* remove unused nzb proxy ([5c14d71](https://github.com/Viren070/AIOStreams/commit/5c14d7163ab2c9d172cc7c7c61d8769b3e05f49d))
* **server:** usenet & dashboard API routes ([203ae49](https://github.com/Viren070/AIOStreams/commit/203ae495aada0281110e64dc105bd12ffa5a0506))
* **usenet/archive:** 7-Zip reader (LZMA) ([03ad62a](https://github.com/Viren070/AIOStreams/commit/03ad62ad214ccf2c8ac629a74835b954a462e744))
* **usenet/archive:** archive core (random-access fs, volumes, streams) ([8973ff0](https://github.com/Viren070/AIOStreams/commit/8973ff0a235a991e454d931065f34e2d4f012208))
* **usenet/archive:** crypto (AES, RAR/7z KDF) ([c3472aa](https://github.com/Viren070/AIOStreams/commit/c3472aaa7042f587ea13cbd29a42561dc54f7d96))
* **usenet/archive:** opener & set resolution ([3081055](https://github.com/Viren070/AIOStreams/commit/30810551c847ab975ef611788ad4142d38bfd304))
* **usenet/archive:** RAR reader (rar4 & rar5) ([818c878](https://github.com/Viren070/AIOStreams/commit/818c878e9d47447305568a1fcb7302fe2d8db55b))
* **usenet/inspect:** availability inspection & probing ([6faefe9](https://github.com/Viren070/AIOStreams/commit/6faefe93d8e027750fb9d11396743456a7cb96cc))
* **usenet/integration:** integration layer (engine, library, sessions, dashboard adapters) ([28e2aa4](https://github.com/Viren070/AIOStreams/commit/28e2aa47d6b69d73d02cd16628c173917c451f7f))
* **usenet/nntp:** NNTP protocol & connection pool ([b5157be](https://github.com/Viren070/AIOStreams/commit/b5157be945b7a1b89a856c878e8da4b33e92dbbf))
* **usenet/nzb:** NZB parsing module ([74b3c48](https://github.com/Viren070/AIOStreams/commit/74b3c488a325c8b3b0d70148ac886fe4a00f6ca3))
* **usenet/par2:** PAR2 decoding ([f211d17](https://github.com/Viren070/AIOStreams/commit/f211d172d5a96be1c11b71630ed2ef0870e9575c))
* **usenet/pool:** improve affinity handling ([d81acdd](https://github.com/Viren070/AIOStreams/commit/d81acdd88f1e70a1ba57e300790119a76fd60b3f))
* **usenet/pool:** segment pool & streaming primitives ([cce9175](https://github.com/Viren070/AIOStreams/commit/cce91759b8459e2e2554d06c2768a92df74ed677))
* **usenet/pool:** yEnc decoding ([bd4efd5](https://github.com/Viren070/AIOStreams/commit/bd4efd5679c878aa4428f0d3a9af321dd1eaf3d0))
* **usenet/sabnzbd:** SABnzbd-compatible API ([8345a7b](https://github.com/Viren070/AIOStreams/commit/8345a7b1a9001fc2cec4b2211cb5213574de949a))
* **usenet/stats:** stats accumulation ([ca70c59](https://github.com/Viren070/AIOStreams/commit/ca70c59ab0da93460a2ecac25a5553bf546fc272))
* **usenet:** add configurable pre-playback verify mode (stat/body) ([873208f](https://github.com/Viren070/AIOStreams/commit/873208fbdeff0943e4c7f85da7c6ef2fe62cc044))
* **usenet:** add delete all button to library ([#1034](https://github.com/Viren070/AIOStreams/issues/1034)) ([d88a774](https://github.com/Viren070/AIOStreams/commit/d88a7741fbd2e77cecdcaaf645e01b8016b84413))
* **usenet:** add inspect scheduler with max concurrent imports ([187e4aa](https://github.com/Viren070/AIOStreams/commit/187e4aab282b8e5b0ec28efd1c1f6e36b589e0a7))
* **usenet:** add stream stop button and idle-timeout setting ([bffcd97](https://github.com/Viren070/AIOStreams/commit/bffcd97fe0c7c738dd60953c2d39cef8ef6c0c95))
* **usenet:** census verifier and zero-fill hole padding ([57c6444](https://github.com/Viren070/AIOStreams/commit/57c6444165083f4819a8bbe8a5f1067ad20949e0))
* **usenet:** remove default pipeline depth setting ([e6eaeba](https://github.com/Viren070/AIOStreams/commit/e6eaebad95daef726260992ed233f6eeebdc734a))
* **usenet:** remove fail archive options ([d60a9ce](https://github.com/Viren070/AIOStreams/commit/d60a9ce366d418f0483f6de6f52f6bd6a836779e))
* **usenet:** store library aliases and key purely by content hash ([187e4aa](https://github.com/Viren070/AIOStreams/commit/187e4aab282b8e5b0ec28efd1c1f6e36b589e0a7))
* **usenet:** stream dashboard live stats and ease between frames ([713abaa](https://github.com/Viren070/AIOStreams/commit/713abaac441ec0f165014756b07cc25cb338bb7a))


### Bug Fixes

* adjust header handling ([b7f8623](https://github.com/Viren070/AIOStreams/commit/b7f86237264ebf4bb7a1bf43805a8c999f7e3734))
* **anime-database:** resolve season 1 to the first cour for TV-less shows ([10f4f38](https://github.com/Viren070/AIOStreams/commit/10f4f38c8a01509176bbabd0f01943aa81ac06f8))
* **api/user:** dont allow encrypted password for user API ([2852d01](https://github.com/Viren070/AIOStreams/commit/2852d01a2ef4e208497a33691d858e02d9388be2))
* **builtins/easynews-search:** default to 3.0 and add search concurrency of 2 to 2.0 ([1b0c05b](https://github.com/Viren070/AIOStreams/commit/1b0c05b12f3f8f80095216ca6b253048bf6b7608))
* **builtins:** convert parsedMediaInfo duration from seconds to ms when applying to streams ([df61254](https://github.com/Viren070/AIOStreams/commit/df61254cc951ab82535ef9795883dec1a0d84e18))
* **command-palette:** scroll to the selected setting on mobile with accordions ([8de1582](https://github.com/Viren070/AIOStreams/commit/8de1582f57f7dc04ee580e7685cfc1f5fd6258f3))
* **dashboard/usenet:** show toast on non .nzb file upload ([b24fc13](https://github.com/Viren070/AIOStreams/commit/b24fc13cbcd40a42713f9e127b6d026009c2c203))
* **dashboard:** adjust usenet library layout ([e3856e6](https://github.com/Viren070/AIOStreams/commit/e3856e61fd35f9f99be8702ac88402569f7ed00d))
* **disk-backed-cache:** await disk ready on get ([134156a](https://github.com/Viren070/AIOStreams/commit/134156ae43a76d6891838aa486de07c4ae13e81d))
* **disk-backed-cache:** periodically flush index and on server shutdown ([843f926](https://github.com/Viren070/AIOStreams/commit/843f92694633526efa30419279782787ffeaa634))
* **failover:** improve external target probing heuristics ([351560a](https://github.com/Viren070/AIOStreams/commit/351560a6a87f47c579be94a8e2465aad43aa3bc5))
* **filterer:** handle 0 in season/episode matching ([efca9a6](https://github.com/Viren070/AIOStreams/commit/efca9a63155cbbcacf72aa9790dbeab4fa7c69fb))
* **frontend:** description adjustments ([cc552af](https://github.com/Viren070/AIOStreams/commit/cc552afd3c114604cc3d823ea5aa27d52195e8b9))
* **main:** mutate original stream when marking `preloading` ([f64cfe1](https://github.com/Viren070/AIOStreams/commit/f64cfe17709df65766f07bebe0abe5a5b2c7579f))
* **media-info:** derive resolution from both dimensions and map more real-world codec aliases ([1daca60](https://github.com/Viren070/AIOStreams/commit/1daca60a5ffcfebe77e888a7a279b58ee4c75c48))
* **media-info:** ensure duration is in seconds ([aeb2898](https://github.com/Viren070/AIOStreams/commit/aeb289853c914c3bf731a1f6a1b3e292c9fe8e78))
* **presets/easynewsSearch:** valdiate easynews service credentials ([5a98930](https://github.com/Viren070/AIOStreams/commit/5a98930e218211d269757a60f1b70a673621567d))
* **presets/newznab:** move Season Pack Strategy option next to Search Mode ([#1093](https://github.com/Viren070/AIOStreams/issues/1093)) ([20100f6](https://github.com/Viren070/AIOStreams/commit/20100f612e48b8e4df7e7e44455c135668aa3cb4))
* **presets/usenetStreamer:** parse smart play into stream.message ([2237165](https://github.com/Viren070/AIOStreams/commit/2237165f7962ed77f592fa4c932b0853d2b0c3cc))
* **proxy:** pass `nzb_grabs` context to `shouldProxy` and `resolveOverrideHeaders` for `nzb` type ([#1046](https://github.com/Viren070/AIOStreams/issues/1046)) ([26d9601](https://github.com/Viren070/AIOStreams/commit/26d960127f16dfd5a2dfe5e57d364cddbfb83396))
* **sel:** update service list in whitelist and error message for `service()` ([#1043](https://github.com/Viren070/AIOStreams/issues/1043)) ([231a8cb](https://github.com/Viren070/AIOStreams/commit/231a8cbc0f632974770551215ff0b793011e25c1))
* **server:** add unhandled exception/rejection net ([9ee6afc](https://github.com/Viren070/AIOStreams/commit/9ee6afcf07379dc15acfc63ce131542b74671c9d))
* update link to docs ([c077dd1](https://github.com/Viren070/AIOStreams/commit/c077dd124e0043b59b4ed64cb21fa3aa01fbc9b0))
* use special header for ip forwarding ([8fa6cad](https://github.com/Viren070/AIOStreams/commit/8fa6cad1556fded7e5e231e387871a5d409244ab))
* **usenet/archive:** group obfuscated multi-volume archives with per-volume random base names ([d19e90a](https://github.com/Viren070/AIOStreams/commit/d19e90ad2cc599b2e65f2a6567e1e89e349f326c))
* **usenet/archive:** order RAR volumes by RAR5 header volume number, not filename ([f4919c2](https://github.com/Viren070/AIOStreams/commit/f4919c2868b447bd05039e36981c60dc0041957d))
* **usenet/nzb:** harden subject parsing ([06513a2](https://github.com/Viren070/AIOStreams/commit/06513a2898e51e224ada7e4491ea62ef474a4092))
* **usenet:** attribute archive-set missing-article failures to the actual failing volume ([82226ae](https://github.com/Viren070/AIOStreams/commit/82226aec239c7838e922797efa30b669fc5da35f))
* **usenet:** check plausibilty of yenc size ([892e25a](https://github.com/Viren070/AIOStreams/commit/892e25a38468af006333bf5d6f0b69aa70183b17))
* **usenet:** destroy live readers and drop warm sessions on engine close ([47ef36e](https://github.com/Viren070/AIOStreams/commit/47ef36ee98102486475a028b909db57d395c8bc5))
* **usenet:** fetch by message-id only, never send GROUP ([e5e1f82](https://github.com/Viren070/AIOStreams/commit/e5e1f824415a816826b6111492ed17e57e991e03))
* **usenet:** improve connection handling and connection/download stat display ([089aa47](https://github.com/Viren070/AIOStreams/commit/089aa478f6701f4ad42f9f1db2341d89304fe280))
* **usenet:** include password hmac in fingerprint ([bcf36cc](https://github.com/Viren070/AIOStreams/commit/bcf36cc53ac6e5f01e713aadced3d667ac58a4ec))
* **usenet:** invalidate warm engines on config change ([bcf36cc](https://github.com/Viren070/AIOStreams/commit/bcf36cc53ac6e5f01e713aadced3d667ac58a4ec))
* **usenet:** make archive crypt errors generic and use in sevenzip ([30e82d8](https://github.com/Viren070/AIOStreams/commit/30e82d86591107a375678d92eb9fc3b0d0459627))
* **usenet:** make error classification more robust ([bcf36cc](https://github.com/Viren070/AIOStreams/commit/bcf36cc53ac6e5f01e713aadced3d667ac58a4ec))
* **usenet:** measure latency separately ([958777f](https://github.com/Viren070/AIOStreams/commit/958777f674d02a93aa58bfda4f74705d0a3c8d05))
* **usenet:** measure only DATE command latency ([#1035](https://github.com/Viren070/AIOStreams/issues/1035)) ([37ff5f0](https://github.com/Viren070/AIOStreams/commit/37ff5f0b8c9ad6ea22ada1b1ba342652612b88b2))
* **usenet:** mint extension-less stream urls for cloudflare compatibility ([#1070](https://github.com/Viren070/AIOStreams/issues/1070)) ([d0cf369](https://github.com/Viren070/AIOStreams/commit/d0cf369e44ee755d575d2af3c9d7836055ef1801))
* **usenet:** prefer to size archive volumes by par2/part-grid ([b0f2473](https://github.com/Viren070/AIOStreams/commit/b0f2473b52d49036c0c78034ba485a830c8ccb95))
* **usenet:** prevent crashes from unhandled rejections and post-EOF stream errors ([9fe2b68](https://github.com/Viren070/AIOStreams/commit/9fe2b685d462ccf1351c26886831bcd1450e3b6f))
* **usenet:** recover from transient provider failures ([bcf36cc](https://github.com/Viren070/AIOStreams/commit/bcf36cc53ac6e5f01e713aadced3d667ac58a4ec))
* **usenet:** redesign provider speed test ([daddc7a](https://github.com/Viren070/AIOStreams/commit/daddc7a1b7df5a178bc787d7a5e01bb58c900c72))
* **usenet:** share the archive boundary-segment memo per VolumeSet ([4fd2e8f](https://github.com/Viren070/AIOStreams/commit/4fd2e8f6c1d6de50fd85626f76920e11c0d75b65))
* **usenet:** stop obfuscated split-7z inference from absorbing par2 sidecars ([1e98a8e](https://github.com/Viren070/AIOStreams/commit/1e98a8e5a92c19a8f52a3db919ca7ec2acec93a4))
* **usenet:** stream RAR5 -p encrypted splits with non-16-aligned volume fragments ([39464b2](https://github.com/Viren070/AIOStreams/commit/39464b2b80c82af2487f79650db5a387270243fa))
* **usenet:** throw on externally-aborted inspect ([705d66c](https://github.com/Viren070/AIOStreams/commit/705d66c516be28ff35cb60444b0ff366b2f9c95d))
* **usenet:** truncate rar passwords to 127 chars, cap archive passwords at 512 ([23d9f0c](https://github.com/Viren070/AIOStreams/commit/23d9f0c723cacea64be0344a062d16296fbe732c))
* **usenet:** use name from meta ([f809046](https://github.com/Viren070/AIOStreams/commit/f809046e2d3330fa2aaa4889c33b715c5dace88e))


### Performance Improvements

* **docker:** preload mimalloc ([cbee416](https://github.com/Viren070/AIOStreams/commit/cbee416f6b8960a4b8ec5b31b2ba85b912210a48))
* **usenet/nzb:** byte-level segment scanning and chunked hashing ([e546e8b](https://github.com/Viren070/AIOStreams/commit/e546e8b6367270d4990dceb8fff65dd3f9fff0ed))
* **usenet:** lean yEnc decode with pooled output buffers ([7aacb4b](https://github.com/Viren070/AIOStreams/commit/7aacb4bb9096bcce0b5cb8ed9df231af47963ed6))
* **usenet:** rework connection budget and make the segment cache disk-only ([cab8322](https://github.com/Viren070/AIOStreams/commit/cab832292c580eee4484f3475fd3041c33fafb27))
* **usenet:** scale archive windows with read-ahead and cancel stale queued downloads ([2735fb2](https://github.com/Viren070/AIOStreams/commit/2735fb217fef01840370fbc6de907661f961dcc3))
* **usenet:** suffix-anchor near-EOF reads for lazy split-RAR streams ([1a0c1b7](https://github.com/Viren070/AIOStreams/commit/1a0c1b735a38a7fbf9b8e01e573b28886f63c21e))
* **usenet:** zero-alloc onread NNTP read path ([01e3332](https://github.com/Viren070/AIOStreams/commit/01e333228c4fb77c7813719429363573b46af321))
* **usenet:** zero-alloc serve path with a pinned segment arena ([d9f6b9c](https://github.com/Viren070/AIOStreams/commit/d9f6b9ca4b8d2b4e7eb1b0611f94cb1f0a078956))


## v2.30.6-R3 (2026-07-14)

- No pull requests found for this version bump.
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


