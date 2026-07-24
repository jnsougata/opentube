---
title: opentube.video
---

# `opentube.video`

## Classes

- [Video](#class-video)
- [_EngagementPanelType](#class--engagementpaneltype)

<a id="class-video"></a>
## Video

`opentube.video.Video`

### Property Index

- [metadata](#video-metadata)

### Properties

<a id="video-metadata"></a>
#### `metadata`

Fetches video metadata in a dict format
Returns
-------
Dict
Video metadata in a dict format containing keys: title, id, views, duration, author_id,
upload_date, url, thumbnails, tags, description


<a id="class--engagementpaneltype"></a>
## _EngagementPanelType

`opentube.video._EngagementPanelType`

Create a collection of name/value pairs.
Example enumeration:
>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3
Access them by:
- attribute access:
>>> Color.RED
<Color.RED: 1>
- value lookup:
>>> Color(1)
<Color.RED: 1>
- name lookup:
>>> Color['RED']
<Color.RED: 1>
Enumerations can be iterated over, and know how many members they have:
>>> len(Color)
3
>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

### Inheritance

- `enum.Enum`

