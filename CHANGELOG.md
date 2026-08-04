# Changelog

## 0.11.0 (2026-08-04)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/limrun-inc/python-sdk/compare/v0.10.0...v0.11.0)

### Features

* **api:** add analytics api ([f53ecaa](https://github.com/limrun-inc/python-sdk/commit/f53ecaa0a628640dc520bf392aca70597e7a20c1))
* **api:** add gradle to stainless config as well ([335e975](https://github.com/limrun-inc/python-sdk/commit/335e975b1564432c709f7cf55760dbe05382d61f))
* **api:** add jurisdiction ([6921be5](https://github.com/limrun-inc/python-sdk/commit/6921be5995d0db5864b53000960c24602b1b23ab))
* **api:** add scoped tokens to stainless config ([d399044](https://github.com/limrun-inc/python-sdk/commit/d3990440a1badd3c9c826ea83313bd33acf25b44))
* **api:** add version to android playwright ([c01f3dc](https://github.com/limrun-inc/python-sdk/commit/c01f3dcc11a3e1b64e4007c0ae2562ba545b74bc))
* **api:** add xcode build logs and signedStreamUrl ([47e6ac4](https://github.com/limrun-inc/python-sdk/commit/47e6ac44f3d48bb15a995f17d3e586b823c5547a))
* **api:** analytics api, make platform enum ([6c679fb](https://github.com/limrun-inc/python-sdk/commit/6c679fb381e1db207b8831f8cea2f290e0c01394))
* **api:** fix indentation ([0be86f5](https://github.com/limrun-inc/python-sdk/commit/0be86f5ba050b8fa1f23b778eb81226248e799e4))
* **api:** fix stainless models for scoped tokens ([248a9d4](https://github.com/limrun-inc/python-sdk/commit/248a9d475d7b56aadac3fda9f0ff6a79bbfeddf6))
* **api:** ios add forceBundleId ([d37a940](https://github.com/limrun-inc/python-sdk/commit/d37a940752faf9b8386d686e486c6ec5f529d512))
* **api:** manual updates ([5cf9a85](https://github.com/limrun-inc/python-sdk/commit/5cf9a857267b343d0a9bb2e5a1673809ee319a6b))
* **api:** manual updates ([ae30f4d](https://github.com/limrun-inc/python-sdk/commit/ae30f4df8b4a19ef4643afd49cfcd2ae1adcd643))
* **api:** manual updates ([80939c4](https://github.com/limrun-inc/python-sdk/commit/80939c44898768cea4fe25806cf0a5d86cd9b3a0))
* **api:** scoped tokens desc fix ([4dcb31a](https://github.com/limrun-inc/python-sdk/commit/4dcb31a1e020e20810483236deee43f87ffa94d6))
* **api:** simplify the models for analytics endpoint ([656c11c](https://github.com/limrun-inc/python-sdk/commit/656c11cb7c9f5e3bdeddc43d53489d9e267bcea7))
* **api:** update to latest main ([a536ff1](https://github.com/limrun-inc/python-sdk/commit/a536ff10b358b05429c836cf5babed59286d3c9b))
* **internal/types:** support eagerly validating pydantic iterators ([d787141](https://github.com/limrun-inc/python-sdk/commit/d787141ec4d087f8f473dfe41d86f0c8c82672e5))
* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([cd09a15](https://github.com/limrun-inc/python-sdk/commit/cd09a15656fbc5edf53745564128092099e4346d))
* support setting headers via env ([601135d](https://github.com/limrun-inc/python-sdk/commit/601135db9f4eb15ee575e63b50d737e3c93d1625))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([3d63f72](https://github.com/limrun-inc/python-sdk/commit/3d63f72d80c3aa8455a0c58ca8d9aeebbf0bc307))
* use correct field name format for multipart file arrays ([c46f7f3](https://github.com/limrun-inc/python-sdk/commit/c46f7f392bf1a617a5fa372096a276ddf299f457))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([0229b73](https://github.com/limrun-inc/python-sdk/commit/0229b737adc72f602a1525f2687c89ab776e7eaf))


### Chores

* **internal:** more robust bootstrap script ([12a1534](https://github.com/limrun-inc/python-sdk/commit/12a1534ba8cadb440b4430aab9223ebfc0de806d))
* **internal:** reformat pyproject.toml ([8b67d80](https://github.com/limrun-inc/python-sdk/commit/8b67d807da768fa5292b61286da1e36d2a071046))

## 0.10.0 (2026-04-11)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/limrun-inc/python-sdk/compare/v0.9.0...v0.10.0)

### Features

* **api:** add apiUrl to android ([f4b20d1](https://github.com/limrun-inc/python-sdk/commit/f4b20d10ff3146a7f69fba5592c4e6a2a99b8686))
* **api:** add displayName to asset ([d4fe4c1](https://github.com/limrun-inc/python-sdk/commit/d4fe4c16bf47c880f3a36772df6b51fa202dfc22))
* **api:** add ios sandbox properties and app store for assets ([79b878d](https://github.com/limrun-inc/python-sdk/commit/79b878dd9ce6a49a811bdef875da931c97ae0f35))
* **api:** add optional os field to assets ([95d3948](https://github.com/limrun-inc/python-sdk/commit/95d39487044edc9f135b7b0f74afcf30e09b7d96))
* **api:** add spec.model to ios creation api ([b7e6770](https://github.com/limrun-inc/python-sdk/commit/b7e67702e48bab7c14314b907016e2d65b2d5815))
* **api:** add status.mcpUrl for ios ([b6b64d3](https://github.com/limrun-inc/python-sdk/commit/b6b64d310d619e86e24f3ba0acf4596d788d36ad))
* **api:** add status.mcpUrl to android ([b837288](https://github.com/limrun-inc/python-sdk/commit/b837288b3b60d618463c9481cf896d8fc627b0f1))
* **api:** add xcode instances endpoints ([5041989](https://github.com/limrun-inc/python-sdk/commit/50419899965c9346919a1cc3e6cccc39b81d291a))
* **api:** fix model name for xcode_instance in stainless config ([6524d3f](https://github.com/limrun-inc/python-sdk/commit/6524d3ff19c19675ad87b2e72fda31a30ca04c1a))
* **api:** increase timeout to 5 minutes since big app installations may take longer than a minute ([0d9a065](https://github.com/limrun-inc/python-sdk/commit/0d9a0656b4de373bc2feedfedeb177fc8ecec502))
* **api:** update stainless config for xcode_instances resource ([40668f3](https://github.com/limrun-inc/python-sdk/commit/40668f35e880c6beb2b319ae85c95a5eedb16545))
* **client:** add custom JSON encoder for extended type support ([0403818](https://github.com/limrun-inc/python-sdk/commit/0403818157b7f32718d50f421a7038941c92ac38))
* **client:** add support for binary request streaming ([8918b83](https://github.com/limrun-inc/python-sdk/commit/8918b8372a5c18a2163972fd798e0810ce2ed686))


### Bug Fixes

* **client:** loosen auth header validation ([3c8c6e2](https://github.com/limrun-inc/python-sdk/commit/3c8c6e2a2e452b742ba890e0b3fb6d6d76434783))
* use async_to_httpx_files in patch method ([8207c94](https://github.com/limrun-inc/python-sdk/commit/8207c946cc0cb3d9b5a97a60331aae610b304ece))


### Chores

* **ci:** upgrade `actions/github-script` ([ce1aac8](https://github.com/limrun-inc/python-sdk/commit/ce1aac814b24e47c04f837946eb77ae716727586))
* format all `api.md` files ([9be9c3f](https://github.com/limrun-inc/python-sdk/commit/9be9c3f027208e348d11e4148814871ea5f53cfa))
* **internal:** add `--fix` argument to lint script ([c6513ca](https://github.com/limrun-inc/python-sdk/commit/c6513cac50526f80bd8100a0b22541918dc0d07f))
* **internal:** add missing files argument to base client ([3b4eb61](https://github.com/limrun-inc/python-sdk/commit/3b4eb61934e77432e15228e080adf5ea57010419))
* **internal:** bump dependencies ([51e3172](https://github.com/limrun-inc/python-sdk/commit/51e317263c35e3145d826f5be4b5060000cd2f9c))
* **internal:** codegen related update ([b3e791f](https://github.com/limrun-inc/python-sdk/commit/b3e791f51bb2213fb10123d2dc57611380c37958))
* **internal:** codegen related update ([c627787](https://github.com/limrun-inc/python-sdk/commit/c627787552abc38f5a4035ddbfac925b07457416))
* **internal:** codegen related update ([502959d](https://github.com/limrun-inc/python-sdk/commit/502959de7c4daa021b8d842d2aa16f85640d4096))
* **internal:** codegen related update ([e2a0ba3](https://github.com/limrun-inc/python-sdk/commit/e2a0ba32faa10f7795a236c66cf0f131026e45d5))
* **internal:** codegen related update ([cf97aec](https://github.com/limrun-inc/python-sdk/commit/cf97aec9039fd06bbc1f6dcc088247de592e17a4))
* **internal:** codegen related update ([adb7df2](https://github.com/limrun-inc/python-sdk/commit/adb7df2b6635dc5b7517b68900880bb66f342364))
* **internal:** codegen related update ([d6320fe](https://github.com/limrun-inc/python-sdk/commit/d6320fece3c04ca4974719cb8a44ceb08e8ef4b3))
* **internal:** codegen related update ([7f99be1](https://github.com/limrun-inc/python-sdk/commit/7f99be1af61e1fe2579ffe978d3e4950975dabb5))
* **internal:** codegen related update ([ac36b22](https://github.com/limrun-inc/python-sdk/commit/ac36b229930b1f2b0745d8c914749e21df5d403f))
* **internal:** codegen related update ([93c6957](https://github.com/limrun-inc/python-sdk/commit/93c695795df12fdbc3f101b462508bf180a0000f))
* **internal:** fix lint error on Python 3.14 ([d11f360](https://github.com/limrun-inc/python-sdk/commit/d11f36003e8e13287d2acfb228dd47357358761a))
* **internal:** remove mock server code ([6bc0de4](https://github.com/limrun-inc/python-sdk/commit/6bc0de40a2048d0a6162aa7a3eb2e3cf7d5ca2ef))
* **internal:** update `actions/checkout` version ([b6db8d6](https://github.com/limrun-inc/python-sdk/commit/b6db8d64544d9da9d3e1948f73272f5a1018756f))
* speedup initial import ([7cafc23](https://github.com/limrun-inc/python-sdk/commit/7cafc23a5d774732001b90025cc1ba62ead284a6))
* update mock server docs ([5ebe065](https://github.com/limrun-inc/python-sdk/commit/5ebe0654d5a13a65158418acefb9dd48903636f8))


### Documentation

* add more examples ([5ec7ea7](https://github.com/limrun-inc/python-sdk/commit/5ec7ea7fd56fc35e7d9a06201615c04d96d4d926))

## 0.9.0 (2025-12-14)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/limrun-inc/python-sdk/compare/v0.8.0...v0.9.0)

### Features

* **api:** add android sandbox api ([b1ec65b](https://github.com/limrun-inc/python-sdk/commit/b1ec65b1d7e36768d2bf3c8627242cc889f143ec))
* **api:** add asset type configuration with chrome flag ([0900df2](https://github.com/limrun-inc/python-sdk/commit/0900df2b560b981493c0c1572b5dcca043b7524a))
* **api:** add the optional errorMessage field in status ([6d26c2b](https://github.com/limrun-inc/python-sdk/commit/6d26c2bdedd6f9e576fd9419022d150dbdb3194f))
* **api:** make chromeFlag enum with supported value ([a937aac](https://github.com/limrun-inc/python-sdk/commit/a937aac4d9c69a21886f5c477e989edbbbaf9732))
* **api:** manual updates ([57c22b4](https://github.com/limrun-inc/python-sdk/commit/57c22b43395e906b6a2a869e7355fe1938770796))
* **api:** manual updates ([f88a368](https://github.com/limrun-inc/python-sdk/commit/f88a36818071f20c4a4b06df26a25ee6e0ab0b9d))


### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([bd4bed9](https://github.com/limrun-inc/python-sdk/commit/bd4bed99a71cc69b225adc7c8bd0439a288e0b34))
* ensure streams are always closed ([63f1ee4](https://github.com/limrun-inc/python-sdk/commit/63f1ee4d81c796f3d0aa061726b8a542b6862a0c))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([08396f0](https://github.com/limrun-inc/python-sdk/commit/08396f04ff54737c4d9f9b7da4c37aa1f8620537))


### Chores

* add Python 3.14 classifier and testing ([e635bb6](https://github.com/limrun-inc/python-sdk/commit/e635bb6f3c9930eb22551f692062bd9e45837c36))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([5469100](https://github.com/limrun-inc/python-sdk/commit/54691000d4ca3460ead03628d6d2d3a4a4ffea17))
* **docs:** use environment variables for authentication in code snippets ([af6c346](https://github.com/limrun-inc/python-sdk/commit/af6c346ea2fdbce9e207e59d829253a0617fced6))
* update lockfile ([bd03e1b](https://github.com/limrun-inc/python-sdk/commit/bd03e1ba15189503e3617b052701e7ed69b9e7a2))

## 0.8.0 (2025-11-11)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/limrun-inc/python-sdk/compare/v0.7.0...v0.8.0)

### Features

* **api:** add assetId as asset source kind ([1aac770](https://github.com/limrun-inc/python-sdk/commit/1aac770249a41d2ceb6147cbe04cddf92ba23bbb))
* **api:** add comma-separated state for multi-state listings ([58b65a2](https://github.com/limrun-inc/python-sdk/commit/58b65a2e1c2a4970f480ac65b54e6408ecb981ce))
* **api:** add pagination for ios instances and assets as well ([123d228](https://github.com/limrun-inc/python-sdk/commit/123d2288130547b7e69f89cc9977e82baf813bee))
* **api:** add pagination to asset spec ([8be229c](https://github.com/limrun-inc/python-sdk/commit/8be229c8d4514cd2c033fe9cbb78221f14c64206))
* **api:** add reuseIfExists to creation endpoint ([4a0dd43](https://github.com/limrun-inc/python-sdk/commit/4a0dd43c17e8750e60f588e4fb2985d195daaa58))
* **api:** disable pagination for assets ([4b449fa](https://github.com/limrun-inc/python-sdk/commit/4b449fabb5b50dc0b3aea34a30f0ca0c29e26bb7))
* **api:** enable pagination for android_instances ([04130ef](https://github.com/limrun-inc/python-sdk/commit/04130ef1ab28bb6db9bef0727598c0c01950a3c3))
* **api:** manual updates ([52753ed](https://github.com/limrun-inc/python-sdk/commit/52753ed8cd09c24370aa3665e8310fefe7376562))
* **api:** manual updates ([e616c29](https://github.com/limrun-inc/python-sdk/commit/e616c29a6e3addbeab4788734dee903300a72b82))
* **api:** move pagination prop to openapi ([2d59a37](https://github.com/limrun-inc/python-sdk/commit/2d59a37ab0f2663a389ce65a1fba113ef5700720))
* **api:** regenerate new pagination fields ([83ff598](https://github.com/limrun-inc/python-sdk/commit/83ff598ecde93383f846fe55605633bfa744762a))
* **api:** update comment ([e6e7657](https://github.com/limrun-inc/python-sdk/commit/e6e7657d1a32dbde27a9fcaa3408e9b327432fe2))
* **api:** update to use LIM_API_KEY instead of LIM_TOKEN ([ba2e85e](https://github.com/limrun-inc/python-sdk/commit/ba2e85e00e7ee937ab8ceaf5f9119a7a4f74b49a))


### Bug Fixes

* compat with Python 3.14 ([c97037d](https://github.com/limrun-inc/python-sdk/commit/c97037dc5c683fcc72c5ce50b58ba1ee7951432a))


### Chores

* **package:** drop Python 3.8 support ([3be5696](https://github.com/limrun-inc/python-sdk/commit/3be5696b0cf40c1f02467d03e85c0181667fb9ea))

## 0.7.0 (2025-11-05)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/limrun-inc/python-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** add asset deletion endpoint ([e468855](https://github.com/limrun-inc/python-sdk/commit/e4688552f9edac991e15e0e3c9e052882b7c8e5f))
* **api:** add ios port-forward endpoint url to return type ([a636183](https://github.com/limrun-inc/python-sdk/commit/a6361831f2965f40dca0304c2a6a9b774b54a938))
* **api:** add launchMode to iOS asset object ([4e5bb3c](https://github.com/limrun-inc/python-sdk/commit/4e5bb3c6727312a6e2006d4a323685eeecd3344a))
* **api:** add the assigned state to both android and ios instance states ([0aa0e44](https://github.com/limrun-inc/python-sdk/commit/0aa0e4428f16befa8058ddaa81c432336b9ab621))


### Bug Fixes

* **client:** close streams without requiring full consumption ([f2fe77c](https://github.com/limrun-inc/python-sdk/commit/f2fe77cfdb1027a3bde5fe2ddfa763598ead2194))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([73d9600](https://github.com/limrun-inc/python-sdk/commit/73d960047c072bc1139fdbb2fdc7d8c8b844cdb4))
* **internal:** grammar fix (it's -&gt; its) ([7e8562b](https://github.com/limrun-inc/python-sdk/commit/7e8562bce0d40d2e239132d7fd9d0d5b1e8ee5a8))

## 0.6.0 (2025-10-29)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/limrun-inc/python-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** add explicit pagination fields ([c4756f3](https://github.com/limrun-inc/python-sdk/commit/c4756f391ef5094ffccd2988e49ae2fc2be3fe62))
* **api:** add os version clue ([7d0bda5](https://github.com/limrun-inc/python-sdk/commit/7d0bda58126acff22bf569828ea1c38abf144e0c))
* **api:** limit pagination only to limit parameter temporarily ([68a99e1](https://github.com/limrun-inc/python-sdk/commit/68a99e16648bd03a5edaebd4115b77fd5ab311f7))
* **api:** manual updates ([6301238](https://github.com/limrun-inc/python-sdk/commit/6301238cfadf4c89827fee3e2ecca0194b3e5b50))
* **api:** manual updates ([6dda9e7](https://github.com/limrun-inc/python-sdk/commit/6dda9e73f01b3cc6be13633b1a6f84bd4477ce18))
* **api:** os version description to show possible values ([a4d9cd3](https://github.com/limrun-inc/python-sdk/commit/a4d9cd3c2b77d85c010e0a9884b7aac36136e354))
* **api:** osVersion clue is available only in Android yet ([545f2db](https://github.com/limrun-inc/python-sdk/commit/545f2dbb4ce59f7288fa978df60b2b46a6ac8736))
* **api:** remaining pieces of pagionation removed temporarily ([73713dd](https://github.com/limrun-inc/python-sdk/commit/73713dd432d23023862e4d15a609c8ea4fdd9819))
* **api:** update assets and ios_instances endpoints with pagination ([95668d7](https://github.com/limrun-inc/python-sdk/commit/95668d74ca87e07403623c3a3ddcb93fa42820d6))
* **api:** update stainless schema for pagination ([3767bd6](https://github.com/limrun-inc/python-sdk/commit/3767bd695bef605b8d2169d4bb783864df90401f))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([ce7151e](https://github.com/limrun-inc/python-sdk/commit/ce7151eb8db959e77260d8da78343c91b7a36853))
* **internal:** detect missing future annotations with ruff ([5ea3e8e](https://github.com/limrun-inc/python-sdk/commit/5ea3e8e2ce8f057a8e22854221db80b5f8aa229c))

## 0.5.0 (2025-10-07)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/limrun-inc/python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** add the new multiple apk installation options ([58e81cc](https://github.com/limrun-inc/python-sdk/commit/58e81cc2074ef7a75dcc8ac25f50a0b2bf0f3c57))
* **api:** mark public urls as required ([0af09f5](https://github.com/limrun-inc/python-sdk/commit/0af09f54ee37d7b4cfe3d4b02d69faf412cf2442))
* **api:** revert api change ([5be7d22](https://github.com/limrun-inc/python-sdk/commit/5be7d225f832016734c449ba2fd6c906efd9646c))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([a810b55](https://github.com/limrun-inc/python-sdk/commit/a810b55f4f433cf81e91cc6384eb803d9178b75e))
* **internal:** update pydantic dependency ([21a183f](https://github.com/limrun-inc/python-sdk/commit/21a183f72ff7e281b0db44cd1f598fd7f73bffa9))
* **types:** change optional parameter type from NotGiven to Omit ([200fa8d](https://github.com/limrun-inc/python-sdk/commit/200fa8ddfca76d214e1b8c793ef5939a629d1b30))

## 0.4.0 (2025-09-12)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/limrun-inc/python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** manual updates ([7dbb780](https://github.com/limrun-inc/python-sdk/commit/7dbb780b65eae748a19c41154d41b4f24c153bd1))
* **api:** manual updates ([3836853](https://github.com/limrun-inc/python-sdk/commit/38368531d480706c4528c6bd0b4b94a94e788592))

## 0.3.0 (2025-09-11)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/limrun-inc/python-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** remove md5filter from list assets ([9e460d4](https://github.com/limrun-inc/python-sdk/commit/9e460d4e032d1549f0fb419bb871fd03a846f864))

## 0.2.0 (2025-09-09)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/limrun-inc/python-sdk/compare/v0.1.1...v0.2.0)

### Features

* **api:** manual updates ([9c3f233](https://github.com/limrun-inc/python-sdk/commit/9c3f2330f50cdeef71004c7ea10874cc4fc157d3))


### Chores

* update SDK settings ([eef22eb](https://github.com/limrun-inc/python-sdk/commit/eef22eba5f9ee08a1620cf7155306f01b9c0020c))

## 0.1.1 (2025-09-09)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/limrun-inc/python-sdk/compare/v0.1.0...v0.1.1)

### Chores

* update SDK settings ([e1a6a95](https://github.com/limrun-inc/python-sdk/commit/e1a6a95be568d7fd21fcbfeba3460b2934e84212))

## 0.1.0 (2025-09-08)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/limrun-inc/python-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([77b548c](https://github.com/limrun-inc/python-sdk/commit/77b548ca5977d8155954a4ad2da14086ef66de59))


### Chores

* configure new SDK language ([2c6c2f5](https://github.com/limrun-inc/python-sdk/commit/2c6c2f56099811070dc4c137f4cdbad18ec5c5a6))
* update SDK settings ([905181c](https://github.com/limrun-inc/python-sdk/commit/905181c229934fd82579ea0364b5d34f05b89138))
