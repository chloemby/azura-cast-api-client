This Python library provides an API client for AzuraCast JSON API.

# Installation

```bash
pip install git+https://github.com/chloemby/azura-cast-api-client.git
```

# Usage

```python3
from azura_cast_api_client import AzuraCastApi

api = AzuraCastApi(HOST, API_KEY)

response = await api.nowplaying()
```

