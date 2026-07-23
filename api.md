# AndroidInstances

Types:

```python
from limrun_api.types import AndroidInstance
```

Methods:

- <code title="post /v1/android_instances">client.android_instances.<a href="./src/limrun_api/resources/android_instances.py">create</a>(\*\*<a href="src/limrun_api/types/android_instance_create_params.py">params</a>) -> <a href="./src/limrun_api/types/android_instance.py">AndroidInstance</a></code>
- <code title="get /v1/android_instances">client.android_instances.<a href="./src/limrun_api/resources/android_instances.py">list</a>(\*\*<a href="src/limrun_api/types/android_instance_list_params.py">params</a>) -> <a href="./src/limrun_api/types/android_instance.py">SyncItems[AndroidInstance]</a></code>
- <code title="delete /v1/android_instances/{id}">client.android_instances.<a href="./src/limrun_api/resources/android_instances.py">delete</a>(id) -> None</code>
- <code title="get /v1/android_instances/{id}">client.android_instances.<a href="./src/limrun_api/resources/android_instances.py">get</a>(id) -> <a href="./src/limrun_api/types/android_instance.py">AndroidInstance</a></code>

# Assets

Types:

```python
from limrun_api.types import Asset, AssetListResponse, AssetGetOrCreateResponse
```

Methods:

- <code title="get /v1/assets">client.assets.<a href="./src/limrun_api/resources/assets.py">list</a>(\*\*<a href="src/limrun_api/types/asset_list_params.py">params</a>) -> <a href="./src/limrun_api/types/asset_list_response.py">AssetListResponse</a></code>
- <code title="delete /v1/assets/{assetId}">client.assets.<a href="./src/limrun_api/resources/assets.py">delete</a>(asset_id) -> None</code>
- <code title="get /v1/assets/{assetId}">client.assets.<a href="./src/limrun_api/resources/assets.py">get</a>(asset_id, \*\*<a href="src/limrun_api/types/asset_get_params.py">params</a>) -> <a href="./src/limrun_api/types/asset.py">Asset</a></code>
- <code title="put /v1/assets">client.assets.<a href="./src/limrun_api/resources/assets.py">get_or_create</a>(\*\*<a href="src/limrun_api/types/asset_get_or_create_params.py">params</a>) -> <a href="./src/limrun_api/types/asset_get_or_create_response.py">AssetGetOrCreateResponse</a></code>

# IosInstances

Types:

```python
from limrun_api.types import IosInstance
```

Methods:

- <code title="post /v1/ios_instances">client.ios_instances.<a href="./src/limrun_api/resources/ios_instances.py">create</a>(\*\*<a href="src/limrun_api/types/ios_instance_create_params.py">params</a>) -> <a href="./src/limrun_api/types/ios_instance.py">IosInstance</a></code>
- <code title="get /v1/ios_instances">client.ios_instances.<a href="./src/limrun_api/resources/ios_instances.py">list</a>(\*\*<a href="src/limrun_api/types/ios_instance_list_params.py">params</a>) -> <a href="./src/limrun_api/types/ios_instance.py">SyncItems[IosInstance]</a></code>
- <code title="delete /v1/ios_instances/{id}">client.ios_instances.<a href="./src/limrun_api/resources/ios_instances.py">delete</a>(id) -> None</code>
- <code title="get /v1/ios_instances/{id}">client.ios_instances.<a href="./src/limrun_api/resources/ios_instances.py">get</a>(id) -> <a href="./src/limrun_api/types/ios_instance.py">IosInstance</a></code>

# XcodeInstances

Types:

```python
from limrun_api.types import XcodeInstance
```

Methods:

- <code title="post /v1/xcode_instances">client.xcode_instances.<a href="./src/limrun_api/resources/xcode_instances.py">create</a>(\*\*<a href="src/limrun_api/types/xcode_instance_create_params.py">params</a>) -> <a href="./src/limrun_api/types/xcode_instance.py">XcodeInstance</a></code>
- <code title="get /v1/xcode_instances">client.xcode_instances.<a href="./src/limrun_api/resources/xcode_instances.py">list</a>(\*\*<a href="src/limrun_api/types/xcode_instance_list_params.py">params</a>) -> <a href="./src/limrun_api/types/xcode_instance.py">SyncItems[XcodeInstance]</a></code>
- <code title="delete /v1/xcode_instances/{id}">client.xcode_instances.<a href="./src/limrun_api/resources/xcode_instances.py">delete</a>(id) -> None</code>
- <code title="get /v1/xcode_instances/{id}">client.xcode_instances.<a href="./src/limrun_api/resources/xcode_instances.py">get</a>(id) -> <a href="./src/limrun_api/types/xcode_instance.py">XcodeInstance</a></code>

# Analytics

Types:

```python
from limrun_api.types import AnalyticsInstancesResponse, AnalyticsResponse
```

Methods:

- <code title="get /v1/analytics">client.analytics.<a href="./src/limrun_api/resources/analytics.py">get</a>(\*\*<a href="src/limrun_api/types/analytics_get_params.py">params</a>) -> <a href="./src/limrun_api/types/analytics_response.py">AnalyticsResponse</a></code>
- <code title="get /v1/analytics/instances">client.analytics.<a href="./src/limrun_api/resources/analytics.py">get_instances</a>(\*\*<a href="src/limrun_api/types/analytics_get_instances_params.py">params</a>) -> <a href="./src/limrun_api/types/analytics_instances_response.py">AnalyticsInstancesResponse</a></code>

# ScopedTokens

Types:

```python
from limrun_api.types import ScopedToken
```

Methods:

- <code title="post /v1/scoped_tokens">client.scoped_tokens.<a href="./src/limrun_api/resources/scoped_tokens.py">create</a>(\*\*<a href="src/limrun_api/types/scoped_token_create_params.py">params</a>) -> <a href="./src/limrun_api/types/scoped_token.py">ScopedToken</a></code>
