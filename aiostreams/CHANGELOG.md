# Changelog

## [2.37.0](https://github.com/Viren070/AIOStreams/compare/v2.36.0...v2.37.0) (2026-10-23)


### Features

* **core:** add a party store kept in memory or in Redis ([7a489b4](https://github.com/Viren070/AIOStreams/commit/7a489b4ae2fa12704ccf9b740d5825dd816b7c9c))
* **core:** add a sharedId to episodes whose own id is hashed ([2b5eaf9](https://github.com/Viren070/AIOStreams/commit/2b5eaf91e3cfef37f003e6989edce32ced077221))
* **core:** add a SyncPlay group engine and the party relay protocol ([0dc9c67](https://github.com/Viren070/AIOStreams/commit/0dc9c670b5c9e419cc7b5d4d0691ffd69b266104))
* **core:** add an app custom CSS setting ([b47d1ed](https://github.com/Viren070/AIOStreams/commit/b47d1eded94c71b6c787b251110024934272f06c))
* **core:** add avatars to the party protocol ([8781d22](https://github.com/Viren070/AIOStreams/commit/8781d2234e0164b10122d8f105fc9d2f80dabcd7))
* **core:** add storage, ids and items for Jellyfin playlists ([948cfe7](https://github.com/Viren070/AIOStreams/commit/948cfe74ed5b29c138d30b8ae36b19e162ad41e1))
* **core:** keep reports from the apps and pass them on to the developer ([2c760fd](https://github.com/Viren070/AIOStreams/commit/2c760fdece71ec5d8c6e72419f60d1c2ecf549a4))
* **core:** let a shared record kind count toward its own cap ([42327c9](https://github.com/Viren070/AIOStreams/commit/42327c92148c837e054895a26e965076e8bd7dd2))
* **core:** name a country the same from any code or spelling ([724d346](https://github.com/Viren070/AIOStreams/commit/724d3468df17c6cb50f5575e9a965321e719d023))
* **core:** name the language a tag stands for, with its region ([f0d8569](https://github.com/Viren070/AIOStreams/commit/f0d85693e47e77ec4f7f28a8ddaa9626a67a04ef))
* **core:** replace the party report message with an offset message ([6d6228e](https://github.com/Viren070/AIOStreams/commit/6d6228e400c487a6ddaa841c5a68cee533bb7500))
* **core:** store the playing version and tracks on watch sessions ([6d8858a](https://github.com/Viren070/AIOStreams/commit/6d8858a2580a1b580be6874ca1b8f3440ac22dcd))
* **desktop:** play HDR on macOS with a choice of video output ([#1563](https://github.com/Viren070/AIOStreams/issues/1563)) ([3f88359](https://github.com/Viren070/AIOStreams/commit/3f88359dc527e91a8b4b14677562522b5db5aa03))
* **frontend:** add the party invite page and a Watch Parties settings tab ([40f8da5](https://github.com/Viren070/AIOStreams/commit/40f8da57abbec5a5ff218169b52b674fd57a1179))
* **frontend:** read app reports in the dashboard ([8c3257d](https://github.com/Viren070/AIOStreams/commit/8c3257de696dc6250244f195522ccde3d7100ae0))
* **frontend:** rework addons menu ([644dda6](https://github.com/Viren070/AIOStreams/commit/644dda67bd96f406d08fcddcf619434402224298))
* **jellyfin:** add folder, editions, matched expressions and SeaDex to version extensions ([4ceeffb](https://github.com/Viren070/AIOStreams/commit/4ceeffbf98d343a2858a579e140664f6d138d4b4))
* **jellyfin:** add showWatchedAt to Next Up episodes ([eb30c78](https://github.com/Viren070/AIOStreams/commit/eb30c780a4549d4cd71d5547f210c21473ea628c))
* **jellyfin:** add SyncPlay ([b6b1c12](https://github.com/Viren070/AIOStreams/commit/b6b1c1220778e8e136a099c15b0f5fe958f298a8))
* **jellyfin:** add the /Playlists routes and list playlists as items ([6b38420](https://github.com/Viren070/AIOStreams/commit/6b38420e6218eb665273f7493adf3a442f5b2526))
* **jellyfin:** add the stream list index to version extensions ([c31e6fe](https://github.com/Viren070/AIOStreams/commit/c31e6fefdf91f6685c7f4f64c62f64e411401b6b))
* **jellyfin:** fill person pages and filmographies from person metas ([e7ec655](https://github.com/Viren070/AIOStreams/commit/e7ec6552328ec985f585d2e10d5a248d8beff049))
* **jellyfin:** keep SyncPlay groups in the party store ([f317a9d](https://github.com/Viren070/AIOStreams/commit/f317a9d249b2cf3d2e183b37dc9b7fcbfee4907d))
* **jellyfin:** let the X-AIOStreams-* headers through CORS ([2eb9b16](https://github.com/Viren070/AIOStreams/commit/2eb9b16ade5c7f8502edffb5347a70cb2dc04c53))
* **jellyfin:** list versions that need headers or YouTube when PlaybackInfo asks ([92d0190](https://github.com/Viren070/AIOStreams/commit/92d0190159f031528bd8048d0d171759e90bc37a))
* **jellyfin:** pass animatedPoster from metas onto items ([e0c7e80](https://github.com/Viren070/AIOStreams/commit/e0c7e80a705d3912ea9203cbe3f9b52429bc77a2))
* **jellyfin:** pick the default audio track by the user's audio types ([e0eb9f2](https://github.com/Viren070/AIOStreams/commit/e0eb9f2e6a2809394375f06ed3ce4edb33067eb4))
* **jellyfin:** raise the library limit to 500 and cap concurrent catalog requests ([3278fa6](https://github.com/Viren070/AIOStreams/commit/3278fa69835f0e95a942158adbe524a0af7d88b2))
* **jellyfin:** read More Like This from similar catalogs ([a0e34a6](https://github.com/Viren070/AIOStreams/commit/a0e34a6537e61729ee3c7b60b8f784616f0f5503))
* **jellyfin:** search people through person catalogs ([e65c58a](https://github.com/Viren070/AIOStreams/commit/e65c58aa7207899e1ec8ee3a5aca1c8fb4c7b336))
* **jellyfin:** send the app custom CSS in the server's public info ([9694f1e](https://github.com/Viren070/AIOStreams/commit/9694f1e092a50e42617a010458939e1e087bdd94))
* **jellyfin:** take tmdbId and tvdbId as a cast entry's person id ([ba30161](https://github.com/Viren070/AIOStreams/commit/ba301611075d7c2811260f14126294c1e0dd3571))
* **native:** add container indexes and seek thumbnails in Rust ([e2bca29](https://github.com/Viren070/AIOStreams/commit/e2bca29b433934c3b5f02e5d6e9d511e43e9ce59))
* **native:** add thumbnail JNI exports for Android ([39eb4ac](https://github.com/Viren070/AIOStreams/commit/39eb4acca632329e5a03d8607102f612ee096add))
* **native:** add thumbnails that open their file in the background ([87c1ece](https://github.com/Viren070/AIOStreams/commit/87c1ecefeb5c4e483827192d4b9a4d1c6d5dc592))
* **native:** log thumbnail opens, retries and keyframe failures ([3b20314](https://github.com/Viren070/AIOStreams/commit/3b203141fbe9b3ec82e861f2fcf5894d103210f1))
* **native:** read PGS and MP4 subtitle timelines ([b767db3](https://github.com/Viren070/AIOStreams/commit/b767db3c1afdcc750f311aec24a65eedbc48592b))
* **native:** read subtitle timelines from a Matroska file's index ([f7bc3b2](https://github.com/Viren070/AIOStreams/commit/f7bc3b2b335827c8ed6eb8967d75f76bbc77a93a))
* **native:** reshape Dolby Vision profile 5 thumbnails with each frame's RPU ([5534a20](https://github.com/Viren070/AIOStreams/commit/5534a20472705661d0587b87523fb092b13da5d0))
* **server:** add a watch party relay at /party/v1 ([434c368](https://github.com/Viren070/AIOStreams/commit/434c368327f25df01425b29ea9379fce449cdedc))
* **server:** keep relay parties in the party store ([af4d5c6](https://github.com/Viren070/AIOStreams/commit/af4d5c64fd4753e3d35bf57fb314e8bbed94b413))
* **server:** keep sealed avatars on relay seats ([d1a62bf](https://github.com/Viren070/AIOStreams/commit/d1a62bf376985b15ee9a48b76e421c25475cac4e))
* **server:** mark controllable devices among the activity sessions ([77448e6](https://github.com/Viren070/AIOStreams/commit/77448e62d8aa8e9f3ea188642b619c47c90ef223))
* **server:** report the playing version and tracks in sessions ([48706ee](https://github.com/Viren070/AIOStreams/commit/48706ee29c2a8dea2b9f0cb3e387e1be479647d4))
* **server:** take app reports and prune them ([2b04799](https://github.com/Viren070/AIOStreams/commit/2b047996a077d6a7991d6b1a7de26d1fe61bde54))
* **server:** take capabilities and relay remote commands to sessions ([24611c8](https://github.com/Viren070/AIOStreams/commit/24611c8fc91a9824159d601e51e47d1651bd5590))
* **server:** take members' offsets from their apps ([3ad9205](https://github.com/Viren070/AIOStreams/commit/3ad9205eed360568f710169607f949f680338286))
* **ui:** add a replaceable table of the kit's own words ([dde33e6](https://github.com/Viren070/AIOStreams/commit/dde33e61fe14864cc7f9c5dd6a3fda293da2b66a))
* **ui:** add swatches and an optional picker to the colour input ([628cb1f](https://github.com/Viren070/AIOStreams/commit/628cb1f85d813957b83a4613491b1e7342558c5f))
* **ui:** let a carousel keep a focused slide where the first one starts ([8e781aa](https://github.com/Viren070/AIOStreams/commit/8e781aa1d21fbb5375a7c1b54535b44104c6c9eb))
* **ui:** mark a drawer's side ([847ff77](https://github.com/Viren070/AIOStreams/commit/847ff772b515c7eff9cb8cf5be2be8991f170d98))
* **ui:** ring the whole row of a right-side switch when focused ([0b085be](https://github.com/Viren070/AIOStreams/commit/0b085beab7f32efcec7f37b8e47636c66d047599)), closes [#1533](https://github.com/Viren070/AIOStreams/issues/1533)
* **ui:** support right-to-left layouts ([c99e46b](https://github.com/Viren070/AIOStreams/commit/c99e46bcd7ff2a976fcaad86c806816ddc2faee6))
* **ui:** write sizes in a chosen locale ([43c1a15](https://github.com/Viren070/AIOStreams/commit/43c1a15a247672200eb35e58407652f1d21a53b9))
* **web:** add a cache size setting ([b3d6f92](https://github.com/Viren070/AIOStreams/commit/b3d6f92cdac443387f0a2cc6694d170c76bbc534))
* **web:** add a people row to search ([e9c303e](https://github.com/Viren070/AIOStreams/commit/e9c303e053851c886db1db522106af5d88d8abcb))
* **web:** add a random pick for a show's episodes and your favourites ([01dc8ca](https://github.com/Viren070/AIOStreams/commit/01dc8ca2de9e6aad567ab1bb40b2e251f466b0b0))
* **web:** add a setting for the reactions sent in a party ([33e3608](https://github.com/Viren070/AIOStreams/commit/33e36087545c04bcb0455bbc1e37c86704f6010d))
* **web:** add a time-left toggle and an end time above the player's seek bar ([3efa2b3](https://github.com/Viren070/AIOStreams/commit/3efa2b355e2f192f82a3c25e5cba97e6033276ca)), closes [#1536](https://github.com/Viren070/AIOStreams/issues/1536)
* **web:** add CSS hooks to party members, messages and the player cover ([cf28c5d](https://github.com/Viren070/AIOStreams/commit/cf28c5dc63850c727eb4b8f6c3398a54f8210589))
* **web:** add data-favourite and data-type to poster cards ([af474dd](https://github.com/Viren070/AIOStreams/commit/af474dd1f2e1eea9184364506cb0ea4cd1ed44cf)), closes [#1591](https://github.com/Viren070/AIOStreams/issues/1591)
* **web:** add playlists ([a9bec92](https://github.com/Viren070/AIOStreams/commit/a9bec92aa4148da2af8a8f13060e71c855e0917f))
* **web:** add quick filters and badges to the version list ([eaa4ac7](https://github.com/Viren070/AIOStreams/commit/eaa4ac7d3efd761cf2ba77378276f3edd7dc9032))
* **web:** add sound and output settings for the apps ([976ba8b](https://github.com/Viren070/AIOStreams/commit/976ba8bbc5b50c349b10cfece322b10baae0336a))
* **web:** add subtitle font and shadow settings ([412db8d](https://github.com/Viren070/AIOStreams/commit/412db8db7e1d402b19d2dcaefda27bbf3bb00170))
* **web:** add tooltips to the player buttons and the show download menu ([3729cdb](https://github.com/Viren070/AIOStreams/commit/3729cdb2121b7b8075e0d81822368978dcf3bdbf)), closes [#1588](https://github.com/Viren070/AIOStreams/issues/1588)
* **web:** add translations with Lingui and a language setting ([a48ead4](https://github.com/Viren070/AIOStreams/commit/a48ead42b8273a4c5471a3d05d87e21312cf265d))
* **web:** add watch parties ([93563db](https://github.com/Viren070/AIOStreams/commit/93563dbd3b2b5c166f89829fa574f1f07f76109e))
* **web:** allow a negative subtitle height ([3b2875f](https://github.com/Viren070/AIOStreams/commit/3b2875f61dd2b477c9b552eae2c749b3dd4c3f62))
* **web:** apply the server's CSS under the user's own ([bb658e5](https://github.com/Viren070/AIOStreams/commit/bb658e5741369a36e5f6ee0d9ebbc9085de0ecc0)), closes [#1541](https://github.com/Viren070/AIOStreams/issues/1541)
* **web:** ask for a second Back before leaving the Android app from Home ([5d8791a](https://github.com/Viren070/AIOStreams/commit/5d8791a9c848b4e32d3d319d7090e4be713b3543))
* **web:** clear the launched player's queue when nothing plays next ([4280f9e](https://github.com/Viren070/AIOStreams/commit/4280f9e1cbcf0e4c33b07a5b8c3cd95d0cf19120))
* **web:** connect to a config's server from its manifest URL ([b52e506](https://github.com/Viren070/AIOStreams/commit/b52e506a68df52eac95604543a81eccb28c7e157))
* **web:** cover the player until its first frame ([364c974](https://github.com/Viren070/AIOStreams/commit/364c9746998c4ff3755127aa06d0dd6a4a76ce0a))
* **web:** draw each buffered range on the seek bar ([faca189](https://github.com/Viren070/AIOStreams/commit/faca18939da471d9988a0ede53019727134bd3d3))
* **web:** fetch a server subtitle again each time it is picked ([8542464](https://github.com/Viren070/AIOStreams/commit/85424645350a72e872a1ce53c57bc5d4ee509fa3))
* **web:** give subtitle timing, subtitle style and sound their own menu pages ([1326c9d](https://github.com/Viren070/AIOStreams/commit/1326c9db2e1b3134d6945c8f1c5585c7d6695f03))
* **web:** honour "play the version's default track first" when re-picking audio ([5d22997](https://github.com/Viren070/AIOStreams/commit/5d22997d466959454b37b22a157804b117810747))
* **web:** keep a user with a PIN unlocked until they switch away ([64bd9c0](https://github.com/Viren070/AIOStreams/commit/64bd9c019da6884b7944b02dfb3e686b29367b7d))
* **web:** keep key focus at a row's start ([d58c649](https://github.com/Viren070/AIOStreams/commit/d58c649b7aafbb6e3f881c6f48b1d730ac89761d)), closes [#1583](https://github.com/Viren070/AIOStreams/issues/1583)
* **web:** keep the app language per user ([7e32f7d](https://github.com/Viren070/AIOStreams/commit/7e32f7daf378845a472fa925a39f0874077eee6e)), closes [#1557](https://github.com/Viren070/AIOStreams/issues/1557)
* **web:** keep the subtitle look on the user's account ([e9efa9f](https://github.com/Viren070/AIOStreams/commit/e9efa9f859ed10cb5870afefc7da1b7acaaf35d2))
* **web:** leave the thumbnail out of double-tap seek previews ([270c7c3](https://github.com/Viren070/AIOStreams/commit/270c7c343fa8477e8bb7df004d28140e56e7f698))
* **web:** line added subtitles up with the file's own subtitles ([f016dd6](https://github.com/Viren070/AIOStreams/commit/f016dd6cefc8015cade74def057940d9eb9c3e12))
* **web:** match added subtitles against a PGS track when a file has no text one ([6674a71](https://github.com/Viren070/AIOStreams/commit/6674a71807670a94125c204f241a755fc1e8b465))
* **web:** offer colour swatches, without the picker on TVs ([43850d1](https://github.com/Viren070/AIOStreams/commit/43850d1b131d6e398f81a63c83fbfba29768c78e))
* **web:** offer favourite only on movies and shows ([b723bc3](https://github.com/Viren070/AIOStreams/commit/b723bc3e0fea119a9fa852a486d4612ca4f8d6f3))
* **web:** offer the Android app's download folder choice ([e14f65c](https://github.com/Viren070/AIOStreams/commit/e14f65cff35e377861876be34f99866a10b639a9))
* **web:** open the user switcher from the avatar ([8e26b3c](https://github.com/Viren070/AIOStreams/commit/8e26b3cf22d32cf2bd8f0cd4d902c72aedeaf31f)), closes [#1524](https://github.com/Viren070/AIOStreams/issues/1524)
* **web:** open titles from aiostreams:// item and play links ([2944938](https://github.com/Viren070/AIOStreams/commit/29449387c4d3739f481ed93e52673dfc9c593c68))
* **web:** pass a version's required headers to app downloads ([7e75b36](https://github.com/Viren070/AIOStreams/commit/7e75b36ce600788d56cdc767baa235662e35b9e5))
* **web:** play a card's animatedPoster while it is hovered or focused ([7768318](https://github.com/Viren070/AIOStreams/commit/7768318a17864f00200f398b5be623403f32c273))
* **web:** play titles on and control other devices ([27f7b78](https://github.com/Viren070/AIOStreams/commit/27f7b78d907045c465bd2fc650b262ec1f5cdc68))
* **web:** play trailers with the user's track preferences ([99f67bb](https://github.com/Viren070/AIOStreams/commit/99f67bb460de780f4f1dcc75244519bbd01323aa))
* **web:** play versions that need headers or YouTube in the app's player ([17527e3](https://github.com/Viren070/AIOStreams/commit/17527e34c9156d7b6e303e93df29c1b30eeb97aa))
* **web:** put the profile first in the TV rail and corner menu ([dd663a7](https://github.com/Viren070/AIOStreams/commit/dd663a74f23e14bc710138f5ebcc0264ddabd731)), closes [#1576](https://github.com/Viren070/AIOStreams/issues/1576)
* **web:** raise the player controls' idle delay to 5 seconds ([b567511](https://github.com/Viren070/AIOStreams/commit/b56751198a7593280901d0bebd5b8c19811bbac0)), closes [#1592](https://github.com/Viren070/AIOStreams/issues/1592)
* **web:** re-pick the audio track by the user's audio types ([1fe5557](https://github.com/Viren070/AIOStreams/commit/1fe555724b3c7b02a18982d8ae0b1ce62c2d9cc4))
* **web:** reorder the player's option buttons by purpose ([0fad099](https://github.com/Viren070/AIOStreams/commit/0fad0994ac73bab7e921d8a3d27d03ccbf01bd97))
* **web:** scroll the calendar agenda to today on a new visit ([7e4407a](https://github.com/Viren070/AIOStreams/commit/7e4407af813bfdd928936709961cdb05d30a96cd))
* **web:** select tabs as a remote or keyboard moves onto them ([a36b909](https://github.com/Viren070/AIOStreams/commit/a36b909276709fa32e59eb4aa99f4b3b7e3e31ad))
* **web:** send a report from troubleshooting or after a crash ([661daef](https://github.com/Viren070/AIOStreams/commit/661daef90ff0b939586cc6cc8579c1a157b3aa8b))
* **web:** send and show avatars in watch parties ([7f79300](https://github.com/Viren070/AIOStreams/commit/7f793000d138502e6644e3fea81500d8a9824d13)), closes [#1584](https://github.com/Viren070/AIOStreams/issues/1584)
* **web:** send continue watching to the Android TV app's Watch Next row ([7f2e4ff](https://github.com/Viren070/AIOStreams/commit/7f2e4ff8f1e52db7f2f4ca702db0cd66d779aca1))
* **web:** send the party offset when it changes ([a902cc4](https://github.com/Viren070/AIOStreams/commit/a902cc4035af18b30b2be1268e6411450fe7ad4c))
* **web:** send the player the segments it skips ([df28a23](https://github.com/Viren070/AIOStreams/commit/df28a23d15f42cc0b0dce6d4e80dc640cd0642e4))
* **web:** send X-AIOStreams-* headers to servers listing clientHints ([b56f5c1](https://github.com/Viren070/AIOStreams/commit/b56f5c1c85611d9dc7672e0b5a687f3c5bbbb704))
* **web:** settle unsure subtitle syncs on when lines start and end ([394b73f](https://github.com/Viren070/AIOStreams/commit/394b73fc15b210864099b7b4d95ce2e26e151d80))
* **web:** show a retimed copy of subtitles made for another frame rate ([d56bc6b](https://github.com/Viren070/AIOStreams/commit/d56bc6b587c802149d3ba632e2f320133d24c651))
* **web:** show cover immediately on auto play first ([6a93d18](https://github.com/Viren070/AIOStreams/commit/6a93d189ece07cfb48f4c187677824a3891ce751))
* **web:** show home's Activity and Calendar buttons only with the bottom bar ([6936c8e](https://github.com/Viren070/AIOStreams/commit/6936c8ee44dc19891f2462f81e5a6af2b32d26a5))
* **web:** show keyframe thumbnails over the seek bar ([baa0035](https://github.com/Viren070/AIOStreams/commit/baa0035f2296a813343ea5edc70732dc4c2c987c))
* **web:** show notices at their index among the versions ([b63a30c](https://github.com/Viren070/AIOStreams/commit/b63a30cd4fa9bd4e0d86c7ccad3ff76c173a932f))
* **web:** show party reactions beside the open party sheet ([fee3b45](https://github.com/Viren070/AIOStreams/commit/fee3b4572eb088c5ab4ee129992021c14a37b6f7))
* **web:** show the audio output and memory in ExoPlayer's stats ([27e7b2e](https://github.com/Viren070/AIOStreams/commit/27e7b2ef49648243fdea2b0a903b38247a8359ec))
* **web:** show the cache size setting in the desktop app ([67c1f2f](https://github.com/Viren070/AIOStreams/commit/67c1f2f046ebdf2cb4359b1f713996269c5432ab))
* **web:** show the cache's time behind in Exo stats ([b73aa8d](https://github.com/Viren070/AIOStreams/commit/b73aa8d56b82ac82137dddfc679cbfdc3c701d68))
* **web:** show the channel setting in the Android app ([4b0f6ac](https://github.com/Viren070/AIOStreams/commit/4b0f6ac3022d8a15dc4c7a9f6b1cbd71caf9405c))
* **web:** show the seek-bar picture for arrow-key seeks only on TVs ([d4d00bf](https://github.com/Viren070/AIOStreams/commit/d4d00bf777d7b059cb583ddcf9a0da9b1495b8a6))
* **web:** skip a file's own subtitle its other subtitles don't back ([216ce6b](https://github.com/Viren070/AIOStreams/commit/216ce6b4fd3a4ba87ac36fe1fc9ef65e56c3ccd1))
* **web:** skip row titles and the hero's dots in arrow navigation everywhere ([33aa5ba](https://github.com/Viren070/AIOStreams/commit/33aa5ba5c215bf2bd91c9147a595126223585291))
* **web:** sort the merged Continue watching row by watch time ([62b2b6e](https://github.com/Viren070/AIOStreams/commit/62b2b6e539e04ba49304424b067f60d6f0d67f9b)), closes [#1483](https://github.com/Viren070/AIOStreams/issues/1483)
* **web:** suggest aiostreams.viren070.me's relay to servers without party info ([91a028e](https://github.com/Viren070/AIOStreams/commit/91a028ef23a1e8f7e9c8cce64cd481c228a7d6a1))
* **web:** support right-to-left layouts ([0e7f1e4](https://github.com/Viren070/AIOStreams/commit/0e7f1e4e4e43feee58ff89f7d8ecd0e655a15957))
* **web:** take a party's next titles from its queue ([b9af145](https://github.com/Viren070/AIOStreams/commit/b9af14508f4a95d14a3c7cfba0fd3541f8c44541))
* **web:** take remote commands from the session socket ([7c0a942](https://github.com/Viren070/AIOStreams/commit/7c0a94217de4b807557a148b8c3bf6e591db1516))
* **web:** title a report of a page restart as one ([5f76024](https://github.com/Viren070/AIOStreams/commit/5f76024172d435520839a054c49ace7aa15a0d7e))
* **web:** wrap every message in Lingui ([f04715e](https://github.com/Viren070/AIOStreams/commit/f04715ef1e44dca7a5b7d98e49545931622d00c7))


### Bug Fixes

* **config:** decrypt string and URL credentials set by the environment ([#1528](https://github.com/Viren070/AIOStreams/issues/1528)) ([795208e](https://github.com/Viren070/AIOStreams/commit/795208e502155df7ec503cf0a7da49a54729f47b)), closes [#1215](https://github.com/Viren070/AIOStreams/issues/1215)
* **frontend:** only refresh catalogs on catalog tab ([644dda6](https://github.com/Viren070/AIOStreams/commit/644dda67bd96f406d08fcddcf619434402224298))
* **jellyfin:** air an undated episode no earlier than the ones before it ([48a77e7](https://github.com/Viren070/AIOStreams/commit/48a77e7955f400a63d7bd51d84889ccdd966df23))
* **jellyfin:** keep separate users off the account's switch list ([68a0f69](https://github.com/Viren070/AIOStreams/commit/68a0f69b30abcc206b3030c2134fe762989aa876))
* **jellyfin:** leave subtitles marked no-store out of the cache ([762360a](https://github.com/Viren070/AIOStreams/commit/762360a301ef18b22469b28ba009c42653920be6))
* **jellyfin:** match default tracks by the addon's language names ([54b029b](https://github.com/Viren070/AIOStreams/commit/54b029bd0c077b1d42da954bfb89c7a17f9e9787))
* **jellyfin:** open a show whose default video is one of its episodes ([d87ce95](https://github.com/Viren070/AIOStreams/commit/d87ce95f05f4d1208a32e57828f63a7384cc848f))
* **jellyfin:** place season-less packed episodes by their match key ([d20066d](https://github.com/Viren070/AIOStreams/commit/d20066dae89ed90e34f6748a77a609b684022a86))
* **jellyfin:** play the session a client was given when its stream request names none ([38c060d](https://github.com/Viren070/AIOStreams/commit/38c060dc081e1ab63ca036f384562a6cba77390d))
* **jellyfin:** raise the per-configuration maxVersions limit to 500 ([#1517](https://github.com/Viren070/AIOStreams/issues/1517)) ([5cde591](https://github.com/Viren070/AIOStreams/commit/5cde591e45b665c9f85185920b5b503b5abf449a))
* **jellyfin:** resolve alias and PIN mounts for the session socket ([5449741](https://github.com/Viren070/AIOStreams/commit/5449741433ea314b60eda2b470459bacb775f774)), closes [#1554](https://github.com/Viren070/AIOStreams/issues/1554)
* **jellyfin:** return only the named version from PlaybackInfo ([f18557c](https://github.com/Viren070/AIOStreams/commit/f18557cf0842f9f80c8985e3cbe8e70d26905345))
* **jellyfin:** show production countries by name ([2919d45](https://github.com/Viren070/AIOStreams/commit/2919d4503420817ff81b726ea432ad1de01a8721)), closes [#1542](https://github.com/Viren070/AIOStreams/issues/1542)
* **metadata/tvdb:** tag the original-language title with its language ([cff9f70](https://github.com/Viren070/AIOStreams/commit/cff9f7092909bfe05094bebfa8e5af9c0727afba))
* send hash of host for reports ([0705e0f](https://github.com/Viren070/AIOStreams/commit/0705e0febf4ef49283898a6ae379fafd56d14108))
* **server:** cap the length of party and SyncPlay queues ([d5b47a9](https://github.com/Viren070/AIOStreams/commit/d5b47a97a2205a9372bfd5421a2d22206b371a90))
* skip merged catalog sources that don't declare a requested extra ([880bd5b](https://github.com/Viren070/AIOStreams/commit/880bd5ba25e800d90fa412da2bf7c25f332faa76))
* **ui:** measure a slider's thumb as the whole slider for key navigation ([78d8f10](https://github.com/Viren070/AIOStreams/commit/78d8f105eba7e193376c132ca050f103348af5c3))
* **web:** abort item and image fetches nothing waits on ([9fe977f](https://github.com/Viren070/AIOStreams/commit/9fe977fd67d45cf6b154542d46970c8cefeac37a))
* **web:** accept a slash after the host in party app links ([fbb961d](https://github.com/Viren070/AIOStreams/commit/fbb961d9c4c0ca360e06ae7e0bebceb9dd3a8492))
* **web:** change party playback speed only for a drift that lasts ([9ef673e](https://github.com/Viren070/AIOStreams/commit/9ef673ea817573285924f5ec0f8134e3a6628c2c))
* **web:** check downloads before finding the next episode's version ([4c66c83](https://github.com/Viren070/AIOStreams/commit/4c66c830ed78099b0a9cc7b8a240445912d68d5a))
* **web:** close the open player menu when another opens ([22d5d3c](https://github.com/Viren070/AIOStreams/commit/22d5d3c9f10980acb7e322bb9aca3f0caf469e73))
* **web:** compile dependencies to the build's browser targets ([bd1de5b](https://github.com/Viren070/AIOStreams/commit/bd1de5bc9720a9fbadfa0f990de7113db3decf7f))
* **web:** dont gate party settings on party feature ([e8e4a4c](https://github.com/Viren070/AIOStreams/commit/e8e4a4cd1252a7cad75678609430eaa9ed0cd13f))
* **web:** draw card focus rings outside the picture ([e3646bc](https://github.com/Viren070/AIOStreams/commit/e3646bc1b31bfc904779d074e86ad56ff1ae53c9))
* **web:** drop the focus ring from body and #root ([bc0e44e](https://github.com/Viren070/AIOStreams/commit/bc0e44e1bbbb1cab39daa2a29d63f30c4e94333a))
* **web:** enter a row lying between focus and the card in line with it ([c4f6c30](https://github.com/Viren070/AIOStreams/commit/c4f6c30e352408ed700c0e5d6d86458dffd5d51d)), closes [#1605](https://github.com/Viren070/AIOStreams/issues/1605)
* **web:** fill landscape cards from landscapePoster before the poster ([f3e0d0b](https://github.com/Viren070/AIOStreams/commit/f3e0d0b90ef27cd909344206a8effec2bae387a0))
* **web:** focus the custom CSS toast's Keep when applied from keys ([0480a86](https://github.com/Viren070/AIOStreams/commit/0480a86e56701f49f14fa0606c396ca94ef5186a))
* **web:** give the About page's Credits title its own context ([a58e39d](https://github.com/Viren070/AIOStreams/commit/a58e39d08b09e8901d65eb102c6cef8931a7d2d0))
* **web:** hide pages kept beneath others with visibility as well ([1526431](https://github.com/Viren070/AIOStreams/commit/15264311d664b1d1bbac195fd07dff7182aef9e6))
* **web:** hold a skip's seek-bar picture for a second ([451a155](https://github.com/Viren070/AIOStreams/commit/451a15598e4c388c37a1db5d53b027d6d8c1500b))
* **web:** keep a replaced artwork copy until it ages out ([7dcaa08](https://github.com/Viren070/AIOStreams/commit/7dcaa089972d417b5af7cac48c914ff1c4380406))
* **web:** keep a skip's seek-bar thumbnail up after the skip lands ([a35c64b](https://github.com/Viren070/AIOStreams/commit/a35c64b96ead48c99d5365b9045d6e51e3bfd25c))
* **web:** keep the TV rail's fading layers composited with will-change ([5aecddb](https://github.com/Viren070/AIOStreams/commit/5aecddbc2f900a440693d81e271adac0d4a59919))
* **web:** leave room for the focus ring in desktop rows ([927e0f4](https://github.com/Viren070/AIOStreams/commit/927e0f4498139d4d491ab46024e2e08c3a9def56))
* **web:** let up and down leave a text box from its first and last line ([025fe89](https://github.com/Viren070/AIOStreams/commit/025fe899509da79f9b3a9d5242ab0971547ccfc1))
* **web:** match track languages by the addon's language names ([0ecace3](https://github.com/Viren070/AIOStreams/commit/0ecace319818b7b2935af72195186737e7267cec)), closes [#1545](https://github.com/Viren070/AIOStreams/issues/1545)
* **web:** memoise the playback info query helpers ([909437d](https://github.com/Viren070/AIOStreams/commit/909437d09bc88055e698981fac9f38bf195b4e78))
* **web:** move along the player menu's stepper rows with left and right ([1a45f22](https://github.com/Viren070/AIOStreams/commit/1a45f2283c6fe22413e21b388a44ca34c2de9b28)), closes [#1559](https://github.com/Viren070/AIOStreams/issues/1559)
* **web:** move focus through a scrolled box before leaving it ([c6c52a1](https://github.com/Viren070/AIOStreams/commit/c6c52a165586c453a7001fca180a1f461f600495))
* **web:** name the badge summary's plural counts ([69b1a66](https://github.com/Viren070/AIOStreams/commit/69b1a661211ae2ca212891cedd1da2c41e66c19f))
* **web:** offer version fields only on servers that send them ([f142a47](https://github.com/Viren070/AIOStreams/commit/f142a4740550a1afafa89a445031045b10b62759))
* **web:** open drawers below the desktop app's window buttons ([226dd06](https://github.com/Viren070/AIOStreams/commit/226dd0682f39f583bbb8769bd7d6eb101f9539ff)), closes [#1548](https://github.com/Viren070/AIOStreams/issues/1548)
* **web:** open the version list with nothing focused on touch screens ([7bb7a63](https://github.com/Viren070/AIOStreams/commit/7bb7a63a3374a7db990c2a68404177b2716b4faf))
* **web:** paint the Android app's root in the page colour outside the player ([b5eeea3](https://github.com/Viren070/AIOStreams/commit/b5eeea37d34c7d107f037cab3855e57597064b8f)), closes [#1589](https://github.com/Viren070/AIOStreams/issues/1589)
* **web:** paint the page's scrollbar in the page colour ([930e8a0](https://github.com/Viren070/AIOStreams/commit/930e8a0464625cd797f75a5761c84633372c8753))
* **web:** pick the following hero's card on pointer moves, not enters ([754a4d1](https://github.com/Viren070/AIOStreams/commit/754a4d1983083198b9bd283e3a56060571bb6bb8))
* **web:** play a version's own address rather than the stream route ([fc8e554](https://github.com/Viren070/AIOStreams/commit/fc8e554c3b9fa6e1f971a6ffeca2e55f6d99b4aa))
* **web:** read buffered ranges from one snapshot ([10f9382](https://github.com/Viren070/AIOStreams/commit/10f9382bb64a3d2d7e06bbbb87ac7eda8d0ac79d))
* **web:** remember the subtitle type picked for a show ([657980e](https://github.com/Viren070/AIOStreams/commit/657980e0f7f9d17ad6c5f80a25df732fd1368300)), closes [#1617](https://github.com/Viren070/AIOStreams/issues/1617)
* **web:** return focus to a card after a dialog its menu opened ([ae8e7e5](https://github.com/Viren070/AIOStreams/commit/ae8e7e58a70aa3db70ef56e7e738bd38bb1bd588))
* **web:** return nothing from the calendar agenda's scroll ([3b54f0f](https://github.com/Viren070/AIOStreams/commit/3b54f0fbef47cffd248d45b5a4e970ff045fcd2a))
* **web:** reword the audio help for remembering picks per show ([3d4bcb6](https://github.com/Viren070/AIOStreams/commit/3d4bcb67a5181aaf492102d1ae168895b63df1f6))
* **web:** send a pending settings save before reading them back ([da601ca](https://github.com/Viren070/AIOStreams/commit/da601ca8d6e974e83326816d5d78f92508d59784))
* **web:** send a segment already skipped as offered ([8263f0a](https://github.com/Viren070/AIOStreams/commit/8263f0ac45b0e2efc6991712c582427d0867f7d4))
* **web:** size the shut TV rail's buttons to its icons ([ef055dc](https://github.com/Viren070/AIOStreams/commit/ef055dc32d35f2f87620fe1b27bd8f58453989c1))
* **web:** skip the navigation when a key press starts focus on a page ([6ffeab3](https://github.com/Viren070/AIOStreams/commit/6ffeab314b220f6c0cb5411276a6c4405bb37ad3))
* **web:** start Favourites on its first poster ([1c8ec8c](https://github.com/Viren070/AIOStreams/commit/1c8ec8cc0a4e244d72958bbbd2887ff94b46f309)), closes [#1550](https://github.com/Viren070/AIOStreams/issues/1550)
* **web:** start on Home after switching users or signing out ([b581499](https://github.com/Viren070/AIOStreams/commit/b5814996c628cb5b61846c6fb0a3da80ae8e6ec5)), closes [#1556](https://github.com/Viren070/AIOStreams/issues/1556)
* **web:** stop rejoining the last party when the app opens ([3f6e28a](https://github.com/Viren070/AIOStreams/commit/3f6e28a34c95b0e52c4f76b7a640e641ed3b64f0)), closes [#1549](https://github.com/Viren070/AIOStreams/issues/1549)
* **web:** take a party player's position from its soonest report ([1796aa0](https://github.com/Viren070/AIOStreams/commit/1796aa08a98889a0139384b9961560343c500e98))
* **web:** take Back in the profile PIN prompt ([b85c428](https://github.com/Viren070/AIOStreams/commit/b85c428d66e997cb96b0606c5bbddcad78e3802a)), closes [#1616](https://github.com/Viren070/AIOStreams/issues/1616)
* **web:** tie the item backdrop's fade to the image that loaded ([0c8b2f0](https://github.com/Viren070/AIOStreams/commit/0c8b2f0ec97696963b7e765b0a2af6a228ca92e5)), closes [#1553](https://github.com/Viren070/AIOStreams/issues/1553)
* **web:** treat a dialog holding focus itself as nothing focused for key moves ([9e7b84c](https://github.com/Viren070/AIOStreams/commit/9e7b84c6b9743261f9a6c7f1a60b3d0756212152))
* **web:** write single watched counts as whole plural messages ([d40f1e0](https://github.com/Viren070/AIOStreams/commit/d40f1e06039e631f1e1a0898c3bdf761733a642b))


### Performance Improvements

* **core:** index shared records' tags and refs in memory ([ec85729](https://github.com/Viren070/AIOStreams/commit/ec85729f691dd28f2b75ecc6714f8cf30caa3413))
* **core:** reject values that can't be encrypted before parsing them ([1565c5e](https://github.com/Viren070/AIOStreams/commit/1565c5eb1b52ba7d754b1fa33a6f87852b1ccdcd))
* **native:** convert thumbnails straight to JPEG YCbCr ([2fe4fe1](https://github.com/Viren070/AIOStreams/commit/2fe4fe1d7cfd04859dffa74c01c0b935639d779d))
* **native:** fetch several keyframes at once for thumbnails ([4a67d31](https://github.com/Viren070/AIOStreams/commit/4a67d314ed9ef185752e5f570613e67e64f1d0ec))
* **native:** fetch the next thumbnail's keyframe while one renders ([41d2ecc](https://github.com/Viren070/AIOStreams/commit/41d2eccfcdef127526c39f2d141ac69eb244d5cc))
* **native:** size keyframe reads from recent keyframe sizes ([ea1c4ca](https://github.com/Viren070/AIOStreams/commit/ea1c4cadbe40f30571c33a8dddaf81efd51a1ee3))
* **web:** fade cards and artwork in only when on screen ([4e094f3](https://github.com/Viren070/AIOStreams/commit/4e094f385646daedd063215dd5510854b5fe8df5))
* **web:** find glide layers among a box's children ([131fbfd](https://github.com/Viren070/AIOStreams/commit/131fbfd98f51174107e9008a919923ee176d0a75))
* **web:** reuse the subtitle matcher's curves ([484887d](https://github.com/Viren070/AIOStreams/commit/484887dc45c2153e1645be8a449e8c24e4529d6a))
* **web:** save a query's answer once it stops changing ([ab1d274](https://github.com/Viren070/AIOStreams/commit/ab1d27459b1c35abf0f7a3a3f76ab8c9e226c135))


## v2.36.0

## [2.36.0](https://github.com/Viren070/AIOStreams/compare/v2.35.9...v2.36.0) (2026-10-12)


### Features

* **android:** add an ExoPlayer engine ([764da86](https://github.com/Viren070/AIOStreams/commit/764da86a4b82d5ace8caa42490a57122700f90bc))
* **android:** add the Android app ([2132721](https://github.com/Viren070/AIOStreams/commit/21327210619cdbb5c3f7fe3b35fc958341e30ac3))
* **android:** pass surround audio through by what the output reports ([6cc6828](https://github.com/Viren070/AIOStreams/commit/6cc6828e1afeb49773bf7244445d241e8340085a))
* **android:** run voice search in the app ([cf0939c](https://github.com/Viren070/AIOStreams/commit/cf0939ca54d3c5946c92dc0ec593940aaa591ad8))
* **dashboard:** add a media info page ([b94647c](https://github.com/Viren070/AIOStreams/commit/b94647c26d9207823ff11b03de2832ad812608f6))
* **db:** add the media info tables ([ac93a93](https://github.com/Viren070/AIOStreams/commit/ac93a93822ad0523de32b4883d43ebe7a804806a))
* **docker:** ship a minimal ffprobe ([472def3](https://github.com/Viren070/AIOStreams/commit/472def37da5a9ee55f66f27b2cabe9badf0d9cad))
* **frontend:** list every device the app runs on under Save & Install ([6b33433](https://github.com/Viren070/AIOStreams/commit/6b33433a952766791e39551ce957f86cd6a3e523))
* **jellyfin-web:** add {scheme} to the player link ([9db03c5](https://github.com/Viren070/AIOStreams/commit/9db03c542df26f7d04fde93965a04c2ace468835))
* **jellyfin-web:** add a Cache settings tab ([f9c38fe](https://github.com/Viren070/AIOStreams/commit/f9c38fe09ad7c557a68ef4fc3d7cb56880bf1b11))
* **jellyfin-web:** add Android players to the player choice ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** add Android players to the player choice ([26a3050](https://github.com/Viren070/AIOStreams/commit/26a30502ffd6287383286725882a5b998ee5af0e))
* **jellyfin-web:** add Original language and a default-track switch to the audio settings ([4687ea2](https://github.com/Viren070/AIOStreams/commit/4687ea27ef14289103d6c68c8df82458b18f608f))
* **jellyfin-web:** add subtitle files by dropping or picking them ([76d7116](https://github.com/Viren070/AIOStreams/commit/76d711697a9687dab0fbf0be1daa575bd4063664))
* **jellyfin-web:** add webOS and Tizen hosts ([68241bf](https://github.com/Viren070/AIOStreams/commit/68241bf687e009a4df1dffb27a24b36f2d162d32))
* **jellyfin-web:** ask whether anyone is still watching before playing on ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** ask whether anyone is still watching before playing on ([2d52201](https://github.com/Viren070/AIOStreams/commit/2d52201b9b3f95e10a63692f2c4c5b4e8419d4c3))
* **jellyfin-web:** block the webOS screensaver while the video plays ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** block the webOS screensaver while the video plays ([340818f](https://github.com/Viren070/AIOStreams/commit/340818fbf595a4888467df65d08838f6bbac4375))
* **jellyfin-web:** describe desktop playback failures from mpv's http error ([21f24bf](https://github.com/Viren070/AIOStreams/commit/21f24bfd4fb0b2a0edfc79474c9219afc02b3cf6))
* **jellyfin-web:** download movies, episodes and seasons ([3ad7fad](https://github.com/Viren070/AIOStreams/commit/3ad7fad41787e8ed40895f4669198a7e54e00753))
* **jellyfin-web:** hand downloads to the Jellyfin Android app ([3a31b1f](https://github.com/Viren070/AIOStreams/commit/3a31b1f198fb1f14a130e873f56efd3c5212cd7d))
* **jellyfin-web:** hand the Android app's player the episodes that follow ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** hand the Android app's player the episodes that follow ([25e6f6f](https://github.com/Viren070/AIOStreams/commit/25e6f6f0b7719a0500ff569de4a19da2f4d57de6))
* **jellyfin-web:** list films on the calendar ([05863cb](https://github.com/Viren070/AIOStreams/commit/05863cbb4a5889a8054ef8e8b0a8f46c3524a807))
* **jellyfin-web:** look up the next episode's versions before its prompt ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** look up the next episode's versions before its prompt ([fe2a9dd](https://github.com/Viren070/AIOStreams/commit/fe2a9dd00579cdc5a841df4c18fd24df6cb9250c))
* **jellyfin-web:** play finished downloads from their files ([d377c50](https://github.com/Viren070/AIOStreams/commit/d377c501c0d46f4d30bce4d9f35a2d83918de22f))
* **jellyfin-web:** play through AVPlay on Samsung TVs ([71c8c85](https://github.com/Viren070/AIOStreams/commit/71c8c85fc6e0aee3b1cf251c6b436797bb1a51df))
* **jellyfin-web:** redesign server picker ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** redesign server picker ([8c24862](https://github.com/Viren070/AIOStreams/commit/8c248623c0bd99e754865f97c2926167d4f998b1))
* **jellyfin-web:** refresh watch state on the server socket's pushes ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** refresh watch state on the server socket's pushes ([db18973](https://github.com/Viren070/AIOStreams/commit/db189732477b3435cea49554ebc5ad91fc1565e4))
* **jellyfin-web:** remember audio and subtitle picks per show ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** remember audio and subtitle picks per show ([3926dda](https://github.com/Viren070/AIOStreams/commit/3926ddad5b10e1e2ef1703da3b4cd49975b56898))
* **jellyfin-web:** replace the external player link with a player choice ([3578bd3](https://github.com/Viren070/AIOStreams/commit/3578bd32e8c14cbc4b908e28b2a51ced4e2e05a6))
* **jellyfin-web:** save pages and artwork on the device ([bb28b3b](https://github.com/Viren070/AIOStreams/commit/bb28b3b84d6f982d5785e6c95b1c45da42d66e00))
* **jellyfin-web:** show filler and recap marks and skip them when playing on ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** show filler and recap marks and skip them when playing on ([451321c](https://github.com/Viren070/AIOStreams/commit/451321c422a69b646817046de091db241528ac84))
* **jellyfin-web:** start the desktop players on the server's default tracks ([fb4ded4](https://github.com/Viren070/AIOStreams/commit/fb4ded4ac2f8b78b7efa3a3bf90cb5ab22f2ff39))
* **jellyfin-web:** switch audio tracks the video element lists ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** switch audio tracks the video element lists ([f5a76a9](https://github.com/Viren070/AIOStreams/commit/f5a76a949a76ba38076906a76a15e7e0a42d0b0b))
* **jellyfin-web:** use relative asset paths in the standalone build ([ca58c71](https://github.com/Viren070/AIOStreams/commit/ca58c71251ffd3aba1ef12bbcfcaa5813822e217))
* **jellyfin:** add ordered audio and subtitle language lists ([7df1d5f](https://github.com/Viren070/AIOStreams/commit/7df1d5f7a771c53af40425236851bd56dfad975c))
* **jellyfin:** add watchlisted shows and films to the calendar ([f5abba0](https://github.com/Viren070/AIOStreams/commit/f5abba05d5b503250989b321d4f12f0b5f933e3e))
* **jellyfin:** answer search hints from LumiereDB or Cinemeta ([03ef417](https://github.com/Viren070/AIOStreams/commit/03ef41737acbbf2a8a9641ca352c6d291c38614c))
* **jellyfin:** ask a locked user's own session for its PIN on a switch ([296bc7e](https://github.com/Viren070/AIOStreams/commit/296bc7ef01413f926005f6109351597b261f4d94))
* **jellyfin:** fill a version's tracks from stored probes on play ([ba78352](https://github.com/Viren070/AIOStreams/commit/ba7835290f747bb9f3a39a2d395af0b3b2fb8720))
* **jellyfin:** keep a user separate, on a sign-in address of their own ([0b1fe3b](https://github.com/Viren070/AIOStreams/commit/0b1fe3b0c2c1c91b31dd239f97c1dd47b24f1f1d))
* **jellyfin:** mark filler and recap episodes ([e17da78](https://github.com/Viren070/AIOStreams/commit/e17da78d347e645f070d615f5c28106faac7839c))
* **jellyfin:** rank subtitle tracks by type ([d37af67](https://github.com/Viren070/AIOStreams/commit/d37af67e46ce9b8180250a19ce92bf4c61863e6f)), closes [#1485](https://github.com/Viren070/AIOStreams/issues/1485)
* **jellyfin:** read named trailers and video links ([52c9490](https://github.com/Viren070/AIOStreams/commit/52c949084f74f39ee3d98e8bec63d984f327bc31))
* **media-info:** add a tags list to audio tracks ([6ff91b8](https://github.com/Viren070/AIOStreams/commit/6ff91b8737c26da71ccbfbedaf615e223323e0aa)), closes [#1443](https://github.com/Viren070/AIOStreams/issues/1443)
* **media-info:** fill stream details from stored probes ([5c8b38d](https://github.com/Viren070/AIOStreams/commit/5c8b38dbc11fa7cbf349932d254bdda75dc022a2))
* **media-info:** probe played files with ffprobe ([d0f43a3](https://github.com/Viren070/AIOStreams/commit/d0f43a3a1b3b7bf1e7bf011f57798b4ef7640ed9))
* **media-info:** serve stored media info to other instances ([57d0156](https://github.com/Viren070/AIOStreams/commit/57d0156030ed25642b4233ab513ed5899fabbefa))
* **media-info:** store what StremThru and RemuxDB report ([64aaffd](https://github.com/Viren070/AIOStreams/commit/64aaffd98efe3aaa1c2ae5e229a99404d29ed28b))
* **parser:** read more stream details from behaviorHints ([d56784e](https://github.com/Viren070/AIOStreams/commit/d56784ed024a8bb618a2c94f280f25a5616fc0b8))
* **parser:** read stream duration from behaviorHints.duration ([0b9b655](https://github.com/Viren070/AIOStreams/commit/0b9b655353fce57333f81bfbcf239b1e05dcfe00)), closes [#1340](https://github.com/Viren070/AIOStreams/issues/1340)
* **presets:** parse the torrent file and title where addons name them ([4a27d2b](https://github.com/Viren070/AIOStreams/commit/4a27d2b5bdaaaafc90ffc4f5c09c9236d27e78dd))
* **proxy:** name a trusted stream's release in its proxy token ([c3cedcf](https://github.com/Viren070/AIOStreams/commit/c3cedcfe5b0f6b6227a15e92808b32f39952c586))
* **remuxdb:** contribute and match Prowlarr and NZBHydra results via the indexer info URL ([#1450](https://github.com/Viren070/AIOStreams/issues/1450)) ([a046b0e](https://github.com/Viren070/AIOStreams/commit/a046b0ebb2e410cc50457fe6cd204b3870daeba8))
* **remuxdb:** contribute stored probes ([253cea2](https://github.com/Viren070/AIOStreams/commit/253cea295619f1460adb5c29407ae64da0e9c856))
* **remuxdb:** enable contributing by default ([99b6dc3](https://github.com/Viren070/AIOStreams/commit/99b6dc3f907490ffa9e24eeb6c1f008609f1867c))
* **remuxdb:** look streams up by default ([99b6dc3](https://github.com/Viren070/AIOStreams/commit/99b6dc3f907490ffa9e24eeb6c1f008609f1867c))
* **remuxdb:** turn contributing off by default ([b0e6e9d](https://github.com/Viren070/AIOStreams/commit/b0e6e9dc493ea4bf36ec6bd55295bb4d4d804713))
* **tv:** add a boot script for old TVs and startup errors ([81ef44c](https://github.com/Viren070/AIOStreams/commit/81ef44cabaf7f996b3312119feb74512e602c123))
* **tv:** build the Tizen package unsigned ([82e7ac3](https://github.com/Viren070/AIOStreams/commit/82e7ac33523b8333b33484d3bd40ffdcf7ed782e))
* **tv:** package the standalone web app for webOS and Tizen ([915b925](https://github.com/Viren070/AIOStreams/commit/915b9251bd0b86b9fdc7bdf09f56db657fae0d1b))
* **ui:** add a right-side sheet to the modal ([74b41b9](https://github.com/Viren070/AIOStreams/commit/74b41b9b535946b3377fa12531b1e91072a14d57))
* **ui:** leave a zero decimal off formatBytes ([90dfa0b](https://github.com/Viren070/AIOStreams/commit/90dfa0b808b3ed733e6ed5494d414b5e75a8a285))
* **watch-state:** date a stop that arrives late by LastPlayedDate ([b02a09c](https://github.com/Viren070/AIOStreams/commit/b02a09cb36aef73f2e57297792b5b41abab40166))
* **web:** add a Dolby Vision switch that plays the HDR10 picture instead ([e27353e](https://github.com/Viren070/AIOStreams/commit/e27353e9883eb8ff5ef62fa11e821bfbe30c489b))
* **web:** add a follow hero that keeps its artwork in the top corner ([5fe6e6d](https://github.com/Viren070/AIOStreams/commit/5fe6e6d81cc57b134db653e48827a49e6c98a8ce))
* **web:** add a frame-rate matching setting on Android TVs ([9f3832c](https://github.com/Viren070/AIOStreams/commit/9f3832ce229825b4a8097a53ab220628ddd59baa))
* **web:** add a solid navigation bar background and put navigation settings in one card ([1cb3cf0](https://github.com/Viren070/AIOStreams/commit/1cb3cf058d43196a7ab9dd2672720428ecc8cfbc))
* **web:** add a tooltip to the rating button ([03554dc](https://github.com/Viren070/AIOStreams/commit/03554dc4c2797a2e2882d12967967e52a02aec0c))
* **web:** add a touch rail for wide touch screens ([2744be1](https://github.com/Viren070/AIOStreams/commit/2744be19c177a1ca9ed98257cbb364bd6b323e5b))
* **web:** add a trailer player and a sheet of named trailers ([b1c84c1](https://github.com/Viren070/AIOStreams/commit/b1c84c17ab15cdd371e0dc1a29dacc3a0fee4714))
* **web:** add a tunneled playback setting on Android TVs ([433d8e2](https://github.com/Viren070/AIOStreams/commit/433d8e2cee726f9c958f400b6226e839101d0e5a))
* **web:** add a TV layout ([454db91](https://github.com/Viren070/AIOStreams/commit/454db91dc8154e6b3973885427bf8dc01c3fbef9))
* **web:** add a voice search button on Android TVs ([46ef56f](https://github.com/Viren070/AIOStreams/commit/46ef56fe5dc5744340bc3e1c5eb433bec7ce8530))
* **web:** add an Android app section to the settings ([be699af](https://github.com/Viren070/AIOStreams/commit/be699affd7273a491314d883b5bb07f13da107f0))
* **web:** add an Automatic player engine and make it the default ([2549a50](https://github.com/Viren070/AIOStreams/commit/2549a50f2a3433c295ad7cb0bc14c549afadb931))
* **web:** add an episode list to the player ([34e808b](https://github.com/Viren070/AIOStreams/commit/34e808b2cfc7c0a7f8e90dec6b149e611dd314f8)), closes [#1462](https://github.com/Viren070/AIOStreams/issues/1462)
* **web:** add an only-on-Wi-Fi download setting for the Android app ([20613bd](https://github.com/Viren070/AIOStreams/commit/20613bd6213a8d2f5c3d2612d5479c4f77ba2026))
* **web:** add data-nav-exit focus boxes ([83e09ab](https://github.com/Viren070/AIOStreams/commit/83e09abee29b42fceff18cc4e8e4b5b11fd75a48))
* **web:** add data-ui hooks to the parts that had none ([7555445](https://github.com/Viren070/AIOStreams/commit/755544587cc5c42dddb8559514fc75e4f9e37325))
* **web:** add floating and corner side rails ([35533ed](https://github.com/Viren070/AIOStreams/commit/35533ed3315ddf50a1038bdeea0d244704d6b622))
* **web:** add picture-in-picture and background playback settings for the Android app ([c400399](https://github.com/Viren070/AIOStreams/commit/c40039938eba71610ef1a6a3026f7c65fb42b2cb))
* **web:** allow the following hero on TVs ([2f2fba5](https://github.com/Viren070/AIOStreams/commit/2f2fba5e0fedd943f2addc349177deba1ad2d075))
* **web:** ask who's watching when the app opens ([2c02c13](https://github.com/Viren070/AIOStreams/commit/2c02c1391e5d5841f8b8e09fc3c3fc7b0f326053))
* **web:** blur liquid glass without its bend while it resizes ([fb6a4bd](https://github.com/Viren070/AIOStreams/commit/fb6a4bdd630f7989a8b18b63fa0a12a2dfdaa510))
* **web:** bring the page to its top for focus in the item header ([dc6a50b](https://github.com/Viren070/AIOStreams/commit/dc6a50b3829b052bac00e0abb1561b4be4dfe47f))
* **web:** choose the Android app's player engine ([0bef3a4](https://github.com/Viren070/AIOStreams/commit/0bef3a4f4686e78445c275b18063af8ec5906dc6))
* **web:** crossfade the home hero's titles with a swipe ([93d4407](https://github.com/Viren070/AIOStreams/commit/93d44072c2ce7a1b9528a1c7c6bb1870094e7461))
* **web:** draw ExoPlayer's statistics over the player ([4098e26](https://github.com/Viren070/AIOStreams/commit/4098e26988cebde9e92eff1d7e1a586fab849878))
* **web:** drop copying stream links on TVs ([6254b27](https://github.com/Viren070/AIOStreams/commit/6254b27cd02c8e0b1bed0bed8e299df8881a01a0))
* **web:** drop downloads on Android TV ([87fabc4](https://github.com/Viren070/AIOStreams/commit/87fabc471c66cc62a18bf90178f658992efdd14c))
* **web:** drop the follow hero's buttons on TVs ([7e50285](https://github.com/Viren070/AIOStreams/commit/7e50285682d6cd0c75ebb75d7da084fb0c9ec07f))
* **web:** drop the Shortcuts settings tab on TVs ([61b6f8b](https://github.com/Viren070/AIOStreams/commit/61b6f8b2629686593fd74ef6e63a5c415c8d69b4))
* **web:** drop the versions filter on TVs ([62b0cd3](https://github.com/Viren070/AIOStreams/commit/62b0cd3fe414b745b3a142029ebf3dfb5222beae))
* **web:** enter a focus group from outside at the start of its row ([2e9a4f0](https://github.com/Viren070/AIOStreams/commit/2e9a4f087cd62782abbcaadbc6d8d5568a7bd5b6))
* **web:** export the watch history through the Android app ([e5e6830](https://github.com/Viren070/AIOStreams/commit/e5e6830d09b9610b5928a7b4a73b92dd2527c505))
* **web:** fill focused list rows instead of outlining them ([6f0a4a3](https://github.com/Viren070/AIOStreams/commit/6f0a4a3327beaa801f6101a3ddc20cae51331614))
* **web:** fit the sign-in pickers to a remote ([d5a34cf](https://github.com/Viren070/AIOStreams/commit/d5a34cf987326e6a90dbec85ffeec134863577ae))
* **web:** float a TV's top bar over the page on glass ([231101f](https://github.com/Viren070/AIOStreams/commit/231101f0089f06c3a1bdcf9c86dec95240f093b6))
* **web:** focus an item page's Play when keys open it ([d05c1ef](https://github.com/Viren070/AIOStreams/commit/d05c1efd0b5a35e75ec39982ec8e34dc67c1490c))
* **web:** focus the first item on Select with nothing focused ([e07653e](https://github.com/Viren070/AIOStreams/commit/e07653eb2520a935850acf96fd79d2e3cfc306bd))
* **web:** give liquid glass a wider, stronger rim and edge highlights ([2e0b379](https://github.com/Viren070/AIOStreams/commit/2e0b379a2c3801c50f8345e3b5b1e2cb4cd217c8))
* **web:** give the Android and Android TV apps their own client names ([3fc3502](https://github.com/Viren070/AIOStreams/commit/3fc3502565ca582739c05e742d91f0b1b7f2d5e4))
* **web:** glide keyed scrolls on a spring of our own ([f7710b1](https://github.com/Viren070/AIOStreams/commit/f7710b12a00ff2404135cf92f2e7224cca9a296c))
* **web:** hear back from external players in the Android app ([73138d6](https://github.com/Viren070/AIOStreams/commit/73138d6a605428370dc36b7cbded8f3a803538d4))
* **web:** hide an episode's buttons on TVs and add Details to its menu ([13340e3](https://github.com/Viren070/AIOStreams/commit/13340e3418116c6ca060cb048c014d939347e59d))
* **web:** hide external links and skip the hero's dots on TVs ([f11a7c5](https://github.com/Viren070/AIOStreams/commit/f11a7c5ab34dcd49972c12f9cbe567e41a9a06f4))
* **web:** hide scrollbars on TVs ([4b98f25](https://github.com/Viren070/AIOStreams/commit/4b98f2559a81d02baf8b67c7c08db33bb5271454))
* **web:** hide the player's controls on Back before leaving on a TV ([a6b5424](https://github.com/Viren070/AIOStreams/commit/a6b5424d005efabec45bec7682098d42a716c87e))
* **web:** keep a show's Play button in place while its next episode loads ([bf5e3cd](https://github.com/Viren070/AIOStreams/commit/bf5e3cd5dcae510fea1e4cf053e56bf0f5b670fd))
* **web:** keep subtitles above the player's controls while they show ([19a0d62](https://github.com/Viren070/AIOStreams/commit/19a0d622a8faea41e33c25fdf9d5526c0da245a6))
* **web:** land focus where it last was in rows, grids and lists ([712f2fc](https://github.com/Viren070/AIOStreams/commit/712f2fcdb884e11a5f77d1a462300b8d9904b922))
* **web:** leave volume out of the player on TVs and touch screens ([273140a](https://github.com/Viren070/AIOStreams/commit/273140a0160e39a2eaf37c0fea120ba4958c3a07))
* **web:** let a held key's action run until the key is let go ([201d55e](https://github.com/Viren070/AIOStreams/commit/201d55e188f7a89c80571ff8e8c48904865d1ed0))
* **web:** list only the user's subtitle languages in the subtitle menu ([0afe744](https://github.com/Viren070/AIOStreams/commit/0afe74400f59c535f4ec9a871579cb5d4172543f)), closes [#1490](https://github.com/Viren070/AIOStreams/issues/1490)
* **web:** list versions in a drawer over the player and on short screens ([957fc44](https://github.com/Viren070/AIOStreams/commit/957fc441da5d26632f5004f9d189b6e53d321503))
* **web:** list versions in a side sheet over the player ([6510fc7](https://github.com/Viren070/AIOStreams/commit/6510fc788bc9b529c83679d1e77e2571dc6acaf4))
* **web:** mark a focused settings tab on its sliding marker ([f5bec52](https://github.com/Viren070/AIOStreams/commit/f5bec52235fb090f01e26d884af36c0374ef97c6))
* **web:** mark webOS and Tizen as TVs ([cd01056](https://github.com/Viren070/AIOStreams/commit/cd01056ba4bebd130c2b41e57b79c0e6f6dd01d7))
* **web:** offer a ready update in a dialog on TVs ([6bbe727](https://github.com/Viren070/AIOStreams/commit/6bbe727487c6358d67fa3d96be6a62a68b9a86a1))
* **web:** offer the other engine on the Android app's error screen ([1e63e1e](https://github.com/Viren070/AIOStreams/commit/1e63e1e40fa7210dbfdc264c1965965dc505e6bd))
* **web:** open a TV's keyboard on Select rather than on focus ([bd9ad67](https://github.com/Viren070/AIOStreams/commit/bd9ad679ba26a034e267b99bea5ea5b473a7ccb3))
* **web:** open a user's own address on their sign-in ([2e48202](https://github.com/Viren070/AIOStreams/commit/2e482020b6b9e07166808cbc8d76a458237dad78))
* **web:** play full screen in landscape in the Android app ([58a6550](https://github.com/Viren070/AIOStreams/commit/58a65508286218274ae682e90899b1ff67d96d7e))
* **web:** play full screen on tablets in the app ([beee186](https://github.com/Viren070/AIOStreams/commit/beee186d02697a6b82ffb769841a7f32b5dc477d))
* **web:** press a showing skip button on Select ([05a6079](https://github.com/Viren070/AIOStreams/commit/05a607916af5f8d88ccb05987cc9fa9230bdfdc4)), closes [#1477](https://github.com/Viren070/AIOStreams/issues/1477)
* **web:** put a TV's keyboard away on its own Enter ([439c860](https://github.com/Viren070/AIOStreams/commit/439c8601e6557f5531a7e0cf55c51e735f701660))
* **web:** remove a recent search from its context menu ([4565884](https://github.com/Viren070/AIOStreams/commit/456588426f0ab077ae3bb13e11216ca00468babb))
* **web:** reuse the server's kept version list in the player ([edac5c2](https://github.com/Viren070/AIOStreams/commit/edac5c2ef161ef88a03e8c6a994e7f6c30015e48)), closes [#1488](https://github.com/Viren070/AIOStreams/issues/1488)
* **web:** rework the player's controls ([bb9b11f](https://github.com/Viren070/AIOStreams/commit/bb9b11ff148ee0a00defd7da9f2ee4b7ae12646f))
* **web:** run a button's hold action on a held Select ([e4b2452](https://github.com/Viren070/AIOStreams/commit/e4b2452eb19323caf7dabbfffafde59598d7fefb))
* **web:** say which picture fit the button picked ([3902c74](https://github.com/Viren070/AIOStreams/commit/3902c74a9f6a4d051a4cb5c2fc6936ce337904f7))
* **web:** scroll to the top when the rotating hero takes focus ([c098b24](https://github.com/Viren070/AIOStreams/commit/c098b24553e0865faf8da5781479bc9e62bbbb05))
* **web:** seek with a double tap and swipe for brightness and volume on touch ([d1d51a6](https://github.com/Viren070/AIOStreams/commit/d1d51a67e7a63e9589779808354f6f58cdeaeb2e))
* **web:** send Back into a TV's navigation from the pages it leads to ([36f1b2f](https://github.com/Viren070/AIOStreams/commit/36f1b2f389d6999fb31eee42ea060b4bbf3294db))
* **web:** send the backdrop as now-playing artwork ([3dae86e](https://github.com/Viren070/AIOStreams/commit/3dae86eb60444feddb521c5cf298419ae9b98745))
* **web:** show the display's HDR types and the Dolby Vision route in ExoPlayer's statistics ([c23dc88](https://github.com/Viren070/AIOStreams/commit/c23dc8810629a31ba6e361111ac940a3339f3adc))
* **web:** show the passthrough switch in the Android app ([76bf5de](https://github.com/Viren070/AIOStreams/commit/76bf5deadcb320ebfb759f6551be5406471e575a))
* **web:** show the picture-in-picture setting only where the device has it ([65e7798](https://github.com/Viren070/AIOStreams/commit/65e779858f5debe537825f868c8e752f8b1347cf))
* **web:** show the player's controls on Up and Down on TVs ([29ddbbd](https://github.com/Viren070/AIOStreams/commit/29ddbbd4df15f3240e60fee28cefb695d77252ca))
* **web:** show where a run of skips is headed on the seek bar ([ea29cff](https://github.com/Viren070/AIOStreams/commit/ea29cff5a0770416971465c9f7c22c247e8f94d7)), closes [#1478](https://github.com/Viren070/AIOStreams/issues/1478)
* **web:** skip row headers and hide minor buttons on TVs ([c83f694](https://github.com/Viren070/AIOStreams/commit/c83f694162203a54bb451aa121379518b9c57520))
* **web:** slide a TV's top bar away while focus is in the following hero's rows ([3c5fa80](https://github.com/Viren070/AIOStreams/commit/3c5fa80538640e25e9f043d2de1b4667e2b8b059))
* **web:** start Discover's focus on its first card ([fc794c9](https://github.com/Viren070/AIOStreams/commit/fc794c9ba328ab83bdc397ef10c7be9ee3a80c4d))
* **web:** start the version picker on the first version for keys ([209e0fe](https://github.com/Viren070/AIOStreams/commit/209e0fea42f11b038831167a1419dab4cfb1fc95))
* **web:** step through the TV hero's titles with Left and Right ([039afbc](https://github.com/Viren070/AIOStreams/commit/039afbc004026a961bc33bd5c201e3ae3116ecf1))
* **web:** suggest titles from search hints while typing ([9f36d38](https://github.com/Viren070/AIOStreams/commit/9f36d38c4ceb92309834c647ec979ddab9748367)), closes [#1491](https://github.com/Viren070/AIOStreams/issues/1491)
* **web:** take ordered audio and subtitle language lists ([fe8b99c](https://github.com/Viren070/AIOStreams/commit/fe8b99cd2da1e5c4f637f7a0ab741fb6d6d46844))
* **web:** take the Android app's Back ([fb93b47](https://github.com/Viren070/AIOStreams/commit/fb93b47ee602c1b1b0a0fb1d8186f9e3f5f77564))
* **web:** thicken card focus rings on TVs ([56bf856](https://github.com/Viren070/AIOStreams/commit/56bf856416eafbf7eed79c68766dab152cb9eb23))
* **web:** toggle playback with Enter on the seek bar ([42a6d41](https://github.com/Viren070/AIOStreams/commit/42a6d411f461791fff2b6e2fb8d6cb08532c49eb)), closes [#1474](https://github.com/Viren070/AIOStreams/issues/1474)
* **web:** toggle the player's controls with a tap ([5d5df5e](https://github.com/Viren070/AIOStreams/commit/5d5df5e04ee09f6c920c51b9a953a2fa22b132d2))
* **web:** wrap focus across card grid rows ([ba46baa](https://github.com/Viren070/AIOStreams/commit/ba46baa22e9a32d3b717c4afd16481db67146dbf))


### Bug Fixes

* **cache:** drop a buffered sql write on delete ([c2e6bdd](https://github.com/Viren070/AIOStreams/commit/c2e6bdd3e0803979f5daf30ca6e9efc12b2aad51))
* **core:** drop "Usenet" from the built-in usenet service's known names ([28fa990](https://github.com/Viren070/AIOStreams/commit/28fa990d0f33eaa5c18ebb1e648d6fb2ca121812))
* **core:** only type a stream as external when it has no url ([0f8a13d](https://github.com/Viren070/AIOStreams/commit/0f8a13de0c2cefff5954b81cd42c3aa84b520a16)), closes [#1375](https://github.com/Viren070/AIOStreams/issues/1375)
* **core:** trust a confirmed-empty media probe over a stale guess ([#1437](https://github.com/Viren070/AIOStreams/issues/1437)) ([f156e27](https://github.com/Viren070/AIOStreams/commit/f156e275b61d1eaa20c5fcc29d3b10b6da7c7d63))
* **dedupe:** copy probed tracks from a duplicate that lists them ([aeb4f2f](https://github.com/Viren070/AIOStreams/commit/aeb4f2fb91f72ff1620a34118552ac58edb1dc43))
* **frontend:** add no-referrer to the marketplace and reorder modal logos ([37ff00f](https://github.com/Viren070/AIOStreams/commit/37ff00fe251fc50b87a36dfad7912caf229fbf6b))
* **http:** include the path's directory in indexer cooldown keys ([ed4944f](https://github.com/Viren070/AIOStreams/commit/ed4944ffb87482933b34b9b900a20268dd0dfb28))
* **jellyfin-web:** clear only the position on remove from continue watching ([c66e99f](https://github.com/Viren070/AIOStreams/commit/c66e99fef2d4c3d94907120a6d49355d2c6d5a54))
* **jellyfin-web:** hold Play to list the versions of a resume ([cebbc23](https://github.com/Viren070/AIOStreams/commit/cebbc2343f8a71e3e90114d3efc56753c99bdf97))
* **jellyfin-web:** hold Play to list the versions of a resume ([0c26e7b](https://github.com/Viren070/AIOStreams/commit/0c26e7b61b1e4d62ab2dfb0e5dbae8ad20b1d1a0))
* **jellyfin-web:** keep the picked season in the item page's address ([b9692d9](https://github.com/Viren070/AIOStreams/commit/b9692d93362e5bfd03da09a74440ed17dc57186a))
* **jellyfin-web:** replace the player controls with the error screen ([c34b7b1](https://github.com/Viren070/AIOStreams/commit/c34b7b1fe27f31300c12539faac5731720214eea))
* **jellyfin:** list a probed file's streams in the file's order ([873d42f](https://github.com/Viren070/AIOStreams/commit/873d42f522b31a90fe87b96bc3541cf74802f239))
* **jellyfin:** pick each version's default tracks from the user's settings ([0b98582](https://github.com/Viren070/AIOStreams/commit/0b985824b07a74cc101697e190d7b7597c1748b2))
* **jellyfin:** return a user's saved settings from /Users/{id} ([fda114a](https://github.com/Viren070/AIOStreams/commit/fda114aa3431bc3577b4477387866cfd40369c27))
* **jellyfin:** serve the sign-in picker's avatars before signing in ([4a2d369](https://github.com/Viren070/AIOStreams/commit/4a2d3691022e2ab90f6054dc102df0b9c18574ef))
* **media-info:** merge rows for one file before storing a batch ([533a3bc](https://github.com/Viren070/AIOStreams/commit/533a3bc448e84e902b17ead9819041d9d0115aa5))
* **media-info:** read UTF-8 file names from Content-Disposition ([7673006](https://github.com/Viren070/AIOStreams/commit/7673006c06482b19ea2ea13550006a37811fb46c))
* **presets:** mark old AnimeTosho archived, drop unneeded API key on new ([#1435](https://github.com/Viren070/AIOStreams/issues/1435)) ([fdde68c](https://github.com/Viren070/AIOStreams/commit/fdde68c4264035e49fb86ee49cd9c48183e17cd0))
* **presets:** note TsukiHime's per-file audio/subtitle extraction ([#1436](https://github.com/Viren070/AIOStreams/issues/1436)) ([b17de1e](https://github.com/Viren070/AIOStreams/commit/b17de1eabd7d98e6f4a65aa01229d215081ff38f))
* **presets:** replace the fkstream and nzbhydra logos ([063a46f](https://github.com/Viren070/AIOStreams/commit/063a46f760e029f998e3793c306a9b7316b07db4)), closes [#1361](https://github.com/Viren070/AIOStreams/issues/1361)
* **remuxdb:** put the season and episode in the versions id ([bc78e36](https://github.com/Viren070/AIOStreams/commit/bc78e3657ce06684adacd71a1db34559eebba5da))
* send alang and slang lists to mpv as -append options ([fc10515](https://github.com/Viren070/AIOStreams/commit/fc10515af600dd9d667035830435bcd5d95d6823))
* **services/altmount:** send season and episode for episode requests ([#1475](https://github.com/Viren070/AIOStreams/issues/1475)) ([c27606e](https://github.com/Viren070/AIOStreams/commit/c27606efbcd0332b1e94174c0e518b8228817100)), closes [#1473](https://github.com/Viren070/AIOStreams/issues/1473)
* **ui:** base the carousel arrows on the scroll position ([6622477](https://github.com/Viren070/AIOStreams/commit/6622477c505a8c193542314feee9c9a229364eba))
* **ui:** focus a combobox's list when keys open it ([7657ecd](https://github.com/Viren070/AIOStreams/commit/7657ecd9ef754e85989dbdadaa0203dc79c95ef3))
* **ui:** ignore a loading button's presses instead of disabling it ([00032ad](https://github.com/Viren070/AIOStreams/commit/00032ad66bbfd48a36d04aae6cc40c6d3cf9e130))
* **ui:** keep a modal's overlay and content on their own layers ([ef3a7a8](https://github.com/Viren070/AIOStreams/commit/ef3a7a8b3fbb1f8349cc2dc421e4a3edd05b1193))
* **ui:** show a controlled Select's value again after a pick it didn't take ([75a651c](https://github.com/Viren070/AIOStreams/commit/75a651c8bc53f47ca0c05136e3dfb667f0160ef3))
* **ui:** size a modal's column to its box rather than its widest text ([3766493](https://github.com/Viren070/AIOStreams/commit/37664939a12d2123e9652e5ddda3457037e06128))
* **ui:** transition a tab's colours rather than all its properties ([7a0c6ec](https://github.com/Viren070/AIOStreams/commit/7a0c6ecf045afa3a6123e450b9ece6869094d071))
* **ui:** update the Radix packages ([ae82a44](https://github.com/Viren070/AIOStreams/commit/ae82a44474d62f12fcf989c1954f319a53ce86d7))
* **usenet:** check services by the hash of the NZB URL they are sent ([546b706](https://github.com/Viren070/AIOStreams/commit/546b706683d1b53afe1ba7213df798734d7a0837))
* **usenet:** hash proxied NZB URLs by the URL behind our proxy ([9ac363f](https://github.com/Viren070/AIOStreams/commit/9ac363f4ac9d7d56f3ee4017a084bff3f71c5fcc))
* **watch-state:** add the session start time to playback event ids ([ea9ddbd](https://github.com/Viren070/AIOStreams/commit/ea9ddbd2e11adaab4d0400988a6df8452a912a87))
* **watch-state:** keep the played mark under a resume point ([a4cdbc0](https://github.com/Viren070/AIOStreams/commit/a4cdbc078e38c4c200aad3f8ff8d52546e7d7b96))
* **watch-state:** move a row's sort time only on a play ([b3a2727](https://github.com/Viren070/AIOStreams/commit/b3a27278a5c8f5a749d734e2d6fed23856557150))
* **watch-state:** skip imported spellings our own rows already cover ([1ef6d01](https://github.com/Viren070/AIOStreams/commit/1ef6d0132cd2131c02c099c5c9eb5bea8208de90))
* **watch-state:** treat a favourite under any spelling as the title's ([14336d0](https://github.com/Viren070/AIOStreams/commit/14336d0488c52b1a9c564e96df9b09c17cca111f)), closes [#1429](https://github.com/Viren070/AIOStreams/issues/1429)
* **web:** bring a focused field into view when the Android app's keyboard opens ([5743cd6](https://github.com/Viren070/AIOStreams/commit/5743cd66a1cdc8df99f3534cd2b7054d897af69f))
* **web:** copy mpv's decoded frames back on TVs ([4ba4972](https://github.com/Viren070/AIOStreams/commit/4ba4972951562ff95cefa6cc951ca0da3ec9f363))
* **web:** draw the watched mark on episode images on TVs ([5a8eef9](https://github.com/Viren070/AIOStreams/commit/5a8eef96fa2bac4c0c9642f9590e3cc1cc3bdbc2)), closes [#1472](https://github.com/Viren070/AIOStreams/issues/1472)
* **web:** drop a page's focus spot only when the pointer leaves it ([3e1a5cd](https://github.com/Viren070/AIOStreams/commit/3e1a5cdbcd2aeb55afc84a7027b82dd32fe7c35c))
* **web:** drop a show's picked language from the rest of its list ([b625cd3](https://github.com/Viren070/AIOStreams/commit/b625cd3bb7db8d445a90eb86c3aad60d42f14443))
* **web:** fade each hero backdrop in as a layer over the last ([709958f](https://github.com/Viren070/AIOStreams/commit/709958fd9b665cc010b88073ea82e29964c3f60d))
* **web:** fade the backdrop's left edge in landscape ([8691143](https://github.com/Viren070/AIOStreams/commit/8691143a8e0bce6f3da84c48db1175e60f3a2285))
* **web:** fade the item page's backdrop out at its bottom edge ([e579237](https://github.com/Viren070/AIOStreams/commit/e579237e28e03e637f708a5d1f57189df1b354f4))
* **web:** fall back to the title when the hero's logo fails to load ([4c0cab5](https://github.com/Viren070/AIOStreams/commit/4c0cab5f78614accc83c51ae29c6b85af1dc65c4))
* **web:** fill the player controls' focus with an inset shadow ([78e1d27](https://github.com/Viren070/AIOStreams/commit/78e1d2771e34aea8f820b029d40fff6ff52de91f))
* **web:** fix TV focus around the rail, page starts, grids and rows ([4f0e954](https://github.com/Viren070/AIOStreams/commit/4f0e95494ebb52dc335a1db4bc3f914de487ac89))
* **web:** give focus back to what opened the version picker ([cb86a88](https://github.com/Viren070/AIOStreams/commit/cb86a88cc21d38b44de8247173ff158bfbed08ad))
* **web:** go up or down to the nearest row when nothing is in line ([197bdef](https://github.com/Viren070/AIOStreams/commit/197bdef1fb4e616bbfbcb86a053d6ea86ba35bef))
* **web:** hand a remote's Back in a list to the back action ([c5ed382](https://github.com/Viren070/AIOStreams/commit/c5ed38210acf70dc5212869ecebc352ec78698d5))
* **web:** hide the volume step on TVs ([0af0fe2](https://github.com/Viren070/AIOStreams/commit/0af0fe2639d0811af34313a2dcc7e964c45c9898))
* **web:** hold focus at a loading episode row ([1ae1483](https://github.com/Viren070/AIOStreams/commit/1ae1483e4ed6f3e298e6ba6578da4f9984d069a0)), closes [#1472](https://github.com/Viren070/AIOStreams/issues/1472)
* **web:** ignore player swipes from the top and bottom edges ([90ae6b9](https://github.com/Viren070/AIOStreams/commit/90ae6b92cdf40e271577d30b245bb02d32429295))
* **web:** jump rather than restart a smooth scroll that's still going ([7f87d72](https://github.com/Viren070/AIOStreams/commit/7f87d7238c7e18b37dd99ba04f63a83162c83168))
* **web:** keep every arrow key on a TV ([e600fdf](https://github.com/Viren070/AIOStreams/commit/e600fdf2e9be8eea9e9feab56ce2703944e79cb4))
* **web:** keep fading hero backdrops on their own layers ([f7094e6](https://github.com/Viren070/AIOStreams/commit/f7094e698c1872c3fe62218c481e73bd96a24a7c))
* **web:** keep keyed scroll steps off the page behind a dialog ([3cb138d](https://github.com/Viren070/AIOStreams/commit/3cb138d28c536d6ce7f6393322ec04ddb121ddc0))
* **web:** keep Left and Right on focus's own line ([62bb409](https://github.com/Viren070/AIOStreams/commit/62bb4092750030d505dc276908c7e07295b968aa))
* **web:** keep presses that move the desktop window from the page ([5a316fa](https://github.com/Viren070/AIOStreams/commit/5a316fa66932bad0d2f536f1a8f4bd48f673f9b2)), closes [#1476](https://github.com/Viren070/AIOStreams/issues/1476)
* **web:** keep the page still for focus in a dialog or bar ([7018937](https://github.com/Viren070/AIOStreams/commit/7018937523ac1496d56d1941774d6adea789006d))
* **web:** keep the player's controls awake while keys move in them ([c8b76b3](https://github.com/Viren070/AIOStreams/commit/c8b76b3a814926a9bf20fc22dea5d782179f0f79))
* **web:** keep the player's TV layout on TVs that report a touch pointer ([988a1b5](https://github.com/Viren070/AIOStreams/commit/988a1b5cd46421175b06a7ab629cb3c792782120))
* **web:** leave row posters room only for the caption lines shown ([1fe26e6](https://github.com/Viren070/AIOStreams/commit/1fe26e6d60051acfaced5bda8af269a7814787df))
* **web:** list ExoPlayer before mpv in the player engine setting ([d724799](https://github.com/Viren070/AIOStreams/commit/d724799f890cb5c15f9cf5e8951b36dc29a390d1))
* **web:** make the next episode card opaque and lower it while the controls hide ([e2e2069](https://github.com/Viren070/AIOStreams/commit/e2e2069689a254862c368dad5c4501fe99af3e83))
* **web:** mark a focused episode on its thumbnail in rows and its row in lists ([9a4d26c](https://github.com/Viren070/AIOStreams/commit/9a4d26cf64cb9d647382ee6c3f7d59ae848d48f0))
* **web:** measure an episode's title as its whole card for focus moves ([9a15c81](https://github.com/Viren070/AIOStreams/commit/9a15c813ff187b9cea410ce5b608d481cc33b5fe))
* **web:** measure focus moves from where scrolls under way end ([effb4c0](https://github.com/Viren070/AIOStreams/commit/effb4c0b89cfbf13e679a56f0243e5cfbaecc4c9))
* **web:** measure in-view targets on each scroll, without the glide's offset ([1e321d0](https://github.com/Viren070/AIOStreams/commit/1e321d0de0e8a8f7eb2479e308175a57256fcbb5))
* **web:** move focus sideways into the nearest bar ([fa6c2a8](https://github.com/Viren070/AIOStreams/commit/fa6c2a8a45c7942ad70f211f6efa7ed6d7f11383))
* **web:** narrow row cards to the height left under the following hero ([186d8b4](https://github.com/Viren070/AIOStreams/commit/186d8b4f721f9bdb1cf37ca2425829681de6bbc1))
* **web:** press Enter in a field on a gamepad's A ([20b9954](https://github.com/Viren070/AIOStreams/commit/20b995484a9720ee9793bf3efa395a6dba750bf7))
* **web:** retry rate-limited download version searches after Retry-After ([5995ba5](https://github.com/Viren070/AIOStreams/commit/5995ba533ea87713e398ab3437d7cb30c52b9217))
* **web:** reveal the outermost nav box and make rows nav boxes ([0831343](https://github.com/Viren070/AIOStreams/commit/083134379c2eba07ec772ed32077628fba31360d))
* **web:** rework the download rows for phones ([4178497](https://github.com/Viren070/AIOStreams/commit/4178497c98b415f72e1ca076c7c3ccf0882eb36b))
* **web:** ring a focused season poster inside its image ([650a8a4](https://github.com/Viren070/AIOStreams/commit/650a8a41fa23db4e0c07bf3840352cc01dac6b83))
* **web:** ring a focused version inside its card ([9be856a](https://github.com/Viren070/AIOStreams/commit/9be856a2962386bf432d2048545a717f42480e10))
* **web:** ring focused menu items and options inside their edges ([08f3b0b](https://github.com/Viren070/AIOStreams/commit/08f3b0b030e068ecaf8f7cef9244c4c29f89fa23))
* **web:** scroll a focused episode's whole card into view ([a3985cd](https://github.com/Viren070/AIOStreams/commit/a3985cd58d8a17d960addd4ef8147bc62ce75b92))
* **web:** scroll the player menu's list and footer together on short screens ([e391611](https://github.com/Viren070/AIOStreams/commit/e3916115030e7960bd0525feda7e4b994ccb97bc))
* **web:** set the item menu's width on phones and clamp where it opens ([65f872e](https://github.com/Viren070/AIOStreams/commit/65f872e70e0b471f6d637100a2b4211cb5304627))
* **web:** show an early end of file as a failure with a resume button ([a4a9dd7](https://github.com/Viren070/AIOStreams/commit/a4a9dd7d4b19a8e2e8aecdf85b849e6ca1c4852f))
* **web:** skip inert elements when returning focus to a page ([3b9cc3e](https://github.com/Viren070/AIOStreams/commit/3b9cc3e13561a6cb5962bb00ded07b4090ab2a41))
* **web:** skip rows scrolled out of their own scroller when moving focus ([0947dd7](https://github.com/Viren070/AIOStreams/commit/0947dd7aa0b61d188cb80083b0cf263e0582dc7a))
* **web:** stack keyed glides on layers again, easing held repeats in and out ([3bd1644](https://github.com/Viren070/AIOStreams/commit/3bd164477a3c0dafa8cbc11a5f4749a72cb2cafa))
* **web:** take a held key's quick presses as repeats ([fe5d6f7](https://github.com/Viren070/AIOStreams/commit/fe5d6f792f8dbbadc3317f083ac9c2e6549fb46b))
* **web:** treat sticky bars like fixed ones in arrow navigation ([bdedc94](https://github.com/Viren070/AIOStreams/commit/bdedc9483f1c15ec71f7de70f63d15c93fd592ae))


### Performance Improvements

* **jellyfin-web:** mount only the hero backdrops in use ([0b22949](https://github.com/Viren070/AIOStreams/commit/0b2294914b26f2e41d5eb6e4f74ebe50736dd4b4))
* **jellyfin-web:** send an image Accept header with artwork fetches ([8c55a18](https://github.com/Viren070/AIOStreams/commit/8c55a1876ef97755a9c3ec7a26669aaae14aa5f1))
* **jellyfin:** keep an ended show's episode list for a week ([2b75194](https://github.com/Viren070/AIOStreams/commit/2b7519448acf12f04dca819141b6050ae7d22a2c))
* **jellyfin:** send Access-Control-Max-Age with preflight answers ([1499906](https://github.com/Viren070/AIOStreams/commit/1499906419bc528a831b16e240cb75a5e1a649a4))
* **jellyfin:** size the image inside AIOMetadata poster cache addresses ([b867f63](https://github.com/Viren070/AIOStreams/commit/b867f63e34a1703456088023e7a2e2f9248b2b49))
* **jellyfin:** start Next Up's next show check as each one ends ([db76294](https://github.com/Viren070/AIOStreams/commit/db762948a3123e847449b956d66198d1e039ca51))
* **media-info:** send stored records packed from the lookup API ([d9b6399](https://github.com/Viren070/AIOStreams/commit/d9b639908c6934eec105884fd7873c619f4800a8))
* **remuxdb:** start the lookup alongside the addon fetch and time out after 2 s ([99b6dc3](https://github.com/Viren070/AIOStreams/commit/99b6dc3f907490ffa9e24eeb6c1f008609f1867c))
* **ui:** glide a carousel to focus with a CSS transition ([405bdfb](https://github.com/Viren070/AIOStreams/commit/405bdfbfbdb0c2302537c3e8ec65319eae8218aa))
* **watch-state:** fetch each page of recent shows in one joined query ([c50ded1](https://github.com/Viren070/AIOStreams/commit/c50ded11d198385999e89baeeab63ad335d44292))
* **watch-state:** look up spellings through both indexes ([64f62ed](https://github.com/Viren070/AIOStreams/commit/64f62ed99ca19f93c6565fe413b1e50cde251cd2))
* **web:** ask for a show's next episode, seasons and opening episodes as its page starts to draw ([f649549](https://github.com/Viren070/AIOStreams/commit/f649549289850315625eeeb9cae1dee1fdccaffb))
* **web:** ask for a title before reading its saved copy ([c8932ff](https://github.com/Viren070/AIOStreams/commit/c8932ffcb0763c4a0113cf142919af5cc5e5db90))
* **web:** ask for the show's poster for a season that carries it ([a71ed35](https://github.com/Viren070/AIOStreams/commit/a71ed35c94bb128022e431eac6386404916f4b66))
* **web:** ask the Android app's mpv for direct MediaCodec decoding ([2173c62](https://github.com/Viren070/AIOStreams/commit/2173c6232fc6f35c8483a81ea3976cdd119c63f8))
* **web:** chase keyed jumps on one layer at an even speed ([ce4fa87](https://github.com/Viren070/AIOStreams/commit/ce4fa87530583be1b90c4adbcb191b63b54ea076))
* **web:** check a row's end in a frame rather than in its effect ([db4fa6f](https://github.com/Viren070/AIOStreams/commit/db4fa6fd3aaa0e7ec6037002a7a40f7103eb5343))
* **web:** count saved bytes so a prune reads every entry only near the limit ([9188cda](https://github.com/Viren070/AIOStreams/commit/9188cdaf7218cef3256899fb2fd2fdd439d44180))
* **web:** draw a home library row's cards only once it nears the screen ([c32c777](https://github.com/Viren070/AIOStreams/commit/c32c777201e9fcafca8fb72838ae3b8ac69f76e1))
* **web:** draw a title's page from a loaded list's copy of it while it loads ([2031f62](https://github.com/Viren070/AIOStreams/commit/2031f62b76ab3200860018a1559aee40c63080c8))
* **web:** draw only the cards near a long row's view ([93e4c55](https://github.com/Viren070/AIOStreams/commit/93e4c556702b366287b71ae4470248fe2775e775))
* **web:** ease keyed page and hero row scrolls on the compositor on TVs ([c6cc502](https://github.com/Viren070/AIOStreams/commit/c6cc502c239bf170e7f7bdbd8d2594f5e5bc9e93))
* **web:** fade card overlays rather than colouring them in ([7cdf21d](https://github.com/Viren070/AIOStreams/commit/7cdf21d0ac0afc145bc74947aa5dbca26d563cb8))
* **web:** fade cards in with the Web Animations API ([d82987b](https://github.com/Viren070/AIOStreams/commit/d82987b6d76e56e55c3ed1e3c59328deb8f780a6))
* **web:** give focus transitions on cards the keyed glide's duration ([52d0693](https://github.com/Viren070/AIOStreams/commit/52d069362ef48e5e5f849f4f7b9e92f07008ace8))
* **web:** give the apps' build an empty page icon ([6928b24](https://github.com/Viren070/AIOStreams/commit/6928b24fa28b331d7b1c3a5573a848b6acf70efe))
* **web:** hold an unfetched row's place with one placeholder ([3993676](https://github.com/Viren070/AIOStreams/commit/399367626c0c1887e813a0e69b5c43801c4ef21d))
* **web:** hold placeholders still in rows not loading yet ([9a5fd19](https://github.com/Viren070/AIOStreams/commit/9a5fd19a9b2a843feb5a8ac55777c97c25eee506))
* **web:** keep React from listening for transition and animation events ([6ca93a8](https://github.com/Viren070/AIOStreams/commit/6ca93a8fdbce95b0e8e861499d8d607577167b15))
* **web:** keep saved artwork as Blobs ([cebb61f](https://github.com/Viren070/AIOStreams/commit/cebb61fa9d6db850af1ea0f09e433296c353a953))
* **web:** keep the home page while others are open ([90f2def](https://github.com/Viren070/AIOStreams/commit/90f2defc44daac60dd98f21c81d9b158ba22961a))
* **web:** keep the layout and Home mounted under the player ([acb9b68](https://github.com/Viren070/AIOStreams/commit/acb9b68138508f77bf424721a64b10150b4a8df9))
* **web:** keep the playhead out of the player's React state ([880cc8e](https://github.com/Viren070/AIOStreams/commit/880cc8ef6fd7c214c795b05d9419769959795ad3))
* **web:** leave the touch navigation bar out on TVs ([233ec48](https://github.com/Viren070/AIOStreams/commit/233ec48d1d05a2c85fbe4beec0e71faf410d30a6))
* **web:** make form-less buttons submit buttons on Android ([1307291](https://github.com/Viren070/AIOStreams/commit/13072919d60b3d39c57da4ff0375fb11d2823bfe))
* **web:** measure in-view targets once a scroll settles ([b878fb9](https://github.com/Viren070/AIOStreams/commit/b878fb97934574ce2af2943c0edfe38420c6714a))
* **web:** measure in-view targets once after a navigation ([cc4a951](https://github.com/Viren070/AIOStreams/commit/cc4a95120a34e6f543670686fe181426d31798c3))
* **web:** measure nearness by hand and keep link addresses in data-href on TVs ([a192627](https://github.com/Viren070/AIOStreams/commit/a19262703f0aa4e5e1464cfa02de0dc165af1936))
* **web:** measure only cards near the screen when moving focus ([f47e21a](https://github.com/Viren070/AIOStreams/commit/f47e21a83b8ce07dc359d31bbdf70c7f4719ba16))
* **web:** memoise the Home page kept under other pages ([c120f88](https://github.com/Viren070/AIOStreams/commit/c120f8865c96bf84a7f29d5ab995ee80ab3f5150))
* **web:** memoise the item header's toggles, overview, rating and links ([9729fdb](https://github.com/Viren070/AIOStreams/commit/9729fdbc81e73167cbf9d772c380d873e94e40ac))
* **web:** memoise the season posters row ([f7999c8](https://github.com/Viren070/AIOStreams/commit/f7999c835a4d2590a0cd34cf9c726fb1acfc8de6))
* **web:** open a settings tab once focus rests on it ([7ab9bf1](https://github.com/Viren070/AIOStreams/commit/7ab9bf13a2118c7e2ea277332870bbce81b8060f))
* **web:** open item menus without blocking the page ([c88ff6d](https://github.com/Viren070/AIOStreams/commit/c88ff6d1b857fbf88c63e5fea9090c43720447af))
* **web:** open the docked TV rail with a fade rather than a widening ([1ee7d6f](https://github.com/Viren070/AIOStreams/commit/1ee7d6f93b1afdbf20ae871a9cf4c7a51a3eed92))
* **web:** pace a held key's repeats to the screen ([854db60](https://github.com/Viren070/AIOStreams/commit/854db6025660759db7807bc230c919f14e6ed7f0))
* **web:** pause the rotating hero while it is out of sight ([12d13ef](https://github.com/Viren070/AIOStreams/commit/12d13ef23092896012d462bdd0c2c1d948cc9fdf))
* **web:** put a submit button before the page's first control on Android ([30e01bd](https://github.com/Viren070/AIOStreams/commit/30e01bd3a0fdbb96816641670f16b06b7853f132))
* **web:** read fewer layouts when moving focus ([558f416](https://github.com/Viren070/AIOStreams/commit/558f41619d987c45969b97d77fea727631fbfb29))
* **web:** save the small copies of shrunk artwork ([f6c0ab3](https://github.com/Viren070/AIOStreams/commit/f6c0ab3a53145a3592718da00643ec59649fc9c4))
* **web:** scale artwork at rest and look for open dialogs only in portals ([b95f252](https://github.com/Viren070/AIOStreams/commit/b95f252d07a6ae866b13c645e537fe4dc85333f6))
* **web:** scale focused artwork in 200 ms ([b87ec97](https://github.com/Viren070/AIOStreams/commit/b87ec9785aea81b475e375ec717e3619c28218d2))
* **web:** scroll rows natively on touch screens ([a0c6e01](https://github.com/Viren070/AIOStreams/commit/a0c6e01aff3c7aa9dc445a582e72e12ebdcbff57))
* **web:** scroll TV rows natively with a compositor glide ([3595f05](https://github.com/Viren070/AIOStreams/commit/3595f05e1a58bf06af607941a6597656c5e8d246))
* **web:** share intersection observers between elements ([5f1c8dc](https://github.com/Viren070/AIOStreams/commit/5f1c8dce35a935e119d363642f7f8832b0ebbe34))
* **web:** share one item menu between all cards ([e1605a7](https://github.com/Viren070/AIOStreams/commit/e1605a77e3b7775f8fc3f9d2c88e3d07eca13af1))
* **web:** show artwork as images kept in memory ([b93abea](https://github.com/Viren070/AIOStreams/commit/b93abea6824fd944ad2fcb7b6226298cf5c971e4))
* **web:** shrink artwork in a pool of workers ([d6e8542](https://github.com/Viren070/AIOStreams/commit/d6e8542b9298e4968df41bb2b8b433e203e84010))
* **web:** start gamepad support in the Android app only with a controller attached ([4930925](https://github.com/Viren070/AIOStreams/commit/493092548715836381c92840873667569c7c62e0))
* **web:** start the artwork workers with the page and make blob addresses in them ([2a32ba9](https://github.com/Viren070/AIOStreams/commit/2a32ba978747a1517f86a2e31014db0afe3eaa2d))
* **web:** step along a row's cards without measuring the others ([783cb1a](https://github.com/Viren070/AIOStreams/commit/783cb1aa8f44081a7bdd29b4d59de975548497b0))

## [2.35.9](https://github.com/Viren070/AIOStreams/compare/v2.35.8...v2.35.9) (2026-10-03)


### Features

* **jellyfin:** add watchlisted shows and films to Upcoming ([7814d09](https://github.com/Viren070/AIOStreams/commit/7814d091bffccdf9230967d4074d114428f51f36))
* **jellyfin:** raise the max versions default to 25 ([9f8ed87](https://github.com/Viren070/AIOStreams/commit/9f8ed87f92548a9516f1d4f60cc372088337fb53))
* **watch-state:** read a kind on pulled watchlist and rating entries ([95c77e5](https://github.com/Viren070/AIOStreams/commit/95c77e52d90d71f6c6005b5245c0fde84aefe7a5))
* **watch-state:** read airsAt on pulled next episodes ([9aee883](https://github.com/Viren070/AIOStreams/commit/9aee8832accce0cd26576b5cccf3736e8dfb06d4))


### Bug Fixes

* **desktop:** load a bundled vulkan-1.dll when Windows has none ([30ddeb0](https://github.com/Viren070/AIOStreams/commit/30ddeb0d8506179319bda82486ad8c2f9a672de9))
* **jellyfin-web:** avoid GamepadList array methods and AbortSignal.timeout ([76ca250](https://github.com/Viren070/AIOStreams/commit/76ca25076df04330f7a2974a4dc0559f5cd94df6))
* **jellyfin-web:** keep the artwork crop inside the image ([f8fae6c](https://github.com/Viren070/AIOStreams/commit/f8fae6ca9494622549a04643f33c493572c2a397))
* **jellyfin:** decode HTML entities in overviews ([9902895](https://github.com/Viren070/AIOStreams/commit/99028950d9a9b9dbad4c9c04d4def8369fae1ef4))
* **jellyfin:** page Next Up through up to 200 recent shows ([4f51dc1](https://github.com/Viren070/AIOStreams/commit/4f51dc11b085fa096fd8c962fe2be587e91b2fed))
* **jellyfin:** size the pointer cache by max versions ([c086df8](https://github.com/Viren070/AIOStreams/commit/c086df84b56e6c111936c8e7bdbc0b3d8c96b6f3))
* **watch-state:** fold an item's spellings in the history list and counts ([4f82379](https://github.com/Viren070/AIOStreams/commit/4f823797deb3f490482e551d793029567a272071))

## [2.35.8](https://github.com/Viren070/AIOStreams/compare/v2.35.7...v2.35.8) (2026-10-02)


### Features

* **cache:** add stale-while-revalidate reads and use them for manifests ([416fcce](https://github.com/Viren070/AIOStreams/commit/416fcce2ec5d20edf379c4e993163932ac30ee15))
* **dashboard:** add a version card to the overview ([a16a2f1](https://github.com/Viren070/AIOStreams/commit/a16a2f1c8980f82ad7d0987d2ce777e69211f5d1))
* **jellyfin-web:** change subtitle size and height from the player ([ffdc0d3](https://github.com/Viren070/AIOStreams/commit/ffdc0d39c990af1bf5402d4a6f3fc70f72158c81))
* **jellyfin-web:** drop hold to play from rows ([d800040](https://github.com/Viren070/AIOStreams/commit/d800040a45bef85ba00ac955c9c325576bb2a6f5))
* **jellyfin-web:** guess intro and credits segments from chapter lengths ([1580465](https://github.com/Viren070/AIOStreams/commit/158046534d2c66712f97a6bbca608407c4b6ac3f))
* **jellyfin-web:** play next up and resume items from their page ([72f8032](https://github.com/Viren070/AIOStreams/commit/72f8032e52f63a8a27614e9501ca21125ade5570))
* **jellyfin-web:** pulse the episode a page opened on instead of ringing it ([b4fbd7c](https://github.com/Viren070/AIOStreams/commit/b4fbd7cbc69b930f8999e2f2ac7ecca99bed35c8))
* **jellyfin-web:** request images at their drawn width times the pixel ratio ([7f3d396](https://github.com/Viren070/AIOStreams/commit/7f3d396d5e7308399770ee0714caf41cf414ea90))
* **jellyfin-web:** resize card artwork to its device size in a worker ([2b49efe](https://github.com/Viren070/AIOStreams/commit/2b49efee7685ee99191853245b72cc156a38e7c1))
* **jellyfin-web:** restore keyboard focus on pages returned to ([3ce4dee](https://github.com/Viren070/AIOStreams/commit/3ce4dee78ac0cc9b081d03e90d3f822d33f29918))
* **jellyfin-web:** rewrite shortcuts as remappable actions and add spatial navigation ([ff0dd1a](https://github.com/Viren070/AIOStreams/commit/ff0dd1a11e2111d998226946d72a39f0a777c11d))
* **jellyfin:** redirect artwork to the smallest rendition covering the requested width ([a0d2f9d](https://github.com/Viren070/AIOStreams/commit/a0d2f9d067203aba06adb53a5e57d295336bcc42))


### Bug Fixes

* **formatter:** stop cached templates keeping their formatter alive ([360deb8](https://github.com/Viren070/AIOStreams/commit/360deb8a4c9625ed2a772587a64fb518cede65dd))
* **jellyfin-web:** leave genre-required libraries off home ([0ac4310](https://github.com/Viren070/AIOStreams/commit/0ac4310c3e3bf015bd0d92532e9dc6a932f3be25))
* **jellyfin-web:** show one continue watching card per show ([09b1676](https://github.com/Viren070/AIOStreams/commit/09b1676a7d7003cda4066a0264dc3640a07d5109))
* **jellyfin:** attach user data to series built from watch rows ([dd9a87c](https://github.com/Viren070/AIOStreams/commit/dd9a87c162a210f450ba2d874b7831b4caeae1dd)), closes [#1419](https://github.com/Viren070/AIOStreams/issues/1419)
* **jellyfin:** look up episodes by video id across every season first ([aa64fb4](https://github.com/Viren070/AIOStreams/commit/aa64fb4179c7b85ebfb4892914f5a25eba9d847e))
* **jellyfin:** reload cached configs once their TTL has passed ([82f0bd3](https://github.com/Viren070/AIOStreams/commit/82f0bd36780522953dd2d1c86a7249a1344f0ffd))
* **watch-state:** place anime episodes by TVDB when their IMDb hints name another show ([f815290](https://github.com/Viren070/AIOStreams/commit/f815290e8775981cbdde22e0fff7fc1d5d8657cb))
* **wrapper:** bound foreground manifest fetches by the manifest timeout ([f82773b](https://github.com/Viren070/AIOStreams/commit/f82773bb7f39dcbfcf4e2330c28aebdf2d965e3f))


### Performance Improvements

* **anime-database:** log only candidate rids in the selector ([8f7fd8a](https://github.com/Viren070/AIOStreams/commit/8f7fd8a803c0c6e21cd3834b50ba28f193b0e80c))
* **api:** stop counting users on every health and status check ([54ce0ca](https://github.com/Viren070/AIOStreams/commit/54ce0cac441f58d4fcb47ca8cb9233c97702a0d1))
* **cache:** estimate the SQL cache size between counts ([e98bbe3](https://github.com/Viren070/AIOStreams/commit/e98bbe34a423246d68b3a435240521e51916b774))
* **db:** drop unused indexes and narrow the import sweep index ([61d73a8](https://github.com/Viren070/AIOStreams/commit/61d73a83cf7a4416de5a99522503e940e95a1ce6))
* **db:** stamp users.accessed_at at most once an hour ([89beb47](https://github.com/Viren070/AIOStreams/commit/89beb47700588621d8d67171b7600779311c35bc))
* **debrid:** skip torrents and NZBs with more than 10,000 selectable files ([ec99d30](https://github.com/Viren070/AIOStreams/commit/ec99d30930216c841ca6d57b65d704d32fd77985))
* **debrid:** treat audio files as non-video and look extensions up in a set ([e27061d](https://github.com/Viren070/AIOStreams/commit/e27061ddb4bfb224bb0ba82fac7520d9b8fb108c))
* **debrid:** treat ebook and comic files as non-video ([6547f3e](https://github.com/Viren070/AIOStreams/commit/6547f3ee7eb135bfdf224717a3367ab4f5c06667))
* **jellyfin:** build only the episodes Next Up picks ([62b5670](https://github.com/Viren070/AIOStreams/commit/62b5670e4c16333e06f396b01ee2823dcfa0edd5))
* **jellyfin:** memoise image tags by URL ([24b395a](https://github.com/Viren070/AIOStreams/commit/24b395acf393557fcae38dca291ecdbecbab35e4))
* **jellyfin:** read Upcoming and calendar shows through a pool ([ae8b370](https://github.com/Viren070/AIOStreams/commit/ae8b370cad832cdf7f4316ba079dece8716d9c36))
* **jellyfin:** refresh id map seen_at at most once a day ([52d43ec](https://github.com/Viren070/AIOStreams/commit/52d43ec58a14a05ce91ed13e090620e9142627af))
* **jellyfin:** share the cached config instead of cloning it ([6a1140f](https://github.com/Viren070/AIOStreams/commit/6a1140fb3ec2955f7693726f903f09514b17b8ac))
* **sel:** extract expression names once per item when matching overrides ([25f2fc0](https://github.com/Viren070/AIOStreams/commit/25f2fc033f5f7b42d109aeed64610bee7c5ad217))
* **watch-state:** cache match keys for batch lookups ([87b4847](https://github.com/Viren070/AIOStreams/commit/87b48474d390c9c56ea57693d6753cd5fdf2462d))
* **watch-state:** return the upserted row instead of reading it back ([6db546d](https://github.com/Viren070/AIOStreams/commit/6db546dfc891948b0a312e2708df4d9918339391))
* **watch-state:** sweep stale imports by listed keys instead of re-stamping them ([4e1cbbf](https://github.com/Viren070/AIOStreams/commit/4e1cbbf8ddc9a11657a4fce56046d606aa9b2bc5))



## [2.35.7](https://github.com/Viren070/AIOStreams/compare/v2.35.6...v2.35.7) (2026-10-01)


### Features

* **jellyfin-web:** add an Android app settings tab that opens the app's settings ([9508271](https://github.com/Viren070/AIOStreams/commit/95082715f10bb5f94bcdaada5b366e1ceaa23279))
* **jellyfin-web:** move app bridges behind one host interface ([9102d6e](https://github.com/Viren070/AIOStreams/commit/9102d6efb20190300a13217799cb1548d9123054))
* **jellyfin-web:** use more of the Android app's bridge ([2a75f88](https://github.com/Viren070/AIOStreams/commit/2a75f88aefeb69185c34100ccdc58d0bc7b284a0))
* **jellyfin:** list the next episode of caught-up shows in Upcoming ([0840b88](https://github.com/Viren070/AIOStreams/commit/0840b8839ba57362f925829e1a8dbb3a2d7123c6))


### Bug Fixes

* **jellyfin:** drop the anime/series fallback on meta requests ([2a7569b](https://github.com/Viren070/AIOStreams/commit/2a7569bd4fbea3fca613fcaee0b1f95431d8dc1a))
* **jellyfin:** go on from the furthest watched episode in Next Up ([c77e031](https://github.com/Viren070/AIOStreams/commit/c77e031405efe58bad4c6809de8310866a7ed8f9))
* **watch-state:** return one recent series row per show across its ids ([5389d49](https://github.com/Viren070/AIOStreams/commit/5389d49d8e1ffe128326cc3ef1918b00581eaf88))

## [2.35.4](https://github.com/Viren070/AIOStreams/compare/v2.35.3...v2.35.4) (2026-09-28)


### Features

* adjust jellyfin wording/install options, update docs, readme ([d461cd7](https://github.com/Viren070/AIOStreams/commit/d461cd76ef43c34f270d8a93a6f721f42071b528))
* **builtins/nab:** warn on missing infohash, fix hash-fallback bug ([#1261](https://github.com/Viren070/AIOStreams/issues/1261)) ([8b5aa22](https://github.com/Viren070/AIOStreams/commit/8b5aa22e397d9378216ecc1e0ccfd353fcd88e9e))
* **desktop:** add Discord events for browsing and a connection status ([eb193b4](https://github.com/Viren070/AIOStreams/commit/eb193b47ff45fe30604c3ed66b0829509ccc7cf5))


## [2.35.2](https://github.com/Viren070/AIOStreams/compare/v2.35.1...v2.35.2) (2026-09-27)


### Features

* **jellyfin-web:** add hooks for custom CSS and an apply step ([6a66b23](https://github.com/Viren070/AIOStreams/commit/6a66b234cfb9008968fe50cc2dabdbbb582a23c5))


### Bug Fixes

* **dashboard:** load settings saved on other instances ([b99ef06](https://github.com/Viren070/AIOStreams/commit/b99ef060e954c0b2168c8b7b56ce71adbaa02b4b))
* **jellyfin-web:** brighten the calendar's episode art ([46a092c](https://github.com/Viren070/AIOStreams/commit/46a092c692d0544e005d5c6ede353d3c8985c57d))
* **ui:** keep a modal open when a press closes a dialog above it ([c0c745b](https://github.com/Viren070/AIOStreams/commit/c0c745b78d3077bf5df36f6b1bc3a0f59ed349a5))


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


## [2.33.2](https://github.com/Viren070/AIOStreams/compare/v2.33.1...v2.33.2) (2026-08-10)


### Bug Fixes

* **usenet:** type archive inner files by magic bytes ([9a1b6d7](https://github.com/Viren070/AIOStreams/commit/9a1b6d7f4954dc38113153893c070580ecd1faef))
* **variants:** support path param based selector and make default ([9778afc](https://github.com/Viren070/AIOStreams/commit/9778afcf07f2b994b226d69031caa454d5127aec))


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


