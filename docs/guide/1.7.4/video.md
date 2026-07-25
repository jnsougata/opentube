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

- [description](#video-description)
- [metadata](#video-metadata)
- [title](#video-title)
- [url](#video-url)

### Properties

<a id="video-description"></a>
#### `description`

Returns the description of the video.
#### _Returns_

- **Type:** `str`
  - Description of the video.

<a id="video-metadata"></a>
#### `metadata`

Fetches video metadata in a dict format
Returns
-------
Dict
Video metadata in a dict format containing keys: title, id, views, duration, author_id,
upload_date, url, thumbnails, tags, description

<a id="video-title"></a>
#### `title`

Returns the title of the video.
#### _Returns_

- **Type:** `str`
  - Title of the video.

<a id="video-url"></a>
#### `url`

Returns the url of the video.
#### _Returns_

- **Type:** `str`
  - Url of the video.


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

