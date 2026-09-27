# Changelog

## v2.35.0

## [2.35.0](https://github.com/Viren070/AIOStreams/compare/v2.34.1...v2.35.0) (2026-09-26)


### Features

* **anime-database:** answer many season and episode lookups from one read ([6c89dc0](https://github.com/Viren070/AIOStreams/commit/6c89dc063e6b50ddcfc6485ac96b44309360391b))
* **builtins:** add TsukiHime built-in addon ([#1293](https://github.com/Viren070/AIOStreams/issues/1293)) ([c33ea50](https://github.com/Viren070/AIOStreams/commit/c33ea50d928ed8af4c52ee052777dc69c8e8457f))
* **core:** add a cached autoplay attribute ([ae02dcd](https://github.com/Viren070/AIOStreams/commit/ae02dcdf231d99581b5d0da3cb468345a653ea3c))
* **core:** backfill probe data from RemuxDB ([#1244](https://github.com/Viren070/AIOStreams/issues/1244)) ([0a440cb](https://github.com/Viren070/AIOStreams/commit/0a440cb4f21759229cba46588acb369f63222c36))
* **core:** list and clear watch history ([d16ec82](https://github.com/Viren070/AIOStreams/commit/d16ec82ba9b83fb32ba7e9944b5856719e0ad733))
* **core:** tell whether a meta can be fetched ([057b3b1](https://github.com/Viren070/AIOStreams/commit/057b3b1eb1e7dfc75fa9fc7fb316bfa1633c0de6))
* **db:** make the PostgreSQL pool size configurable ([b8ecce7](https://github.com/Viren070/AIOStreams/commit/b8ecce70de58624e8eee5681822fd5cd7c34f48e))
* **db:** refuse a database migrated by a different build ([f28c6ac](https://github.com/Viren070/AIOStreams/commit/f28c6accc6017dc3591fab1844e55fe871216a17))
* **debrid:** carry StremThru's video hash through to streams ([c2800f1](https://github.com/Viren070/AIOStreams/commit/c2800f10c4fa1611418fa0b9ad6ed9667aba52ac))
* **desktop:** add a Windows shell with mpv under WebView2 ([d084d89](https://github.com/Viren070/AIOStreams/commit/d084d8984416a4c16b270b1b4e5799382006c637))
* **desktop:** draw the window's title bar in the page ([be6bb14](https://github.com/Viren070/AIOStreams/commit/be6bb141633e4f6fca8f6ebe8ba5a39930eb6b15))
* **desktop:** release the desktop app when its web app changes ([36fc7ff](https://github.com/Viren070/AIOStreams/commit/36fc7ff80839b23073c91560032b4c046fe6a45b))
* **desktop:** run on macOS ([fae9f8d](https://github.com/Viren070/AIOStreams/commit/fae9f8df8ea3339f361502e6c5b540ef75aa063e))
* **desktop:** serve the standalone web app ([bde9066](https://github.com/Viren070/AIOStreams/commit/bde9066a2cf2a4ed8fa31956cdbc458eccd33a51))
* **desktop:** show mpv's statistics overlay from the player ([9b7c4a8](https://github.com/Viren070/AIOStreams/commit/9b7c4a819914750452de16e0d530a30d8c32e684))
* **docs:** add a gallery component ([917f752](https://github.com/Viren070/AIOStreams/commit/917f7527026c02346ff987308493160beeac18cf))
* **failover:** add only-same-release failover toggle ([#1319](https://github.com/Viren070/AIOStreams/issues/1319)) ([3483fda](https://github.com/Viren070/AIOStreams/commit/3483fdadb2b2c110d6b1e69161a3672fd463f5ab))
* **filters:** add opt-in check to block results predating release/air date ([#1312](https://github.com/Viren070/AIOStreams/issues/1312)) ([50ad7ea](https://github.com/Viren070/AIOStreams/commit/50ad7ea1ba31a7eca9adcca3fd4e86e50ba172f4))
* **formatter:** add ::unique list modifier ([051a342](https://github.com/Viren070/AIOStreams/commit/051a342a00b44d056aac72a755b6ef4bab42f5a7))
* **formatter:** add `{stream.site}` ([1b2585a](https://github.com/Viren070/AIOStreams/commit/1b2585a32903a03ca4271b22b13473a0240ce96e))
* **formatter:** add audioTitles and subtitleTitles fields ([09152cd](https://github.com/Viren070/AIOStreams/commit/09152cdaf276eadb8757f37d589aee05ea6a0775))
* **formatter:** add audioTracks and subtitleTracks with where, pluck and each modifiers ([0ae7d3e](https://github.com/Viren070/AIOStreams/commit/0ae7d3ebb1746d51ba4d0d6433eb58bc4e4d24e9))
* **formatter:** add trim modifier ([79d64bb](https://github.com/Viren070/AIOStreams/commit/79d64bb3e3fcaa880773a041bea17acc3e77a9f7))
* **formatter:** add user lists and field references ([b9bc591](https://github.com/Viren070/AIOStreams/commit/b9bc591752803abc46a7c257e0903e7ac2bd16de))
* **formatter:** apply ::replace to lists ([57dbc55](https://github.com/Viren070/AIOStreams/commit/57dbc556424c21a7146cbee525924a69366293d0))
* **formatter:** edit audio and subtitle tracks in the preview ([0ae7d3e](https://github.com/Viren070/AIOStreams/commit/0ae7d3ebb1746d51ba4d0d6433eb58bc4e4d24e9))
* **formatter:** highlight and lint templates inside each() ([0ae7d3e](https://github.com/Viren070/AIOStreams/commit/0ae7d3ebb1746d51ba4d0d6433eb58bc4e4d24e9))
* **formatter:** raise template limit and budget the cache ([3c3363b](https://github.com/Viren070/AIOStreams/commit/3c3363b67bc66d7c4ef69f3863a2445e17885b42))
* **frontend:** add primer declaring instance limits to jellyfin modal ([35d0db5](https://github.com/Viren070/AIOStreams/commit/35d0db5ea8ebd118f1681192f65565b65b912da9))
* **frontend:** drop a show from its page ([8efd198](https://github.com/Viren070/AIOStreams/commit/8efd19809d1c7c682903d98e9217ec2fd2964640))
* **frontend:** link the desktop app on the Jellyfin Connect tab ([bbafbb4](https://github.com/Viren070/AIOStreams/commit/bbafbb4b355da2cb948006286341bb3d9d89f29c))
* **frontend:** restore home row positions on back ([01a4a53](https://github.com/Viren070/AIOStreams/commit/01a4a53c406fcc02b49daa4be452feafa140b319))
* **frontend:** review unsaved drafts before restoring ([096dcaf](https://github.com/Viren070/AIOStreams/commit/096dcaf2cf52c0e78dff06ca85e1f74680cea902))
* **frontend:** set up Jellyfin from the save and install page ([1564a4c](https://github.com/Viren070/AIOStreams/commit/1564a4ca0dd32d566b8813797d2b1739001274a0))
* **frontend:** show enabled segment providers in UI ([1342ab8](https://github.com/Viren070/AIOStreams/commit/1342ab8510ab8489d2a946628b42be07fc2a9318))
* **frontend:** show max versions in primer ([a470d94](https://github.com/Viren070/AIOStreams/commit/a470d94163341e19d0ca39291bafa31db173c918))
* **frontend:** show notice titles, kinds and links in the version picker ([98772f6](https://github.com/Viren070/AIOStreams/commit/98772f647a63368b800e11d80eed8d249076a72d))
* **frontend:** sign in with the password on jellyfin picker addresses ([95e656d](https://github.com/Viren070/AIOStreams/commit/95e656d339b99013e585eb870769b09ebe7672eb))
* **jellyfin-web:** add a hero that follows the selected card ([4c7f50d](https://github.com/Viren070/AIOStreams/commit/4c7f50d986f3a0ab32b4ad5e1002df1390ed6e42))
* **jellyfin-web:** add a season menu and drop the season watched button ([1329dfe](https://github.com/Viren070/AIOStreams/commit/1329dfe49e0720a5f4a7c9c214a5c2e9c7282b95))
* **jellyfin-web:** add a setting to merge continue watching and next up ([8b97546](https://github.com/Viren070/AIOStreams/commit/8b975461a348135d15429f38fb00928948a0cb65))
* **jellyfin-web:** add a settings page ([feb8517](https://github.com/Viren070/AIOStreams/commit/feb8517d45ba5c8de841e7c5a03d9297cd8c174a))
* **jellyfin-web:** add a standalone build that picks its server ([c0ab405](https://github.com/Viren070/AIOStreams/commit/c0ab405fab73f41417ec87494d0ad6c8b57b5711))
* **jellyfin-web:** add chapters to the desktop app's player ([456a621](https://github.com/Viren070/AIOStreams/commit/456a6217c4f522e520e1ce6d8b306f6f492bab2e))
* **jellyfin-web:** add data-ui selectors across the app ([7e2022f](https://github.com/Viren070/AIOStreams/commit/7e2022f7abde3e75850e0c75a607cee52d4c5890))
* **jellyfin-web:** add previous and next episode to the player ([a738260](https://github.com/Viren070/AIOStreams/commit/a73826070a0971b7824bb36e102098b733a8d91f))
* **jellyfin-web:** add the desktop app as a playback host ([5561530](https://github.com/Viren070/AIOStreams/commit/5561530cf612657967daef7d1c5a2fe094ebb696))
* **jellyfin-web:** add themes and custom CSS ([d14e276](https://github.com/Viren070/AIOStreams/commit/d14e2767241b0526f003faaa9b54de2c31c655f6))
* **jellyfin-web:** cap how wide hero and title backdrops get ([485b52b](https://github.com/Viren070/AIOStreams/commit/485b52bc75afa379a197d4355e81954ee11e036e))
* **jellyfin-web:** confirm before removing a saved server ([f5301d3](https://github.com/Viren070/AIOStreams/commit/f5301d3c626a1d908f8e38eb7a345af29d85a930))
* **jellyfin-web:** fit, crop or stretch the picture ([df8838f](https://github.com/Viren070/AIOStreams/commit/df8838f29182b5a03e50ee134c1aea38bd8db6a1))
* **jellyfin-web:** flash seeks on the side they skip to ([042065a](https://github.com/Viren070/AIOStreams/commit/042065a72280987507970230f4b31e8653760ca6))
* **jellyfin-web:** hide the browser's right-click menu in the desktop app and the player ([8279bf8](https://github.com/Viren070/AIOStreams/commit/8279bf809858bc4d9b8ba74a563b0f832f196f32))
* **jellyfin-web:** keep a search history per user ([62b344d](https://github.com/Viren070/AIOStreams/commit/62b344dd0b685494b335308a249f3027de2ceda9))
* **jellyfin-web:** let the latest episode button press win ([e4f12dc](https://github.com/Viren070/AIOStreams/commit/e4f12dcb379de9ae0a80b241a5b9a4e0c8cb6b2a))
* **jellyfin-web:** list a picker address's users at sign-in ([49dd070](https://github.com/Viren070/AIOStreams/commit/49dd070ce4d2912284d5d0eea8589c2c645a7e75))
* **jellyfin-web:** mark watched up to an episode on any server ([8bd314b](https://github.com/Viren070/AIOStreams/commit/8bd314b3284bef4d9f5a9f6386f18b8cd3ad0524))
* **jellyfin-web:** move account actions from the sidebar into an avatar menu ([1582c65](https://github.com/Viren070/AIOStreams/commit/1582c65351cf66f275d11a06087eeb8640e24dc4))
* **jellyfin-web:** move row arrows off the artwork into the row's header ([eaea9c1](https://github.com/Viren070/AIOStreams/commit/eaea9c192b1bb9a596ffa17fea5f024d227ae084))
* **jellyfin-web:** offer next up as a featured source ([53bdc0d](https://github.com/Viren070/AIOStreams/commit/53bdc0d3986af55b64f21ce8f23fb9b74a3b8123))
* **jellyfin-web:** offer the next episode near the end ([75342eb](https://github.com/Viren070/AIOStreams/commit/75342eb5b749fff7ef44c5183368c51608e5c029))
* **jellyfin-web:** open the desktop app's logs and copy diagnostics from settings ([a729d0b](https://github.com/Viren070/AIOStreams/commit/a729d0bc2c6223854719ddd9f46afe267b2d607b))
* **jellyfin-web:** play the first version on by default when none matches ([f89518f](https://github.com/Viren070/AIOStreams/commit/f89518f7537c493de2c1b05798f33954819f6b46))
* **jellyfin-web:** point browsers to the desktop app ([eff3d03](https://github.com/Viren070/AIOStreams/commit/eff3d036fcba3bf0d238e16d5ee2d61720a6a601))
* **jellyfin-web:** resume straight into the last-played version ([036c434](https://github.com/Viren070/AIOStreams/commit/036c434c6ebce2bd073c1ac997358d9e2524b778))
* **jellyfin-web:** scroll player menu lists on their own, keeping subtitle sync in view ([4c2e491](https://github.com/Viren070/AIOStreams/commit/4c2e4914a3ce506d47cac5b5dcc04afcf36e8c48))
* **jellyfin-web:** show a notice while another episode's versions load ([76d358b](https://github.com/Viren070/AIOStreams/commit/76d358b95aec3a8538b2d8665b5a86ffd8d14e06))
* **jellyfin-web:** show desktop app updates and switch their channel ([7831b0a](https://github.com/Viren070/AIOStreams/commit/7831b0a8e324e79907a4cee71856a206ef976554))
* **jellyfin-web:** show sub-collections on a collection's page ([c50f123](https://github.com/Viren070/AIOStreams/commit/c50f123e89b423c69796b20ee2155895c65b48d0))
* **jellyfin-web:** show the show's logo for episodes in the hero ([e192573](https://github.com/Viren070/AIOStreams/commit/e192573d724516564ae2d220d833092d6ce1385e))
* **jellyfin-web:** show the signed-in user's own activity on any server ([278d3e0](https://github.com/Viren070/AIOStreams/commit/278d3e097917fd2a42c3d277d7845b850d3de127))
* **jellyfin-web:** sign in as AIOStreams Desktop on the computer's name in the desktop app ([08daa97](https://github.com/Viren070/AIOStreams/commit/08daa974f4f8c503b0671be7a61017873cb95965))
* **jellyfin-web:** sign in with Quick Connect ([170adac](https://github.com/Viren070/AIOStreams/commit/170adac01a3e954dee2a5f56425ab6b6077aaa3f))
* **jellyfin-web:** skip by the file's chapters in the desktop app ([3bd7ec4](https://github.com/Viren070/AIOStreams/commit/3bd7ec4f6057e06c10394f9986b420cf2a76042e))
* **jellyfin-web:** split search results into movie and show rows ([cc9d024](https://github.com/Viren070/AIOStreams/commit/cc9d0247dec8526e85989cc4273de4f253430a32))
* **jellyfin-web:** start pages at the rail and run rows to the edge ([a062be3](https://github.com/Viren070/AIOStreams/commit/a062be362ac83482a83bbb965f2ca810db625f87))
* **jellyfin-web:** sync subtitles and switch versions in the player ([2c75b60](https://github.com/Viren070/AIOStreams/commit/2c75b60a6d809e96fb012d275f8858ce4cde5c1a))
* **jellyfin-web:** sync subtitles by tapping when a line is heard and when it shows ([1d7c6fa](https://github.com/Viren070/AIOStreams/commit/1d7c6fac322168f1238e1ca70fd2eec5adc0968e))
* **jellyfin-web:** work with any Jellyfin server ([da200a0](https://github.com/Viren070/AIOStreams/commit/da200a03e14c4d228ec21113034d99378d390ba0))
* **jellyfin/segments:** add PMDB provider ([1342ab8](https://github.com/Viren070/AIOStreams/commit/1342ab8510ab8489d2a946628b42be07fc2a9318))
* **jellyfin/segments:** answer once the requested marker types are decided ([4edf5c9](https://github.com/Viren070/AIOStreams/commit/4edf5c976b256f387519d8b885553b45bcb0f490))
* **jellyfin/segments:** implement MediaSegments for intros, recaps and credits from IntroDB, AniSkip and Anime-Skip ([5786b1a](https://github.com/Viren070/AIOStreams/commit/5786b1a4ed4a47665beae4eb496c536327940348))
* **jellyfin/segments:** resolve IMDb ids for TMDB-keyed movies ([b107a10](https://github.com/Viren070/AIOStreams/commit/b107a108d78dc4f813d942541559f35b86fee312))
* **jellyfin/segments:** share identical provider lookups between concurrent requests ([4edf5c9](https://github.com/Viren070/AIOStreams/commit/4edf5c976b256f387519d8b885553b45bcb0f490))
* **jellyfin/segments:** support movie end credits from IntroDB ([5ef9d51](https://github.com/Viren070/AIOStreams/commit/5ef9d5160017aa4ccbf8d84aa774616593d3667c))
* **jellyfin:** add a mark watched up to here episode action ([ea7f171](https://github.com/Viren070/AIOStreams/commit/ea7f171d17fa85fbefe72ce33a515c51f102659d))
* **jellyfin:** add a short sign-in picker address from a configuration's alias ([1b7146a](https://github.com/Viren070/AIOStreams/commit/1b7146a31aca484ecde0b31cd751de8e84508e7a))
* **jellyfin:** add a versions feature for the aiostreams version object ([c79220d](https://github.com/Viren070/AIOStreams/commit/c79220dcd0f2cf8a9ca81baf9935e1a69b5a1949))
* **jellyfin:** add a web app at /web ([5c116c4](https://github.com/Viren070/AIOStreams/commit/5c116c49ffc3e697fa596f89c0d2cffd14e68f90))
* **jellyfin:** add api keys ([5a95a5f](https://github.com/Viren070/AIOStreams/commit/5a95a5fbfd4669f3d220b6d4c9a12f87363b26df))
* **jellyfin:** add library limit and search catalog concurrency limit ([022d5bf](https://github.com/Viren070/AIOStreams/commit/022d5bf72b9a36e33b9eed9577b372254e704f15))
* **jellyfin:** add row and list episode layouts ([6d0b7d1](https://github.com/Viren070/AIOStreams/commit/6d0b7d1f9cc3223f1882b971003e351021d60ea4))
* **jellyfin:** choose trackers per user ([b960e8d](https://github.com/Viren070/AIOStreams/commit/b960e8d0eb1b1edfa6fd00504fb3ea5d995e9c3d))
* **jellyfin:** decide playable entries before a sweep lands ([1ad2f1f](https://github.com/Viren070/AIOStreams/commit/1ad2f1f0f158e2a109721bc47d08f03a245e6a4f))
* **jellyfin:** derive version ids from the release instead of its position ([b865b1a](https://github.com/Viren070/AIOStreams/commit/b865b1a17e530edf5018b56df87002d6bbe78bec))
* **jellyfin:** draw the web app edge to edge ([7a1853b](https://github.com/Viren070/AIOStreams/commit/7a1853b4eed1955a13db5498042353ce469c35e5))
* **jellyfin:** enable skip markers by default ([2001105](https://github.com/Viren070/AIOStreams/commit/2001105e6ce3e99e5005221fbc86dd86c8d96356))
* **jellyfin:** enable the api and watch state by default ([cc82343](https://github.com/Viren070/AIOStreams/commit/cc82343ae42db342cb8a4c2f5e25f01b592db382))
* **jellyfin:** enrich external subtitle tracks ([0f5ad0d](https://github.com/Viren070/AIOStreams/commit/0f5ad0d580933b511aca73f8ad30a5c20681ac76))
* **jellyfin:** fall back through item backdrops to a poster wash ([61bf600](https://github.com/Viren070/AIOStreams/commit/61bf6003e605b21f9a04173d692b098a51e21ae1))
* **jellyfin:** give the web app each version's own id in PlaybackInfo ([42b6722](https://github.com/Viren070/AIOStreams/commit/42b67228e53a62f8746467de270394a4d659440a))
* **jellyfin:** let one configuration sign in as several users ([76f8be1](https://github.com/Viren070/AIOStreams/commit/76f8be1910eee7c11789f19e6f4298a747f0c51e))
* **jellyfin:** list numbered tracks from known languages ([43bc30e](https://github.com/Viren070/AIOStreams/commit/43bc30ea66342b747f0bb4b867175548af1dadbf))
* **jellyfin:** list playing sessions in /Sessions ([eb3a182](https://github.com/Viren070/AIOStreams/commit/eb3a18284909ad552bc81fbb0e03d62371e614b7)), closes [#1327](https://github.com/Viren070/AIOStreams/issues/1327)
* **jellyfin:** list the server's extensions and honour GenreIds in a library ([414a0e7](https://github.com/Viren070/AIOStreams/commit/414a0e7c08007e3f5b5035ddb40bc0021343349d))
* **jellyfin:** mark channel sources live ([58a7929](https://github.com/Viren070/AIOStreams/commit/58a7929774fa1273095ff442b3b604a16609fbf0))
* **jellyfin:** open clamped overviews from a More button ([6c828f9](https://github.com/Viren070/AIOStreams/commit/6c828f900374c6ee1164aaa028887ed955d83b3b))
* **jellyfin:** pass external notice links to clients ([f3fc09c](https://github.com/Viren070/AIOStreams/commit/f3fc09c2ff56bd90e967a938bb8c8febe451e893))
* **jellyfin:** person details and filmography from TMDB ([85af525](https://github.com/Viren070/AIOStreams/commit/85af525c57012d42142d964c64046a4f9fcb98e1))
* **jellyfin:** PINs for users ([90f1a24](https://github.com/Viren070/AIOStreams/commit/90f1a24c87754c6e7a5765189d26a90a60370cf9))
* **jellyfin:** play entries that have nothing to open ([4aba386](https://github.com/Viren070/AIOStreams/commit/4aba386bcc775e8c28a6e6ebaa1800d13bc9e10a))
* **jellyfin:** read extended meta fields ([11b257c](https://github.com/Viren070/AIOStreams/commit/11b257c1357efb4edc6a0b48e92382a37b526e8e))
* **jellyfin:** recommend similar titles from TMDB ([798cdbe](https://github.com/Viren070/AIOStreams/commit/798cdbe630542d251529128b1347f30fd146282c))
* **jellyfin:** report hearing impaired, original and other track flags on media streams ([fdb324f](https://github.com/Viren070/AIOStreams/commit/fdb324f464e7ee440ce4b5b68ddfa3e4b0d89bf3))
* **jellyfin:** report playback and watched marks to watch-state addons ([d1c1b1b](https://github.com/Viren070/AIOStreams/commit/d1c1b1b80ee034faf0638e940f244064a4d612fb))
* **jellyfin:** require the password on picker addresses and aliases ([8c990f0](https://github.com/Viren070/AIOStreams/commit/8c990f0ae0f55203956208d6f2c50f8019d06088))
* **jellyfin:** send each version's binge group ([59d9a90](https://github.com/Viren070/AIOStreams/commit/59d9a90bf1647999e088610bb17e9ad33bf23eba))
* **jellyfin:** send the configure page's address in the public server info ([eaefbb9](https://github.com/Viren070/AIOStreams/commit/eaefbb91a5431c7000d814cdbf821574670f723b))
* **jellyfin:** send undropped when a play picks a dropped show back up ([8ecd577](https://github.com/Viren070/AIOStreams/commit/8ecd5773919a25937a6e57585574371b92ca2328))
* **jellyfin:** serve a Jellyfin-compatible API so Jellyfin clients can browse and play ([dd8ea9c](https://github.com/Viren070/AIOStreams/commit/dd8ea9c36bd6853a3661669940350bbbaeb341c5))
* **jellyfin:** serve collections of any title type ([6be31e0](https://github.com/Viren070/AIOStreams/commit/6be31e077fe5b06bcc327709d06f79df9ff3054f))
* **jellyfin:** serve the web app with its own PWA manifest ([b508b2e](https://github.com/Viren070/AIOStreams/commit/b508b2eb411a8558d7545bea5bae31f02b141d65))
* **jellyfin:** show addon notices, errors and statistics as versions ([c998327](https://github.com/Viren070/AIOStreams/commit/c998327e8889290f2a9fd9e8957f49d3909b0ede))
* **jellyfin:** show watch-state trackers from the configuration in a Trackers tab ([e09a055](https://github.com/Viren070/AIOStreams/commit/e09a055ec0933ad58b1395475bedf82b60d81a83))
* **jellyfin:** sign in with a PIN alone on the picker address ([53df916](https://github.com/Viren070/AIOStreams/commit/53df9160eb7ce60cfce33e081107b87cfbd520cc))
* **jellyfin:** store users' playback preferences ([24db694](https://github.com/Viren070/AIOStreams/commit/24db694d7ae4cb6f25abaaef1a17dd45bf83d126))
* **linked-accounts:** make the per-user link limit configurable ([cf80bb0](https://github.com/Viren070/AIOStreams/commit/cf80bb0c156aacd63509cadfa056765a7260cdf6))
* **media-info:** keep each probed audio and subtitle track ([14ac79c](https://github.com/Viren070/AIOStreams/commit/14ac79cdc1839f063b99bd7fc309d8ed20070f7e))
* **media-info:** parse commentary, dub, original and accessibility flags on audio and subtitle tracks ([fdb324f](https://github.com/Viren070/AIOStreams/commit/fdb324f464e7ee440ce4b5b68ddfa3e4b0d89bf3))
* **parser:** ignore repost suffixes when parsing names ([1563000](https://github.com/Viren070/AIOStreams/commit/15630004b80a8f3acb7d16e7f5ee0ecc261c70c5))
* **parser:** update parse-torrent-title to 0.9.0 ([6a88d69](https://github.com/Viren070/AIOStreams/commit/6a88d69b6f35485d05fa82887365994b44f141ed))
* **presets/bitmagnet:** expose search mode option ([b1c145a](https://github.com/Viren070/AIOStreams/commit/b1c145a5ce2e02e1601c54dafbec78fc980bee78)), closes [#1322](https://github.com/Viren070/AIOStreams/issues/1322)
* **presets/newznab:** add SquareEyed indexer ([#1350](https://github.com/Viren070/AIOStreams/issues/1350)) ([6d37fe3](https://github.com/Viren070/AIOStreams/commit/6d37fe32ee467fc42e96aad7e082b95b86f95d2c))
* **presets:** add penguplay preset ([ff01f94](https://github.com/Viren070/AIOStreams/commit/ff01f94a0730443848938f967409700833e2ec2d))
* **ratelimit:** let a route spend a limiter token without failing the request ([dd8ea9c](https://github.com/Viren070/AIOStreams/commit/dd8ea9c36bd6853a3661669940350bbbaeb341c5))
* **release-blocklist:** add a master enable/disable toggle ([#1330](https://github.com/Viren070/AIOStreams/issues/1330)) ([3d7c536](https://github.com/Viren070/AIOStreams/commit/3d7c536157829ba949658679c2e22fcc29f6b6ec))
* remember config sign-ins by default ([1e405f4](https://github.com/Viren070/AIOStreams/commit/1e405f4f8170c2e04b7a1c13c286136e85c15803))
* **schemas:** add native epg fields ([e6daf4a](https://github.com/Viren070/AIOStreams/commit/e6daf4a8c99360bb0249b86cf9d484b973c3e827))
* **sel:** add audioTitle() and subtitleTitle() filters ([ec2ec03](https://github.com/Viren070/AIOStreams/commit/ec2ec032e71fb67c02c25f8f8f9cf13913cc302e))
* **sel:** add audioTrack() and subtitleTrack() filters ([0ae7d3e](https://github.com/Viren070/AIOStreams/commit/0ae7d3ebb1746d51ba4d0d6433eb58bc4e4d24e9))
* **sel:** add editions(), network(), container() and extension() filters ([0ae7d3e](https://github.com/Viren070/AIOStreams/commit/0ae7d3ebb1746d51ba4d0d6433eb58bc4e4d24e9))
* **settings:** add an orderable multi-select field ([2f2e1f0](https://github.com/Viren070/AIOStreams/commit/2f2e1f09711164d8c73b9f562380c597fd87c89c))
* **settings:** add Jellyfin and Watch State tabs ([bfce5d1](https://github.com/Viren070/AIOStreams/commit/bfce5d1fcd07be4fedcef1932aba7d485a4f97fb))
* show the server's build in About and diagnostics ([c08e496](https://github.com/Viren070/AIOStreams/commit/c08e49601204640b5c870cec8c18b6e250d79c71))
* **ui:** add a colour input ([4cffffe](https://github.com/Viren070/AIOStreams/commit/4cffffe8d4f4f006627c82e3ee6591edc29d95d4))
* **ui:** allow the tab indicator animation to be turned off ([1780c48](https://github.com/Viren070/AIOStreams/commit/1780c4874dbac4148015e6a5423c8159009d3f06))
* **variants:** add an insert instruction for list positions ([022b0e1](https://github.com/Viren070/AIOStreams/commit/022b0e1488799a3758c2b10b6b630837b257cd21))
* **variants:** let [*] walk an object's values ([5afa43c](https://github.com/Viren070/AIOStreams/commit/5afa43cd58fadca8cdfb0397ee01ab25dee7b43e))
* **watch-state:** add the watch_state addon resource ([02d1d4e](https://github.com/Viren070/AIOStreams/commit/02d1d4e673ea0bd204ceb173281b7f8ebbcbb03a))
* **watch-state:** hide and report dropped shows ([1dfeaaa](https://github.com/Viren070/AIOStreams/commit/1dfeaaac76903a224f21ae287c8b5b8dce548904))
* **watch-state:** record watch state and playback sessions ([67c9791](https://github.com/Viren070/AIOStreams/commit/67c97914362cfde2b3f5a9cb9a2cc7dd7cd33c7a))
* **watch-state:** sync addon watchlists with favourites ([9a58fb2](https://github.com/Viren070/AIOStreams/commit/9a58fb2fae56f4aa32c58dd8be0bfb822836ef34))
* **watch-state:** sync playback and watch history with addons that declare watch_state ([60aa8b6](https://github.com/Viren070/AIOStreams/commit/60aa8b6b8891cfef8ef7ae40c8860cde792155bd))


### Bug Fixes

* allow any resource string ([64f9e21](https://github.com/Viren070/AIOStreams/commit/64f9e21b9194e605fa10653e92d9e3162bf9595d))
* **anime-database:** preserve IMDb identity for episode mappings ([#1301](https://github.com/Viren070/AIOStreams/issues/1301)) ([e2224d9](https://github.com/Viren070/AIOStreams/commit/e2224d9aa1bcf22bb9e839e1b096017db2a6d656))
* **anime:** match releases numbered in tvdb's season ([5d319f5](https://github.com/Viren070/AIOStreams/commit/5d319f5b588124b28c969e5c2058c34f9092951f))
* **anime:** scope imdb hints and fix episode mapping ([cdaee68](https://github.com/Viren070/AIOStreams/commit/cdaee68dbf5f6bb3bc384dfceff1134d6747411f))
* **api:** refuse encrypted passwords on the jellyfin routes ([f1b78df](https://github.com/Viren070/AIOStreams/commit/f1b78df3246cd1c64e9f7ac5c783e0214f568cdc))
* **builtins/easynews-search:** preserve season and episode separators ([#1284](https://github.com/Viren070/AIOStreams/issues/1284)) ([3686c3d](https://github.com/Viren070/AIOStreams/commit/3686c3d2a07936f09e8cc704b8eae40192e73320))
* **builtins/library:** escape item ids ([f8f3f83](https://github.com/Viren070/AIOStreams/commit/f8f3f8342045906e42104bdb0780624e0391102e))
* **builtins:** compute torrent age from pubDate for torznab/prowlarr ([#1306](https://github.com/Viren070/AIOStreams/issues/1306)) ([f1daac3](https://github.com/Viren070/AIOStreams/commit/f1daac30440f5ae37a9b82f5f458419e539e10ba))
* **builtins:** preserve zero seeder counts ([#1320](https://github.com/Viren070/AIOStreams/issues/1320)) ([23c7749](https://github.com/Viren070/AIOStreams/commit/23c774990216f3345d3caa8fa280851a4cdacdda))
* **cache:** make a forced write wait for a flush already in progress ([3feb117](https://github.com/Viren070/AIOStreams/commit/3feb11774971cf14e262a98fc4aee438eae22f64))
* **cache:** retry redis writes from a failed flush instead of dropping them ([f3ddb83](https://github.com/Viren070/AIOStreams/commit/f3ddb83ad8611e5033bfa6c224e92f3823921bc7))
* **cache:** slide TTLs on the Redis and SQL backends ([3feb117](https://github.com/Viren070/AIOStreams/commit/3feb11774971cf14e262a98fc4aee438eae22f64))
* **config:** use `byteSize` schema for max pull response bytes ([64ff9ba](https://github.com/Viren070/AIOStreams/commit/64ff9ba8ab6c9f647a494bca2d3325da23e30eb8))
* **core/sync:** log each fetch failure once ([4a5d387](https://github.com/Viren070/AIOStreams/commit/4a5d387be6eb7ba44216f22e65ad326a4c3a0f84))
* **core/sync:** make the vouched URL list the refresh set ([a6554f2](https://github.com/Viren070/AIOStreams/commit/a6554f22eaace70e32dd304d4c3241e418642337))
* **core/sync:** stop refetching every URL on allowlist changes ([e293f11](https://github.com/Viren070/AIOStreams/commit/e293f1175d4ef155f79514ba3ed14935e54ce89b))
* **core:** make trailer source and type optional ([19d7c12](https://github.com/Viren070/AIOStreams/commit/19d7c1294fc2fec70755a4e5864485eb67793ab5))
* **core:** repair garbled startup warning ([f8c6db9](https://github.com/Viren070/AIOStreams/commit/f8c6db973eebfc3b7e2fc94cea1a726752751903))
* **core:** revive DOMException from the lock cache ([105d9de](https://github.com/Viren070/AIOStreams/commit/105d9de813f528df841529851dbbbec8d72f45e9))
* **debrid/torbox:** align timeoutMs with stremthru ([#1281](https://github.com/Viren070/AIOStreams/issues/1281)) ([0ddf328](https://github.com/Viren070/AIOStreams/commit/0ddf328bb63d21805832cc2f4deec3b347838925))
* **debrid:** count an account item as cached only when the service says so ([bc4acbf](https://github.com/Viren070/AIOStreams/commit/bc4acbf70c3c558cc9a2f42fa801b6d312b008bd))
* **dedup:** take languages and tracks from a probed source instead of merging them ([e5b5182](https://github.com/Viren070/AIOStreams/commit/e5b51820805fe03263abf2e5b1c1753e20d391be))
* **distributed-lock:** release redis locks before publishing ([668aa4d](https://github.com/Viren070/AIOStreams/commit/668aa4d8284a70188a8642a92f4791a4f75a3966))
* **distributed-lock:** run the work when the holder finishes before a waiter subscribes ([7afe512](https://github.com/Viren070/AIOStreams/commit/7afe5122e105a17a7519b878b460718702b58223))
* **docs:** version changelog preview image links by their content ([876a481](https://github.com/Viren070/AIOStreams/commit/876a48125506975b49ae118ff84ef2c4535868f0))
* **filters:** route digital-release rejections by which rule matched ([#1333](https://github.com/Viren070/AIOStreams/issues/1333)) ([b767cd4](https://github.com/Viren070/AIOStreams/commit/b767cd41c0a96f98a3f4d2bb7b4bf50830bebeb9))
* **filters:** run the digital release check once per request ([168a94f](https://github.com/Viren070/AIOStreams/commit/168a94fc0b29291c8103055740c1516a4abeea34))
* **filters:** stop forcing the digital-release info stream for single stale results ([#1328](https://github.com/Viren070/AIOStreams/issues/1328)) ([0c9f895](https://github.com/Viren070/AIOStreams/commit/0c9f895c3844abe8fc4acca3aceb7eced97c8fd2))
* **formatter:** stop the formatter browser's tab indicator replaying ([4ebb7ce](https://github.com/Viren070/AIOStreams/commit/4ebb7ce945506648e3ca198a62f996f0cdc45333))
* **frontend:** add no-referrer for addon logos ([#1347](https://github.com/Viren070/AIOStreams/issues/1347)) ([1c60ba4](https://github.com/Viren070/AIOStreams/commit/1c60ba4385398a8e214254d0f3918367bc423c45))
* **frontend:** anchor popped sign-in views to the screen ([22575a1](https://github.com/Viren070/AIOStreams/commit/22575a170f5b62425de2e8ca26c1e555b6597ff0))
* **frontend:** blur the focused field on bottom nav taps ([28b0242](https://github.com/Viren070/AIOStreams/commit/28b0242624a92192cb604c5a2323aee883c2f6c3))
* **frontend:** clarify digital release filter description scope ([#1310](https://github.com/Viren070/AIOStreams/issues/1310)) ([346e8e0](https://github.com/Viren070/AIOStreams/commit/346e8e0dbb7b271c50b19d29d5519b5b2586b277))
* **frontend:** disable desktop subtitles with track 0 instead of -1 ([37be686](https://github.com/Viren070/AIOStreams/commit/37be68628f6d96b971f05737f6df3116ee415606))
* **frontend:** end the version picker's art at the list ([b644af6](https://github.com/Viren070/AIOStreams/commit/b644af6d529ab62a965da3f6c777bc6af9c71eef))
* **frontend:** keep context menus on screen ([46150fb](https://github.com/Viren070/AIOStreams/commit/46150fb4daf15423d0f3759dd26ec7446d107524))
* **frontend:** keep loaded configs' values when status arrives late ([9fd6c67](https://github.com/Viren070/AIOStreams/commit/9fd6c671ad150df8c09275e9e9de9dfb7418915f))
* **frontend:** keep the Profile card of a saved configuration after a reload ([d76e44d](https://github.com/Viren070/AIOStreams/commit/d76e44db7b0cf8a28dfed23884d4176d8903c093))
* **frontend:** mark the web app search box as a search input ([510a2b0](https://github.com/Viren070/AIOStreams/commit/510a2b094c5c7daefcc8990824a26bbacecc1013))
* **frontend:** only report value changes the user made ([f597c79](https://github.com/Viren070/AIOStreams/commit/f597c79bd390627281f7c7f14b1c1cdacdbf02ca))
* **frontend:** only select text meant to be copied in the web app ([48c8064](https://github.com/Viren070/AIOStreams/commit/48c8064ec1b7c871fa5ad36159f864c9f0d846a6))
* **frontend:** re-check drafts on save and compare them with the review diff ([1442fc5](https://github.com/Viren070/AIOStreams/commit/1442fc58add0a0ac9f6a8f58ebad84ae8adc877a))
* **frontend:** render the season pill check as a right icon ([55ae08e](https://github.com/Viren070/AIOStreams/commit/55ae08e9dd28c0ba8152a520242c70ea789adccf))
* **frontend:** size the version picker art by width ([04166b8](https://github.com/Viren070/AIOStreams/commit/04166b8abce48124d7d5b6b9245b0a65909d34af))
* **frontend:** stop animating diff viewer tabs ([819470c](https://github.com/Viren070/AIOStreams/commit/819470c1c929ceceac6c00b16f8a101eb00c4f93))
* **frontend:** stop clipboard copies hanging in embedded browsers ([df0a3fe](https://github.com/Viren070/AIOStreams/commit/df0a3fe5e7c923a0169e742b0cf1def76ad7c50e))
* **frontend:** try the next image when a card's fails to load ([07415a3](https://github.com/Viren070/AIOStreams/commit/07415a394fd3122f00edc884e59b92d6871971aa))
* **http:** back off on 429 using Retry-After ([#1292](https://github.com/Viren070/AIOStreams/issues/1292)) ([f48573d](https://github.com/Viren070/AIOStreams/commit/f48573dbef045002933c5042efd70e76d73c6911))
* ignore desktop-nightly when finding the latest server nightly ([dc7d470](https://github.com/Viren070/AIOStreams/commit/dc7d47097cfd42ffaec13c0b0928097bf2c46dad))
* **jellyfin-web:** ask the server again for a version picked from the list ([84451ee](https://github.com/Viren070/AIOStreams/commit/84451ee4a2f8eeb2489d111fa26ab904840ba38d))
* **jellyfin-web:** clamp overviews by height instead of line-clamp ([a99e6fb](https://github.com/Viren070/AIOStreams/commit/a99e6fb8a3a5d498d975874c937538a34f2abcf9))
* **jellyfin-web:** clear the episode lookup notice when it resolves at once ([c3a3cd0](https://github.com/Viren070/AIOStreams/commit/c3a3cd0b95b9e292ca8f612ffec627653314399e))
* **jellyfin-web:** define NEXT_PUBLIC_PLATFORM for the ui kit ([95a39f0](https://github.com/Viren070/AIOStreams/commit/95a39f079391d804ab71654d6f9365513ff6834e))
* **jellyfin-web:** drop the scroll lock's scrollbar margin ([f6465ae](https://github.com/Viren070/AIOStreams/commit/f6465ae79500df1a22dee16057dccf1d0d07b4bb))
* **jellyfin-web:** handle undated plays and servers that ignore the played filter ([e2016eb](https://github.com/Viren070/AIOStreams/commit/e2016ebdd2966e1486a34cd73a9698c00092ca1a))
* **jellyfin-web:** hide empty catalog rows' placeholders ([bf394e7](https://github.com/Viren070/AIOStreams/commit/bf394e796b86b3f03de189484ec0da2f9e16188b))
* **jellyfin-web:** keep a subtitle URL's query when asking for WebVTT ([ee6aa0e](https://github.com/Viren070/AIOStreams/commit/ee6aa0ee64fc7fbd60495a366fb6d5e7ddb5fc5d))
* **jellyfin-web:** keep sticky parts in place while a menu locks scrolling ([aaa0cfb](https://github.com/Viren070/AIOStreams/commit/aaa0cfbdfb65a7886a18c5d0ac140d144ad71ea5))
* **jellyfin-web:** keep the page scrollbar on the server screens too ([c69dcc9](https://github.com/Viren070/AIOStreams/commit/c69dcc94ceb13b79e61464bb12a84b3b1aa8fe5e))
* **jellyfin-web:** let filter tabs scroll on narrow screens ([c54bab0](https://github.com/Viren070/AIOStreams/commit/c54bab02a3029d7575678a5bbfd777b889283144))
* **jellyfin-web:** offer syncing to a line only for subtitles the player can read ([1d4efb6](https://github.com/Viren070/AIOStreams/commit/1d4efb6778a51b397b9c6a1012f843d98fcaa29b))
* **jellyfin-web:** scroll a new page before its first paint ([9854832](https://github.com/Viren070/AIOStreams/commit/98548323de487bdafbdb1bee8329691fe3077d05))
* **jellyfin-web:** unpause mpv before each file in the desktop player ([0c4f9e6](https://github.com/Viren070/AIOStreams/commit/0c4f9e6ae13eb579acdacbfc7be3074f71c85a64))
* **jellyfin:** anchor next up on the last episode watched ([12a1735](https://github.com/Viren070/AIOStreams/commit/12a1735464eb8ec88289f0c312ed117793974a3c))
* **jellyfin:** charge pin attempts before checking them ([c89e21e](https://github.com/Viren070/AIOStreams/commit/c89e21ea14bcb038a54184cde8018a081003db9b))
* **jellyfin:** don't paginate on search ([ce27dc1](https://github.com/Viren070/AIOStreams/commit/ce27dc1745f59654148f2f197685b812d761ed78))
* **jellyfin:** fall back through episode images in the info banner ([190774c](https://github.com/Viren070/AIOStreams/commit/190774c48124ff4cdd3ccc457301f4f88fe96cf6))
* **jellyfin:** fall back to the cast photo on person items ([ed90002](https://github.com/Viren070/AIOStreams/commit/ed9000218137dd9462dacf39b0d89881690d9792))
* **jellyfin:** fill the phone version picker with placeholders ([931a03e](https://github.com/Viren070/AIOStreams/commit/931a03e0621f403e60d451e62757ee100f7ca8f1))
* **jellyfin:** keep a version's added subtitles when its streams are resolved again ([9bebe70](https://github.com/Viren070/AIOStreams/commit/9bebe70a41c16d827965d3841c0d23dcf89b7d62))
* **jellyfin:** keep episode ratings their own ([f11ab35](https://github.com/Viren070/AIOStreams/commit/f11ab35fa218f878e9709d4fddfa994e4cf64167))
* **jellyfin:** keep live playback out of watch state ([1d42966](https://github.com/Viren070/AIOStreams/commit/1d429667ed27e02c8889af3be9d30885d9567494))
* **jellyfin:** list embedded tracks only in the file's own order ([407c323](https://github.com/Viren070/AIOStreams/commit/407c323315479072f23f928da570e29eea14e951))
* **jellyfin:** log why a catalog page returned errors ([24f1fab](https://github.com/Viren070/AIOStreams/commit/24f1fabeae6c99177215ede25096c543d5748572))
* **jellyfin:** mark a show watched once its aired episodes are ([8470854](https://github.com/Viren070/AIOStreams/commit/84708540dfe8de43ba82f6ac9f6d49a4c3f7bc30))
* **jellyfin:** play and sign in from the Android app ([e1aff12](https://github.com/Viren070/AIOStreams/commit/e1aff12779a79c6f2c466eb0cf4a01ca2e14dc79))
* **jellyfin:** play streams carried on a meta's video instead of querying stream addons ([37955a9](https://github.com/Viren070/AIOStreams/commit/37955a9239a7a0486d4f70fc41ec5847d288b6c4))
* **jellyfin:** read seasonPosters keyed by season ([99b62d5](https://github.com/Viren070/AIOStreams/commit/99b62d5a8b5fb7ad3c660aba0df26b4e2db915fa))
* **jellyfin:** rebuild the signed-in user for requests without a token ([6717441](https://github.com/Viren070/AIOStreams/commit/6717441cb2e5cd32a2a12a134c9dc4709fb656f3))
* **jellyfin:** reuse a failed resolve for 30 seconds instead of retrying on every playback request ([37845e0](https://github.com/Viren070/AIOStreams/commit/37845e0dbd83b921809f1a60350161a7310fa0a0))
* **jellyfin:** send the client's token in external subtitle URLs ([5a28107](https://github.com/Viren070/AIOStreams/commit/5a28107399ebae0e4696dafaaa70629f7b91a277))
* **jellyfin:** share one stream resolve between concurrent opens of an item ([81a9719](https://github.com/Viren070/AIOStreams/commit/81a97194fb4d84972eb885c1e6a305431a3f6df0))
* **jellyfin:** show a spinner on the episode watched toggle ([15d2690](https://github.com/Viren070/AIOStreams/commit/15d2690b76f24fed2a9937fbe308030ac740c834))
* **jellyfin:** show the title when an item's logo fails to load ([a073d33](https://github.com/Viren070/AIOStreams/commit/a073d331eac1ab63c38c32f95ddab0a98443ab0b))
* **jellyfin:** skip removed catalogs in the featured setting ([9cb6f61](https://github.com/Viren070/AIOStreams/commit/9cb6f613707f5efec1bd59c422681af6703c2c0e))
* **jellyfin:** take the playback runtime from the played source ([6a7ed9c](https://github.com/Viren070/AIOStreams/commit/6a7ed9cc2091ac35085088039e04b5a8a309aa62))
* keep & and = inside catalog and subtitle extra values ([0af3424](https://github.com/Viren070/AIOStreams/commit/0af3424507e79b86733c9d0ba524411cc4eae739))
* **languages:** resolve Bokmål and Nynorsk codes to Norwegian ([c8c81f9](https://github.com/Viren070/AIOStreams/commit/c8c81f987e925b48df05e7760a8316260e261d7d))
* loosen trailer type schema ([4436496](https://github.com/Viren070/AIOStreams/commit/443649612d91e58efcfb2d96acd602f9725e6664)), closes [#1307](https://github.com/Viren070/AIOStreams/issues/1307)
* **metadata:** update default user agent for skyhook ([a82a8c0](https://github.com/Viren070/AIOStreams/commit/a82a8c0c48ca3e90b84bd307d522f2a5eaeb178b))
* **parser:** detect hls urls with a query string ([b74283f](https://github.com/Viren070/AIOStreams/commit/b74283ff549ce39af73cf4a2be3d960f28f93309))
* **parser:** match tags followed directly by an opening bracket ([579697a](https://github.com/Viren070/AIOStreams/commit/579697a420e5cb0dbff7735530017c777c573187)), closes [#1263](https://github.com/Viren070/AIOStreams/issues/1263)
* **parser:** take release groups from title parser only ([460f20b](https://github.com/Viren070/AIOStreams/commit/460f20b6790c9584d686065de188b59c8afbb1c2))
* **presets/gdrive:** fix logo ([376d716](https://github.com/Viren070/AIOStreams/commit/376d7163abcbeb24719a5a1a9188ae1d74f59a3c))
* **proxy:** stop forwarding hop-by-hop response headers ([782f819](https://github.com/Viren070/AIOStreams/commit/782f8191dbe6e6af0eb9330b45b5d1484738a88e))
* **remuxdb:** log lookup failures loudly instead of silently at debug ([#1356](https://github.com/Viren070/AIOStreams/issues/1356)) ([ff64174](https://github.com/Viren070/AIOStreams/commit/ff641743970304c4aacfb4b444fdbf9f0cd54c64))
* **remuxdb:** update lookup endpoint to match RemuxDB's current API ([#1353](https://github.com/Viren070/AIOStreams/issues/1353)) ([a8a124e](https://github.com/Viren070/AIOStreams/commit/a8a124e174ebeb44167b1d01de3ffb2c4d3355bb))
* **server:** expose Content-Range and Accept-Ranges to browser players ([#1277](https://github.com/Viren070/AIOStreams/issues/1277)) ([db8afbe](https://github.com/Viren070/AIOStreams/commit/db8afbe66ddefcf7cca8731497d4f7c605e785e2))
* **streams:** stop suppressing statistics across an await ([3e2eac0](https://github.com/Viren070/AIOStreams/commit/3e2eac03d220c89d5804f972b00173fc9725c523))
* **stremio:** stop logging the user's config on meta requests ([3bb0235](https://github.com/Viren070/AIOStreams/commit/3bb0235a1d408954f67459046dcb890aa3fd1aa6))
* **templates:** detect placeholders in any field and type inputs by field ([f62d7ee](https://github.com/Viren070/AIOStreams/commit/f62d7eebda245dcff2dd9d4a91ab9181cdca8239))
* **ui:** give plain and loading toasts a grey surface ([05c2884](https://github.com/Viren070/AIOStreams/commit/05c28846449c6178bcf3a9498c5f36e4a5152886))
* **ui:** keep toasts and title bar buttons usable while a modal is open ([2d76af3](https://github.com/Viren070/AIOStreams/commit/2d76af3eb643c8338f7993a0a125d000fa54caef))
* **ui:** stop checkbox group rows resizing when toggled ([e397310](https://github.com/Viren070/AIOStreams/commit/e39731060fe20bcf10991ad065a1103867edf2fd))
* **usenet:** look up by-id hashes outside the tree projection ([2235d53](https://github.com/Viren070/AIOStreams/commit/2235d536dd6edb8d53c5b883bbb8f7ce2b5002e8))
* **usenet:** verify file contents at import ([e4d1428](https://github.com/Viren070/AIOStreams/commit/e4d14281ee61d6e7dae754bf5bab9f15694700a6))
* **variants:** bound the instructions one request can run ([9f477fa](https://github.com/Viren070/AIOStreams/commit/9f477fa91a2331cb81e890c07071d6901392953e))
* **watch-state:** deliver fresh events ahead of backlogs ([66f1a39](https://github.com/Viren070/AIOStreams/commit/66f1a39647b6545dd11e2ff2aa69d59cd6ba3997))
* **watch-state:** key long-running anime episodes by their TVDB season ([ebb22d9](https://github.com/Viren070/AIOStreams/commit/ebb22d9d81689054e8b9f49b03a1467f29dd5155))
* **watch-state:** make playstate upsert work on postgres ([9d2b3d9](https://github.com/Viren070/AIOStreams/commit/9d2b3d9eec6e624bbb551f1bd679c46ef701729b))
* **watch-state:** match TVDB and TMDB ids to the IMDb id from the id mappings ([3a76201](https://github.com/Viren070/AIOStreams/commit/3a76201bee47b241c14cf26e0ec6be2ae90b55cd))
* **watch-state:** pick one row per series before limiting recent series ([b17c829](https://github.com/Viren070/AIOStreams/commit/b17c8293cb12c084edfa70c4c5a144e417fd69be))
* **watch-state:** round pulled times and positions to whole milliseconds ([09a9c01](https://github.com/Viren070/AIOStreams/commit/09a9c01037a2f791dbb7127d4e64fb9e563b866a))
* **wrapper:** key cached subtitles by their extras ([2dcf85c](https://github.com/Viren070/AIOStreams/commit/2dcf85c387af6f89c562dcc25c190ecd63acbc47))


### Performance Improvements

* **builtins/library:** time-slice the library scan ([9713fd0](https://github.com/Viren070/AIOStreams/commit/9713fd0825e8fc6652bffcd956ad0f6ae8c5bd32))
* **builtins:** cache only the search result fields the addons read ([c0470c5](https://github.com/Viren070/AIOStreams/commit/c0470c57c3719511e123b40905e8c078a540247f))
* **builtins:** parse each debrid file name once and yield while parsing ([0498171](https://github.com/Viren070/AIOStreams/commit/0498171d613b099a473037f77adddadec6b83c60))
* **builtins:** skip .torrent download for pre-validated bad matches ([#1259](https://github.com/Viren070/AIOStreams/issues/1259)) ([479f809](https://github.com/Viren070/AIOStreams/commit/479f809dbfdea79e28d8576c7d75e622ff3b879e))
* **cache:** compress large redis values with zstd ([28cba47](https://github.com/Viren070/AIOStreams/commit/28cba479ddcd5b4a481480e41eaa847eebf407f5))
* **cache:** evict the memory backend's least recently used entry in constant time ([3feb117](https://github.com/Viren070/AIOStreams/commit/3feb11774971cf14e262a98fc4aee438eae22f64))
* **cache:** sweep expired memory cache entries every minute ([00cb428](https://github.com/Viren070/AIOStreams/commit/00cb428d48c940ce9b3be74f4981b2f8cac5d3ad))
* **config:** skip re-testing stream expressions that already passed validation ([95c8697](https://github.com/Viren070/AIOStreams/commit/95c8697253436638efb5b92136edd4447d83190b))
* **config:** skip save-time variant validation on read paths ([fc55a2c](https://github.com/Viren070/AIOStreams/commit/fc55a2c79fecaf061aae4d3cc98ed72f13e5ed7b))
* **core:** clear the withTimeout timer once the operation settles ([0d109c5](https://github.com/Viren070/AIOStreams/commit/0d109c5100f386462fe0223061c5e2c726be61b5))
* **core:** derive config keys with pbkdf2 on the thread pool ([29d4ef5](https://github.com/Viren070/AIOStreams/commit/29d4ef523f0568e5116232c298faa11349ca1c0f))
* **core:** match ranked regexes once per file name and yield between slices ([6d80a47](https://github.com/Viren070/AIOStreams/commit/6d80a47a38d07ce93767f54626468dc5c413046d))
* **core:** memoise language normalisation ([58dda74](https://github.com/Viren070/AIOStreams/commit/58dda74612ea3e365a3bb7ed2f05cce3c4b3dab4))
* **db:** raise the config key cache ttl to 24h ([743da3d](https://github.com/Viren070/AIOStreams/commit/743da3d06a8976747d1c48e4ddbeaedee29152f2))
* **debrid:** batch cached StremThru availability reads with mget ([a4411f5](https://github.com/Viren070/AIOStreams/commit/a4411f52154a3cf323543e9343401096ada52cbe))
* **debrid:** cache only the files StremThru availability checks can select ([f9de485](https://github.com/Viren070/AIOStreams/commit/f9de4856ce2f02bf2d7b3f84487e189b08247dcf))
* **debrid:** parse only the file names selection reads when resolving ([66560eb](https://github.com/Viren070/AIOStreams/commit/66560ebf6545b656da26e5f95689f5ab4aceac58))
* **distributed-lock:** publish a lock's result only when a waiter is subscribed ([7afe512](https://github.com/Viren070/AIOStreams/commit/7afe5122e105a17a7519b878b460718702b58223))
* **frontend:** memoise catalog rows and mount one MenuTabs layout ([59a11db](https://github.com/Viren070/AIOStreams/commit/59a11db29bb956215f886eafcb2808b98126ad24))
* **http:** skip the recursion counter for requests that ignore it ([7dde970](https://github.com/Viren070/AIOStreams/commit/7dde970e58302cb251ba099c6478f20f050f2c28))
* **jellyfin-web:** decode artwork off the main thread ([4889472](https://github.com/Viren070/AIOStreams/commit/4889472996cbf941d8b2662ca30fa40fb3d2d9d7))
* **jellyfin:** fetch catalogs ahead for rows without a library ([4c1067c](https://github.com/Viren070/AIOStreams/commit/4c1067ccc56c1b836a370165b042269694e9a192))
* **jellyfin:** skip collection sources that cannot hold the requested kinds ([f968659](https://github.com/Viren070/AIOStreams/commit/f96865941a33e735747dee87f50c059928655d88))
* **jellyfin:** stream the watch history export ([30b071f](https://github.com/Viren070/AIOStreams/commit/30b071f5d98854f29d8dbd3cd94e619790cbd511))
* **logging:** skip records below the log level ([b13f5de](https://github.com/Viren070/AIOStreams/commit/b13f5de53f2891b8be398a72e491c04d7f92dd77))
* **nab:** parse torznab/newznab responses with a byte scanner ([b08d4d1](https://github.com/Viren070/AIOStreams/commit/b08d4d174d689a4e5f80ea4fdbd7acacada04ec5))
* **parser:** cache the title regex and pattern entries ([1c28184](https://github.com/Viren070/AIOStreams/commit/1c281843068dc2b20274ec4070869c926879bf41))
* **parser:** cache title lists by identity and prune title matches ([3f88925](https://github.com/Viren070/AIOStreams/commit/3f88925ccbdf6d41a794fa23e43ff790dad26904))
* **parser:** compile service name regexes once instead of per stream ([09f654a](https://github.com/Viren070/AIOStreams/commit/09f654a79d247efe2d7334fc6f3be18799630e2e))
* **parser:** skip unicode folding for ascii titles and clean titles in one pass ([3bedcc6](https://github.com/Viren070/AIOStreams/commit/3bedcc6199de487c69f7bc6451df87416390460d))
* **streams:** time-slice the filterer passes ([797eae0](https://github.com/Viren070/AIOStreams/commit/797eae0299143af480a412385aafdda859ee792e))
* **watch-state:** rank only the chosen shows for next up ([fcf41d9](https://github.com/Viren070/AIOStreams/commit/fcf41d9a0bdd2c869f57fab6facb8551ed8d01c0))
* **wrapper:** skip re-validating a cached meta ([2dcf85c](https://github.com/Viren070/AIOStreams/commit/2dcf85c387af6f89c562dcc25c190ecd63acbc47))


## v2.34.1 (2026-09-22)

- No pull requests found for this version bump.
## v2.34.1

## [2.34.1](https://github.com/Viren070/AIOStreams/compare/v2.34.0...v2.34.1) (2026-09-09)


### Features

* **core:** parse Torz's probed codec/HDR/audio/bitrate data ([#1237](https://github.com/Viren070/AIOStreams/issues/1237)) ([f7d0e67](https://github.com/Viren070/AIOStreams/commit/f7d0e6783be796d1bd757aeb65d86492a8b506ec))
* **usenet:** track unreadable articles per provider ([2d8dd11](https://github.com/Viren070/AIOStreams/commit/2d8dd1116cb918e4f002546a24293fc6950dfcdf))
* **usenet:** verify articles against their yEnc checksums ([72ac0a4](https://github.com/Viren070/AIOStreams/commit/72ac0a4d9625699fff28ff20a4b03a2ee83d80a6))


### Bug Fixes

* coalesce concurrent addon resource requests via distributed lock ([#1217](https://github.com/Viren070/AIOStreams/issues/1217)) ([248d1c4](https://github.com/Viren070/AIOStreams/commit/248d1c4aec817e29a401825dbaff2452c495315f))
* **deduplicator:** update mediaInfoQuality on merged languages/subtitles ([#1291](https://github.com/Viren070/AIOStreams/issues/1291)) ([90eaf92](https://github.com/Viren070/AIOStreams/commit/90eaf921c6a99a9d7ff3856112c142a54c1e408f))
* **metadata/scene-mappings:** update user agent ([c495b1d](https://github.com/Viren070/AIOStreams/commit/c495b1d55e7d0a4c58ce032d869b24071e2f73ad))
* **presets:** link to account settings for Anime Tosho New and nekoBT API keys ([#1294](https://github.com/Viren070/AIOStreams/issues/1294)) ([4905648](https://github.com/Viren070/AIOStreams/commit/49056487e6a1f4c5b5bb23f7f24fe54eaa1f992d))
* **usenet/ebml:** log where the hole-fill tracker lost alignment ([8eba1b8](https://github.com/Viren070/AIOStreams/commit/8eba1b834f27e80b469b74f3a80beeae975eaa10))
* **usenet/rar:** size exact middles past volume 128 by the rar5 volume-number varint ([3459b6a](https://github.com/Viren070/AIOStreams/commit/3459b6a00f4ec27152518ec59c4f73655a61d43e))
* **usenet:** cancel an entry's census shadow when it is deleted ([eb9fd78](https://github.com/Viren070/AIOStreams/commit/eb9fd78d686982c3efdc25b763a48d9b77f83c57))
* **usenet:** fail reads whose decoded bytes disagree with their metadata ([9c0ec73](https://github.com/Viren070/AIOStreams/commit/9c0ec73626d7eb94beb5386edc717368a8df7113))
* **usenet:** infer a volume's fragment when its header article is unreadable ([87c031b](https://github.com/Viren070/AIOStreams/commit/87c031b9193611ea7fed4031a86bc6a3aa2bf2b6))
* **usenet:** keep a completed folder for every category the arrs know ([0844e0f](https://github.com/Viren070/AIOStreams/commit/0844e0fc05962a73dff2c52e9410f77bbeb338ce)), closes [#1282](https://github.com/Viren070/AIOStreams/issues/1282)
* **usenet:** persist the volume sizes the archive parse resolved in the layout ([04120de](https://github.com/Viren070/AIOStreams/commit/04120dee4e5165f984744d33a66bcb6b9cff0045))


### Performance Improvements

* **usenet/rar:** emit exact middle fragments from one sampled volume in the lazy parse ([d1ddf73](https://github.com/Viren070/AIOStreams/commit/d1ddf73212f947863ea55d6d3726c1a926d5e00a))
* **usenet:** queue eight tasks in the serve-path readables so the read-ahead ramp follows the player ([736fd38](https://github.com/Viren070/AIOStreams/commit/736fd38405b76e20124ea44ab50ec9f46bae04e9))
* **usenet:** reuse the parsed nzb model on the first play of an upload ([8f91f9c](https://github.com/Viren070/AIOStreams/commit/8f91f9c645cc5c2965545bc33f556ea1b5eb311b))
* **usenet:** run the census at an idle priority so it never delays probes or playback ([c425c5c](https://github.com/Viren070/AIOStreams/commit/c425c5c80f8b95e9008c3f01a00550fbb9465c81))
* **usenet:** size archive volumes from a probed sibling instead of their last segment ([db31877](https://github.com/Viren070/AIOStreams/commit/db31877fdd24cac8e5443cc85e46c6a50a876804))
* **usenet:** warm the playback target's first article after import ([8affadd](https://github.com/Viren070/AIOStreams/commit/8affadd9322e22ecd78b1de7506f8c36b0e84914))
* **usenet:** warm the selected file's first article when a stream url is minted ([58000e8](https://github.com/Viren070/AIOStreams/commit/58000e86c959a3ab31c687c903fa09873ea7d808))


## vnull (2026-09-21)

- No pull requests found for this version bump.
## vnull

## [2.34.1](https://github.com/Viren070/AIOStreams/compare/v2.34.0...v2.34.1) (2026-09-09)


### Features

* **core:** parse Torz's probed codec/HDR/audio/bitrate data ([#1237](https://github.com/Viren070/AIOStreams/issues/1237)) ([f7d0e67](https://github.com/Viren070/AIOStreams/commit/f7d0e6783be796d1bd757aeb65d86492a8b506ec))
* **usenet:** track unreadable articles per provider ([2d8dd11](https://github.com/Viren070/AIOStreams/commit/2d8dd1116cb918e4f002546a24293fc6950dfcdf))
* **usenet:** verify articles against their yEnc checksums ([72ac0a4](https://github.com/Viren070/AIOStreams/commit/72ac0a4d9625699fff28ff20a4b03a2ee83d80a6))


### Bug Fixes

* coalesce concurrent addon resource requests via distributed lock ([#1217](https://github.com/Viren070/AIOStreams/issues/1217)) ([248d1c4](https://github.com/Viren070/AIOStreams/commit/248d1c4aec817e29a401825dbaff2452c495315f))
* **deduplicator:** update mediaInfoQuality on merged languages/subtitles ([#1291](https://github.com/Viren070/AIOStreams/issues/1291)) ([90eaf92](https://github.com/Viren070/AIOStreams/commit/90eaf921c6a99a9d7ff3856112c142a54c1e408f))
* **metadata/scene-mappings:** update user agent ([c495b1d](https://github.com/Viren070/AIOStreams/commit/c495b1d55e7d0a4c58ce032d869b24071e2f73ad))
* **presets:** link to account settings for Anime Tosho New and nekoBT API keys ([#1294](https://github.com/Viren070/AIOStreams/issues/1294)) ([4905648](https://github.com/Viren070/AIOStreams/commit/49056487e6a1f4c5b5bb23f7f24fe54eaa1f992d))
* **usenet/ebml:** log where the hole-fill tracker lost alignment ([8eba1b8](https://github.com/Viren070/AIOStreams/commit/8eba1b834f27e80b469b74f3a80beeae975eaa10))
* **usenet/rar:** size exact middles past volume 128 by the rar5 volume-number varint ([3459b6a](https://github.com/Viren070/AIOStreams/commit/3459b6a00f4ec27152518ec59c4f73655a61d43e))
* **usenet:** cancel an entry's census shadow when it is deleted ([eb9fd78](https://github.com/Viren070/AIOStreams/commit/eb9fd78d686982c3efdc25b763a48d9b77f83c57))
* **usenet:** fail reads whose decoded bytes disagree with their metadata ([9c0ec73](https://github.com/Viren070/AIOStreams/commit/9c0ec73626d7eb94beb5386edc717368a8df7113))
* **usenet:** infer a volume's fragment when its header article is unreadable ([87c031b](https://github.com/Viren070/AIOStreams/commit/87c031b9193611ea7fed4031a86bc6a3aa2bf2b6))
* **usenet:** keep a completed folder for every category the arrs know ([0844e0f](https://github.com/Viren070/AIOStreams/commit/0844e0fc05962a73dff2c52e9410f77bbeb338ce)), closes [#1282](https://github.com/Viren070/AIOStreams/issues/1282)
* **usenet:** persist the volume sizes the archive parse resolved in the layout ([04120de](https://github.com/Viren070/AIOStreams/commit/04120dee4e5165f984744d33a66bcb6b9cff0045))


### Performance Improvements

* **usenet/rar:** emit exact middle fragments from one sampled volume in the lazy parse ([d1ddf73](https://github.com/Viren070/AIOStreams/commit/d1ddf73212f947863ea55d6d3726c1a926d5e00a))
* **usenet:** queue eight tasks in the serve-path readables so the read-ahead ramp follows the player ([736fd38](https://github.com/Viren070/AIOStreams/commit/736fd38405b76e20124ea44ab50ec9f46bae04e9))
* **usenet:** reuse the parsed nzb model on the first play of an upload ([8f91f9c](https://github.com/Viren070/AIOStreams/commit/8f91f9c645cc5c2965545bc33f556ea1b5eb311b))
* **usenet:** run the census at an idle priority so it never delays probes or playback ([c425c5c](https://github.com/Viren070/AIOStreams/commit/c425c5c80f8b95e9008c3f01a00550fbb9465c81))
* **usenet:** size archive volumes from a probed sibling instead of their last segment ([db31877](https://github.com/Viren070/AIOStreams/commit/db31877fdd24cac8e5443cc85e46c6a50a876804))
* **usenet:** warm the playback target's first article after import ([8affadd](https://github.com/Viren070/AIOStreams/commit/8affadd9322e22ecd78b1de7506f8c36b0e84914))
* **usenet:** warm the selected file's first article when a stream url is minted ([58000e8](https://github.com/Viren070/AIOStreams/commit/58000e86c959a3ab31c687c903fa09873ea7d808))


## v2.34.1 (2026-09-16)

- Update ghcr.io/hassio-addons/base Docker tag to v21.0.4 (#39)
- Changes from main (#41)

## v2.34.1

## [2.34.1](https://github.com/Viren070/AIOStreams/compare/v2.34.0...v2.34.1) (2026-09-09)


### Features

* **core:** parse Torz's probed codec/HDR/audio/bitrate data ([#1237](https://github.com/Viren070/AIOStreams/issues/1237)) ([f7d0e67](https://github.com/Viren070/AIOStreams/commit/f7d0e6783be796d1bd757aeb65d86492a8b506ec))
* **usenet:** track unreadable articles per provider ([2d8dd11](https://github.com/Viren070/AIOStreams/commit/2d8dd1116cb918e4f002546a24293fc6950dfcdf))
* **usenet:** verify articles against their yEnc checksums ([72ac0a4](https://github.com/Viren070/AIOStreams/commit/72ac0a4d9625699fff28ff20a4b03a2ee83d80a6))


### Bug Fixes

* coalesce concurrent addon resource requests via distributed lock ([#1217](https://github.com/Viren070/AIOStreams/issues/1217)) ([248d1c4](https://github.com/Viren070/AIOStreams/commit/248d1c4aec817e29a401825dbaff2452c495315f))
* **deduplicator:** update mediaInfoQuality on merged languages/subtitles ([#1291](https://github.com/Viren070/AIOStreams/issues/1291)) ([90eaf92](https://github.com/Viren070/AIOStreams/commit/90eaf921c6a99a9d7ff3856112c142a54c1e408f))
* **metadata/scene-mappings:** update user agent ([c495b1d](https://github.com/Viren070/AIOStreams/commit/c495b1d55e7d0a4c58ce032d869b24071e2f73ad))
* **presets:** link to account settings for Anime Tosho New and nekoBT API keys ([#1294](https://github.com/Viren070/AIOStreams/issues/1294)) ([4905648](https://github.com/Viren070/AIOStreams/commit/49056487e6a1f4c5b5bb23f7f24fe54eaa1f992d))
* **usenet/ebml:** log where the hole-fill tracker lost alignment ([8eba1b8](https://github.com/Viren070/AIOStreams/commit/8eba1b834f27e80b469b74f3a80beeae975eaa10))
* **usenet/rar:** size exact middles past volume 128 by the rar5 volume-number varint ([3459b6a](https://github.com/Viren070/AIOStreams/commit/3459b6a00f4ec27152518ec59c4f73655a61d43e))
* **usenet:** cancel an entry's census shadow when it is deleted ([eb9fd78](https://github.com/Viren070/AIOStreams/commit/eb9fd78d686982c3efdc25b763a48d9b77f83c57))
* **usenet:** fail reads whose decoded bytes disagree with their metadata ([9c0ec73](https://github.com/Viren070/AIOStreams/commit/9c0ec73626d7eb94beb5386edc717368a8df7113))
* **usenet:** infer a volume's fragment when its header article is unreadable ([87c031b](https://github.com/Viren070/AIOStreams/commit/87c031b9193611ea7fed4031a86bc6a3aa2bf2b6))
* **usenet:** keep a completed folder for every category the arrs know ([0844e0f](https://github.com/Viren070/AIOStreams/commit/0844e0fc05962a73dff2c52e9410f77bbeb338ce)), closes [#1282](https://github.com/Viren070/AIOStreams/issues/1282)
* **usenet:** persist the volume sizes the archive parse resolved in the layout ([04120de](https://github.com/Viren070/AIOStreams/commit/04120dee4e5165f984744d33a66bcb6b9cff0045))


### Performance Improvements

* **usenet/rar:** emit exact middle fragments from one sampled volume in the lazy parse ([d1ddf73](https://github.com/Viren070/AIOStreams/commit/d1ddf73212f947863ea55d6d3726c1a926d5e00a))
* **usenet:** queue eight tasks in the serve-path readables so the read-ahead ramp follows the player ([736fd38](https://github.com/Viren070/AIOStreams/commit/736fd38405b76e20124ea44ab50ec9f46bae04e9))
* **usenet:** reuse the parsed nzb model on the first play of an upload ([8f91f9c](https://github.com/Viren070/AIOStreams/commit/8f91f9c645cc5c2965545bc33f556ea1b5eb311b))
* **usenet:** run the census at an idle priority so it never delays probes or playback ([c425c5c](https://github.com/Viren070/AIOStreams/commit/c425c5c80f8b95e9008c3f01a00550fbb9465c81))
* **usenet:** size archive volumes from a probed sibling instead of their last segment ([db31877](https://github.com/Viren070/AIOStreams/commit/db31877fdd24cac8e5443cc85e46c6a50a876804))
* **usenet:** warm the playback target's first article after import ([8affadd](https://github.com/Viren070/AIOStreams/commit/8affadd9322e22ecd78b1de7506f8c36b0e84914))
* **usenet:** warm the selected file's first article when a stream url is minted ([58000e8](https://github.com/Viren070/AIOStreams/commit/58000e86c959a3ab31c687c903fa09873ea7d808))


## v2.34.0 (2026-09-05)

- Random fixes (#40)

## v2.34.0

## [2.34.0](https://github.com/Viren070/AIOStreams/compare/v2.33.2...v2.34.0) (2026-09-04)


### Features

* add linked accounts with stremio and aiomanager as supported platforms ([dd0decb](https://github.com/Viren070/AIOStreams/commit/dd0decb459bf4ec775af5b0c8f802bd97cb79f89)), closes [#1229](https://github.com/Viren070/AIOStreams/issues/1229) [#1230](https://github.com/Viren070/AIOStreams/issues/1230)
* allow staying signed in to a configuration ([31f8876](https://github.com/Viren070/AIOStreams/commit/31f8876c2c51fa9e6640e79864792413ec9a7b94)), closes [#1233](https://github.com/Viren070/AIOStreams/issues/1233)
* **arr:** clean up stuck imports in the Sonarr/Radarr queue ([560794a](https://github.com/Viren070/AIOStreams/commit/560794a68b5b853b731461f3513bbe680ee06382))
* **arr:** link Sonarr/Radarr instances and hand imports over to them ([560794a](https://github.com/Viren070/AIOStreams/commit/560794a68b5b853b731461f3513bbe680ee06382))
* **arr:** replace dead releases through the arr that grabbed them ([560794a](https://github.com/Viren070/AIOStreams/commit/560794a68b5b853b731461f3513bbe680ee06382))
* **builtins:** add Anime Tosho (New) built-in addon ([#1271](https://github.com/Viren070/AIOStreams/issues/1271)) ([0e42d19](https://github.com/Viren070/AIOStreams/commit/0e42d1938bb83b57fee476b87c0534ed63a5df1d))
* **builtins:** add The Pirate Bay built-in addon ([#1273](https://github.com/Viren070/AIOStreams/issues/1273)) ([2a56c79](https://github.com/Viren070/AIOStreams/commit/2a56c791a6cbd0c577213e5714c94c70dca5b4dc))
* **builtins:** add TheRARBG built-in addon ([#1269](https://github.com/Viren070/AIOStreams/issues/1269)) ([fe753f1](https://github.com/Viren070/AIOStreams/commit/fe753f13f1061ecdcca3de622fde7f99d1db9807))
* **community:** share formatters and templates with other users and instances ([c72bad4](https://github.com/Viren070/AIOStreams/commit/c72bad479257f24b2f4b115a6f2a74779dcd2955))
* **core:** add mediaInfoQuality ([#1234](https://github.com/Viren070/AIOStreams/issues/1234)) ([9a456a2](https://github.com/Viren070/AIOStreams/commit/9a456a240d4c0916164de577688704a3aeedce75))
* **core:** add MPEG-4 encode and PCM audio tag ([#1204](https://github.com/Viren070/AIOStreams/issues/1204)) ([f909749](https://github.com/Viren070/AIOStreams/commit/f909749956aabfaf00576b42a3b93087d475a1c6))
* **core:** add onConditionFailure setting for parallel groups ([bdf5be9](https://github.com/Viren070/AIOStreams/commit/bdf5be9eca2f1ecba5d7b9aa39634627e1fc490f)), closes [#1025](https://github.com/Viren070/AIOStreams/issues/1025)
* **core:** show editions in gdrive formatter ([#1242](https://github.com/Viren070/AIOStreams/issues/1242)) ([2774b07](https://github.com/Viren070/AIOStreams/commit/2774b07266809491a5abb37a10e9f8a949253a16))
* **core:** show editions in lightgdrive and prism ([#1214](https://github.com/Viren070/AIOStreams/issues/1214)) ([e301251](https://github.com/Viren070/AIOStreams/commit/e301251eaacfa0e1ed735a156d769b33119a4af9))
* **dashboard:** add memory graph ([eb6a32e](https://github.com/Viren070/AIOStreams/commit/eb6a32e70abedfef580430c8c5ccdb043a41b12a))
* **dashboard:** update overview page with active streams, bandwidth, review queue, usenet activity ([3304d21](https://github.com/Viren070/AIOStreams/commit/3304d21723efc03fb5106a23762485edc4947a9d))
* **frontend:** add formatter browser with mini previews, tabs for built-in / saved / community ([c72bad4](https://github.com/Viren070/AIOStreams/commit/c72bad479257f24b2f4b115a6f2a74779dcd2955))
* **frontend:** group filter tabs ([0d19b73](https://github.com/Viren070/AIOStreams/commit/0d19b73619cc8e483613804a816c4bb8da5a2389))
* **frontend:** keep unsaved changes as drafts ([2a61865](https://github.com/Viren070/AIOStreams/commit/2a61865fd1b3717040554cd5625593e0f436c78e))
* **frontend:** redesign about page, template wizard, onboarding experience ([80dd827](https://github.com/Viren070/AIOStreams/commit/80dd827c7f8e35b44ea6bb8c6564ea040b29def7))
* **frontend:** update styles ([00d1900](https://github.com/Viren070/AIOStreams/commit/00d1900d9a62cea62307985a41ef5da6bf0367b9))
* **frontend:** use shared sortable list component for groups editor ([38f9e53](https://github.com/Viren070/AIOStreams/commit/38f9e534eb9ac8c99789c1851b9ac9132b92b745))
* **health-checks:** let expressions react to whether a service is up ([9ce46c8](https://github.com/Viren070/AIOStreams/commit/9ce46c87953159a18a394df0176cd660cfac9ca6))
* **presets:** add USA TV Next preset ([a6969b2](https://github.com/Viren070/AIOStreams/commit/a6969b26ac89e3ca8ea6b16c1aa34ab279d6602a)), closes [#1031](https://github.com/Viren070/AIOStreams/issues/1031)
* **presets:** ingest Easynews++ subtitle languages from the 💬 line ([#1133](https://github.com/Viren070/AIOStreams/issues/1133)) ([20fbd41](https://github.com/Viren070/AIOStreams/commit/20fbd41962f6a8464e8d746dbce0c3142f83d54d))
* **sel:** add `folderSize()` function ([#1258](https://github.com/Viren070/AIOStreams/issues/1258)) ([f0de21b](https://github.com/Viren070/AIOStreams/commit/f0de21b4051d6212ddd55bf7a798f3dadae67ef8))
* **server:** add configurable max JSON request body size ([c72bad4](https://github.com/Viren070/AIOStreams/commit/c72bad479257f24b2f4b115a6f2a74779dcd2955))
* **shares:** expose the usenet library as a virtual filesystem ([edbf3c1](https://github.com/Viren070/AIOStreams/commit/edbf3c1acdeda42d55331f5f5d47c90f74c4fbfd))
* **shares:** serve the library over WebDAV, NFS and FUSE ([6458135](https://github.com/Viren070/AIOStreams/commit/64581352d26777cdb3e9fa706633419f275f4700))
* **usenet:** recheck library entries against your providers on a schedule ([568f35b](https://github.com/Viren070/AIOStreams/commit/568f35b242a3ff1c3e585ec9ea3024d418e98c54))
* **usenet:** reset recorded stats per provider/indexer and flag removed providers ([3d7e9d8](https://github.com/Viren070/AIOStreams/commit/3d7e9d8efe5bdd97b8814b5a53f68f8f008d6a45))
* **usenet:** support serving audio files ([af32429](https://github.com/Viren070/AIOStreams/commit/af32429f2e0f51741ef74c9c468a7a9d501ba446))
* **usenet:** support suffix byte ranges on the native stream route ([9d8df15](https://github.com/Viren070/AIOStreams/commit/9d8df154c633fe01debb0b99d2fbd756b580bc72))
* **usenet:** verify file heads match their extension at import and on rechecks ([568f35b](https://github.com/Viren070/AIOStreams/commit/568f35b242a3ff1c3e585ec9ea3024d418e98c54))
* **variants:** activate a variant from the request and health checks ([9ce46c8](https://github.com/Viren070/AIOStreams/commit/9ce46c87953159a18a394df0176cd660cfac9ca6))


### Bug Fixes

* acknowledge instance-provided TMDB/TVDB keys in the template wizard and config page ([39c6281](https://github.com/Viren070/AIOStreams/commit/39c62815f03e6a84811bef05e9f065de561265b3))
* add link to template browser on your configuration card ([3d77a85](https://github.com/Viren070/AIOStreams/commit/3d77a855fcca3907da7c2ee839cea42da737ec52))
* **anime-database:** correctly handle empty stored sources ([9e59c4a](https://github.com/Viren070/AIOStreams/commit/9e59c4aa98783b57bfc740f2f6350d4ebb5dbec1))
* **anime-database:** make the shared store safe across replicas ([8ef429f](https://github.com/Viren070/AIOStreams/commit/8ef429ffe8702e092c8f47ded3d57edd2016d13c))
* **anime-database:** switch the anime offline database to cedya77's continuation ([5394626](https://github.com/Viren070/AIOStreams/commit/5394626a60ea1c3dee1ae972220bde5d1d73d0c1))
* **builtins/eztv:** match season packs (episode "0") ([#1262](https://github.com/Viren070/AIOStreams/issues/1262)) ([e677c79](https://github.com/Viren070/AIOStreams/commit/e677c79b1a474601085f9f6374cdf77489950b2c))
* **builtins/torznab:** use prowlarrindexer as indexer ([61e8236](https://github.com/Viren070/AIOStreams/commit/61e8236780b080e8ea74c0332271800704583153))
* **builtins:** add server-side category filtering to TorrentGalaxy and TheRARBG ([#1276](https://github.com/Viren070/AIOStreams/issues/1276)) ([16f983f](https://github.com/Viren070/AIOStreams/commit/16f983f2217443bd1bc43891d422f9f4a942fbb6))
* **config:** trust proxies on private networks by default ([1bd1474](https://github.com/Viren070/AIOStreams/commit/1bd14741d0d5b67e7e82946a30cfe5232c630913))
* **core:** fix emoji-boundary regex ([#1238](https://github.com/Viren070/AIOStreams/issues/1238)) ([c5a253f](https://github.com/Viren070/AIOStreams/commit/c5a253fa2e67bc5ac38536aaa7ad3d02adf79f27))
* **core:** let real probe data override indexer and filename-derived language/subtitle guesses ([#1185](https://github.com/Viren070/AIOStreams/issues/1185)) ([6fdbc62](https://github.com/Viren070/AIOStreams/commit/6fdbc622bc6a2ebd0cfcfa7263d7d7a569ce8a75))
* **core:** match titles that carry a country tag or year ([7a0f2c1](https://github.com/Viren070/AIOStreams/commit/7a0f2c14f40c26dd411076c8297113ac84d77460))
* **core:** preserve DebridError identity across distributed lock ([#1184](https://github.com/Viren070/AIOStreams/issues/1184)) ([448d7c5](https://github.com/Viren070/AIOStreams/commit/448d7c5208e321a4e90fa541898daf0115b08487))
* **core:** skip language/subtitle filters for P2P streams pending service wrap ([#1187](https://github.com/Viren070/AIOStreams/issues/1187)) ([7e0a73a](https://github.com/Viren070/AIOStreams/commit/7e0a73a3c910e9ebbcd9fc3ddec9a7fa74685732))
* **core:** stop stremthru treating subtitle flags as audio languages ([#1241](https://github.com/Viren070/AIOStreams/issues/1241)) ([a91ac4b](https://github.com/Viren070/AIOStreams/commit/a91ac4b01444559fd5730b9f0984e34948fbacb3))
* **distributed-lock:** fix crash reviving errors with a getter-only name ([#1274](https://github.com/Viren070/AIOStreams/issues/1274)) ([b4ebc5c](https://github.com/Viren070/AIOStreams/commit/b4ebc5cead2a4fe1b7b73b13ac47c8ec92fc6479))
* **distributed-lock:** let a file-lock waiter take over a stale lock ([a554c9f](https://github.com/Viren070/AIOStreams/commit/a554c9f0d89e7888b4c7922b8b4843ed063aa619))
* **frontend/alert:** align description-only text correctly ([d7c5f01](https://github.com/Viren070/AIOStreams/commit/d7c5f0100c2dc255ec56f194fcdaaf0e069d96d5))
* **frontend/combobox:** allow limiting displayed item pills ([b86d30b](https://github.com/Viren070/AIOStreams/commit/b86d30b67ea2ef4ff8d4bf33eeaf96cb9b3bcc2e))
* **frontend/templates:** validate select defaults in validator ([8c6f778](https://github.com/Viren070/AIOStreams/commit/8c6f7781d9e1f77873fe2abf03421b36a0aa7dfa))
* **frontend:** add back sign in/out triggers to about page/page controls ([5e450a5](https://github.com/Viren070/AIOStreams/commit/5e450a54dced692b9d3d7ddfa3faad5a221e108a))
* **frontend:** add back simple/advanced toggle ([9450b36](https://github.com/Viren070/AIOStreams/commit/9450b36bfddee4ceb4b6918cda6c9648b63b01f7))
* **frontend:** adjust interface mode switch styles ([16b2bba](https://github.com/Viren070/AIOStreams/commit/16b2bbac08a6436fd09203bb6825a5cb9715f364))
* **frontend:** adjust modal and nzb browser styling/layout ([9555e95](https://github.com/Viren070/AIOStreams/commit/9555e95e27cf05ef2a930d564f6a8ab377120979))
* **frontend:** detect earlier visits for first visit path in update modal ([ca9b676](https://github.com/Viren070/AIOStreams/commit/ca9b676a2190d64a2bbd88fbbe2bde49edaaf185))
* **frontend:** ensure correct template details panel opens on back ([d18f338](https://github.com/Viren070/AIOStreams/commit/d18f3384abc16b073e36f8f8ee3c34a26d4e6567))
* **frontend:** expand up to 5 newer releases by default ([ddc9643](https://github.com/Viren070/AIOStreams/commit/ddc9643bde97459cfb3769e1841cf6867ef20ed4))
* **frontend:** fix featured templates fallback when configured IDs are stale ([5ef92d1](https://github.com/Viren070/AIOStreams/commit/5ef92d1bda88f0e6bccbff75625ab6035b1b1899))
* **frontend:** keep menu tabs on one row past five tabs ([6420946](https://github.com/Viren070/AIOStreams/commit/6420946e98ed2c921c0af7d7c6414301a3d2eee3))
* **frontend:** reserve the scrollbar gutter to stop layout shift ([8c2b148](https://github.com/Viren070/AIOStreams/commit/8c2b148ceca1510c972ad30ad15d01c0d0bc02e6))
* **frontend:** restore contrast on surfaces using the desaturated palettes ([3be1af9](https://github.com/Viren070/AIOStreams/commit/3be1af9595ee3341b11284dacd2559405d2c9365))
* **frontend:** route to the configure page for path param variants ([dfa22fe](https://github.com/Viren070/AIOStreams/commit/dfa22fee51b293bbe3fe9af8975a083727f963eb))
* **frontend:** say "just now" for sub-second relative times ([2c88136](https://github.com/Viren070/AIOStreams/commit/2c881362e99a76fa082bd2dfa2ea07fcf11b83e6))
* **frontend:** scope unsaved drafts to the identity that made them ([34e3b15](https://github.com/Viren070/AIOStreams/commit/34e3b1547153946f326edb173363551fe2900840))
* **frontend:** update colour styles ([9a4a1af](https://github.com/Viren070/AIOStreams/commit/9a4a1afee19a5331b1402ae6a4d46a74bcac9d2a))
* **frontend:** use the latest change handler in ui components ([2c88136](https://github.com/Viren070/AIOStreams/commit/2c881362e99a76fa082bd2dfa2ea07fcf11b83e6))
* **frontend:** wrap template detail content in a single scroll container ([e63adcf](https://github.com/Viren070/AIOStreams/commit/e63adcf15d90ea4760b81f56d7888328f5550495))
* key torrent grabs on guid and indexer where available ([e0a5b4c](https://github.com/Viren070/AIOStreams/commit/e0a5b4c559a42cefc5aab0f1aa7a9077db4d68ec)), closes [#1192](https://github.com/Viren070/AIOStreams/issues/1192)
* **linked-accounts:** match installed addons by identity, not URL ([37825d2](https://github.com/Viren070/AIOStreams/commit/37825d2e68365cf1462199b32746b2eb549ec65b))
* **linked-accounts:** push manifest URLs that use an alias ([a47d696](https://github.com/Viren070/AIOStreams/commit/a47d696aa3c524e43b72310ac53393411064c2a8))
* **nab:** answer test queries with a category the client asked for ([b6a51fb](https://github.com/Viren070/AIOStreams/commit/b6a51fbf140f54fcc940283a22b04234058ae0b5))
* **parent-config:** carry trusted over when merging a parent on load ([5920130](https://github.com/Viren070/AIOStreams/commit/5920130b646942455e72e440d40c7aca1c82dc8f))
* preserve word boundary when stripping : and ; in cleanTitle ([#1188](https://github.com/Viren070/AIOStreams/issues/1188)) ([6b9ee1c](https://github.com/Viren070/AIOStreams/commit/6b9ee1c8eaf9fb200c69d083315a58bf4ea54018))
* **presets:** update Marvel Universe default URL ([861ee6b](https://github.com/Viren070/AIOStreams/commit/861ee6b3c38ecc57ce5627c0c36be79d625dc06c))
* recognize Torrin TRN short name ([#1243](https://github.com/Viren070/AIOStreams/issues/1243)) ([44e46b7](https://github.com/Viren070/AIOStreams/commit/44e46b7d598181867933793886ef42b2d35af199))
* remove arr warning ([0839161](https://github.com/Viren070/AIOStreams/commit/083916104075b1f15b67e53e07ed6e7050223afd))
* remove noisy queue cleanup log ([bbaf8a4](https://github.com/Viren070/AIOStreams/commit/bbaf8a409e14e79114ce185aeff77c376259ec42))
* **server:** enable trust proxy and derive cookie Secure from the request ([0dcf57d](https://github.com/Viren070/AIOStreams/commit/0dcf57dbf849b81aed42f35fa51ffa6ba2ece714))
* **server:** properly handle request body too large errors ([c72bad4](https://github.com/Viren070/AIOStreams/commit/c72bad479257f24b2f4b115a6f2a74779dcd2955))
* **templates:** discard saved template inputs the template no longer accepts ([2eed6d8](https://github.com/Viren070/AIOStreams/commit/2eed6d82227a3bdfd689dcc291cbcb22e5144ecc))
* **torrent:** lower the default get-torrent concurrency ([#1193](https://github.com/Viren070/AIOStreams/issues/1193)) ([c01b81a](https://github.com/Viren070/AIOStreams/commit/c01b81a7d2089e9c6ee39ba8cb77a1521f4e9d00))
* use the static middleware by express ([#1171](https://github.com/Viren070/AIOStreams/issues/1171)) ([61d1aca](https://github.com/Viren070/AIOStreams/commit/61d1aca8df5cb0f77e9f2cb37acc821e9af7c843))
* **usenet:** attribute byte-path nzb grab failures and improve error log ([a5bdb4f](https://github.com/Viren070/AIOStreams/commit/a5bdb4fd59bbae18bc89ecee8ea0a7746ef3de4e))
* **usenet:** cap prefetchSegments at 256 ([8ddedd0](https://github.com/Viren070/AIOStreams/commit/8ddedd0daf13bb49d52ffea73880d29e4db0ac70))
* **usenet:** don't size a file from `=ybegin size=` when it holds only some parts ([e211efa](https://github.com/Viren070/AIOStreams/commit/e211efa9d29fe0d36849a4303f2ca2e158f0fb97))
* **usenet:** merge NZBs that list one file per article ([f1ff3c5](https://github.com/Viren070/AIOStreams/commit/f1ff3c51ce93017dc4a69d66ea6f7b5258c57116))
* **usenet:** resume the segment stream for paused-mode readers ([16a2f7b](https://github.com/Viren070/AIOStreams/commit/16a2f7b15618566c1f560dabf00e64a495934a30))
* **usenet:** stop caching non-NZB grab responses ([5e932f6](https://github.com/Viren070/AIOStreams/commit/5e932f6f96ff723f9dca09dde17c1a1709de2167)), closes [#1205](https://github.com/Viren070/AIOStreams/issues/1205)
* **usenet:** sweep parsed nzb cache for eviction at an interval ([1c80936](https://github.com/Viren070/AIOStreams/commit/1c80936e8e4f5299a8d70c5b54e90f7d2f9c2be2))


### Performance Improvements

* **analytics:** drop unreachable and redundant analytics_events indexes ([764a123](https://github.com/Viren070/AIOStreams/commit/764a1230f5322d9d1d7353fe99eb24dab2b3f524))
* **anime-database:** move the canonical store into the database ([efca465](https://github.com/Viren070/AIOStreams/commit/efca46516286280a304dbcadaea500a7297f4869))
* **anime-database:** reduce store memory and rebuild cost ([383b06b](https://github.com/Viren070/AIOStreams/commit/383b06b1268333680bcf1312fe8a88747ffa6df4))
* **id-mappings:** use typed arrays and a binary cache file ([dae294c](https://github.com/Viren070/AIOStreams/commit/dae294c9605a268c59c812e60b0aed3e3879636d))
* lazy load user agents library ([c5b716c](https://github.com/Viren070/AIOStreams/commit/c5b716c4ad3ab857c23bbd77252a2dddd3be70ec))
* set max semi space size to 8 ([2cee29f](https://github.com/Viren070/AIOStreams/commit/2cee29fd80ffbb57fe29d40bd5056234248f487a))
* **usenet/ebml:** scan for cluster headers without copying the chunk ([e770f10](https://github.com/Viren070/AIOStreams/commit/e770f10c59828a742854be2b24767f9134e0f87d))
* **usenet:** decrypt AES-CBC in place with native module ([a5132f1](https://github.com/Viren070/AIOStreams/commit/a5132f1fef8ca73d2e040dec28f8b3b86e4f3c7a))
* **usenet:** don't decode abandoned article fetches ([773bb07](https://github.com/Viren070/AIOStreams/commit/773bb07e940a83a78466088c607e2b42c1937cc6))
* **usenet:** grow read-ahead with what the player has consumed ([8d9713b](https://github.com/Viren070/AIOStreams/commit/8d9713bd745d135351a3a8367f5a808429a7bd5c))
* **usenet:** manually run GC on engine eviction ([d63d240](https://github.com/Viren070/AIOStreams/commit/d63d240eb083a7dfbd69b8a9bec6a3169f65a428))
* **usenet:** recycle serve-path slot buffers across range streams ([98eb2f4](https://github.com/Viren070/AIOStreams/commit/98eb2f47babf02b0d1e91e38f369559f6e1011b3))
* **usenet:** resolve lazy RAR fragments off the seek path ([74accda](https://github.com/Viren070/AIOStreams/commit/74accda43da8e5d28d1ba1bb3a02cbb2e98e502b))
* **usenet:** share a measured part grid across an archive set's volumes ([125fe03](https://github.com/Viren070/AIOStreams/commit/125fe032651ffd3eb87e517a0cc394e15fb37b5b))
* **usenet:** size an archive range stream's first window to one segment ([0a674ba](https://github.com/Viren070/AIOStreams/commit/0a674ba8e7781749cbe0e27753f67abe1a711d2d))
* **usenet:** size pooled article buffers from the declared segment size ([2dbd222](https://github.com/Viren070/AIOStreams/commit/2dbd222838398bf30685e36c3095e47540b93fe5))
* **usenet:** start an archive range stream narrow ([e23e363](https://github.com/Viren070/AIOStreams/commit/e23e3636420646e70c2b72e06b989870f9979d21))


## v2.33.2 (2026-08-12)

- No pull requests found for this version bump.
## v2.33.2

## [2.33.2](https://github.com/Viren070/AIOStreams/compare/v2.33.1...v2.33.2) (2026-08-10)


### Bug Fixes

* **usenet:** type archive inner files by magic bytes ([9a1b6d7](https://github.com/Viren070/AIOStreams/commit/9a1b6d7f4954dc38113153893c070580ecd1faef))
* **variants:** support path param based selector and make default ([9778afc](https://github.com/Viren070/AIOStreams/commit/9778afcf07f2b994b226d69031caa454d5127aec))


## v2.33.1 (2026-08-11)

- Add logging verbosity toggle to NPM (#35)

## vseanime-extensions-v0.10.1 (2026-08-11)

- No pull requests found for this version bump.
## vseanime-extensions-v0.10.1

## [0.10.1](https://github.com/Viren070/AIOStreams/compare/seanime-extensions-v0.10.0...seanime-extensions-v0.10.1) (2026-08-10)


### Bug Fixes

* **seanime-extensions:** support parsing path based variant selectors ([5e64202](https://github.com/Viren070/AIOStreams/commit/5e642023d32502be032a2d5602b62dcd2022ae75))


## v2.33.1

## [2.33.1](https://github.com/Viren070/AIOStreams/compare/v2.33.0...v2.33.1) (2026-08-09)


### Bug Fixes

* **presets/mediafusion:** add torrin as supported service ([#1176](https://github.com/Viren070/AIOStreams/issues/1176)) ([a2231a9](https://github.com/Viren070/AIOStreams/commit/a2231a9ec3687b5af7c10c880b8498267be9ede2))


### Miscellaneous Chores

* update header presets ([2e12d3d](https://github.com/Viren070/AIOStreams/commit/2e12d3d3f2d5efcd37208c0e53c871dc7ad1ebbb))


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


