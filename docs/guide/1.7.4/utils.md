---
title: opentube.utils
---

# `opentube.utils`

## Functions

- [dup_filter](#dup-filter)
- [extract_initial_data](#extract-initial-data)
- [request](#request)

<a id="dup-filter"></a>
## `dup_filter`

**Qualified Name:** `opentube.utils.dup_filter`

### Signature

```python
dup_filter(iterable: list, limit: int | None = None) -> List[Any]
```

Utility function for filtering out duplicate items.
#### _Arguments_

- _**iterable** (`list`): The list of items to filter._
- _**limit** (`Optional[int]`): The maximum number of items to return._


<a id="extract-initial-data"></a>
## `extract_initial_data`

**Qualified Name:** `opentube.utils.extract_initial_data`

### Signature

```python
extract_initial_data(html: str) -> Any
```

Utility function for extracting the initial data from the HTML of a YouTube page.
#### _Arguments_

- _**html** (`str`): The HTML of the YouTube page._


<a id="request"></a>
## `request`

**Qualified Name:** `opentube.utils.request`

### Signature

```python
request(url: str)
```

The base function for making a request with proper headers.
#### _Arguments_

- _**url** (`str`): The url to make a request._

