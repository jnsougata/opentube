---
title: opentube.channel
---

# `opentube.channel`

## Classes

- [Channel](#class-channel)

<a id="class-channel"></a>
## Channel

`opentube.channel.Channel`

### Property Index

- [available_country_codes](#channel-available-country-codes)
- [avatars](#channel-avatars)
- [banners](#channel-banners)
- [country](#channel-country)
- [creation_date](#channel-creation-date)
- [custom_url](#channel-custom-url)
- [description](#channel-description)
- [family_safe](#channel-family-safe)
- [id](#channel-id)
- [keywords](#channel-keywords)
- [last_streamed](#channel-last-streamed)
- [last_uploaded](#channel-last-uploaded)
- [live](#channel-live)
- [metadata](#channel-metadata)
- [name](#channel-name)
- [old_streams](#channel-old-streams)
- [rss_url](#channel-rss-url)
- [socials](#channel-socials)
- [streaming_now](#channel-streaming-now)
- [subscribers](#channel-subscribers)
- [upcoming](#channel-upcoming)
- [url](#channel-url)
- [verified](#channel-verified)
- [video_count](#channel-video-count)
- [views](#channel-views)

### Method Index

- [playlists](#channel-playlists)
- [shorts](#channel-shorts)
- [videos](#channel-videos)

### Properties

<a id="channel-available-country-codes"></a>
#### `available_country_codes`

Returns the list of country codes where the channel is available.
#### _Returns_

- **Type:** `List[str]`
  - The list of country codes where the channel is available

<a id="channel-avatars"></a>
#### `avatars`

Returns the avatars of the channel in different resolutions.
#### _Returns_

- **Type:** `List[Dict[str, Any]]`
  - The avatars of the channel.

<a id="channel-banners"></a>
#### `banners`

Returns the banners of the channel in different resolutions.
#### _Returns_

- **Type:** `List[Dict[str, Any]]`
  - The banners of the channel.

<a id="channel-country"></a>
#### `country`

Returns the country of the channel if available.
#### _Returns_

- **Type:** `str | None`
  - The country of the channel if available.

<a id="channel-creation-date"></a>
#### `creation_date`

Returns the date of creation of the channel.
#### _Returns_

- **Type:** `str`
  - The date of creation of the channel.

<a id="channel-custom-url"></a>
#### `custom_url`

Returns the user created custom url of the channel.
#### _Returns_

- **Type:** `str`
  - The user created custom url of the channel.

<a id="channel-description"></a>
#### `description`

Returns the description of the channel.
#### _Returns_

- **Type:** `str`
  - The description of the channel.

<a id="channel-family-safe"></a>
#### `family_safe`

Returns whether the channel is marked as family safe.
#### _Returns_

- **Type:** `bool`
  - True if the channel is marked as family safe, False otherwise.

<a id="channel-id"></a>
#### `id`

Returns the unique id of the channel.
#### _Returns_

- **Type:** `str`
  - The unique id of the channel.

<a id="channel-keywords"></a>
#### `keywords`

Returns the keywords of the channel.
#### _Returns_

- **Type:** `List[str]`
  - The keywords of the channel.

<a id="channel-last-streamed"></a>
#### `last_streamed`

Fetches the id of the last completed livestream.
#### _Returns_

- **Type:** `str | None`
  - The id of the last livestreamed video or None.

<a id="channel-last-uploaded"></a>
#### `last_uploaded`

Fetches the id of the last uploaded video.
#### _Returns_

- **Type:** `Dict[str, Any] | None`
  - The id of the last uploaded video or None.

<a id="channel-live"></a>
#### `live`

Returns whether the channel is currently livestreaming.
#### _Returns_

- **Type:** `bool`
  - True if the channel is currently livestreaming, False otherwise.

<a id="channel-metadata"></a>
#### `metadata`

Returns channel metadata in a python dictionary format.
#### _Returns_

- **Type:** `Dict`
  - Channel metadata containing the keys like id, name, subscribers, views, country, custom_url, avatar, banner, url, description, socials etc.

<a id="channel-name"></a>
#### `name`

Returns the name of the channel.
#### _Returns_

- **Type:** `str`
  - The name of the channel.

<a id="channel-old-streams"></a>
#### `old_streams`

Fetches the ids of all old or completed livestreams.
#### _Returns_

- **Type:** `List[str] | None`
  - The ids of all old or completed streams or None.

<a id="channel-rss-url"></a>
#### `rss_url`

Returns the rss url of the channel.
#### _Returns_

- **Type:** `str`
  - The rss url of the channel.

<a id="channel-socials"></a>
#### `socials`

Returns the socials of the channel.
#### _Returns_

- **Type:** `List[str]`
  - The socials of the channel.

<a id="channel-streaming-now"></a>
#### `streaming_now`

Fetches the ids of all ongoing livestreams.
#### _Returns_

- **Type:** `List[str] | None`
  - The ids of all ongoing streams or None.

<a id="channel-subscribers"></a>
#### `subscribers`

Returns the subscriber count of the channel.
#### _Returns_

- **Type:** `str`
  - The subscriber count of the channel.

<a id="channel-upcoming"></a>
#### `upcoming`

Fetches the upcoming scheduled videos.
#### _Returns_

- **Type:** `List[str] | None`
  - The ids of upcoming scheduled videos or None.

<a id="channel-url"></a>
#### `url`

Returns the url of the channel.
#### _Returns_

- **Type:** `str`
  - The url of the channel.

<a id="channel-verified"></a>
#### `verified`

Returns whether the channel is verified by YouTube.
#### _Returns_

- **Type:** `bool`
  - True if the channel is verified, False otherwise

<a id="channel-video-count"></a>
#### `video_count`

Returns the total number of videos uploaded in the channel.
#### _Returns_

- **Type:** `int`
  - The total number of videos uploaded in the channel.

<a id="channel-views"></a>
#### `views`

Returns the total number of views the channel got across all videos.
#### _Returns_

- **Type:** `str`
  - The total number of views the channel got across all videos.

### Methods

<a id="channel-playlists"></a>
#### `playlists`

```python
playlists(self) -> List[Dict[str, Any]] | None
```

Fetches the basic metadata of some public playlists.
#### _Returns_

- **Type:** `List[Dict[str, Any]] | None`
  - The basic metadata of all playlists or None.

<a id="channel-shorts"></a>
#### `shorts`

```python
shorts(self) -> Dict[str, Any] | None
```

Fetches uploaded shorts and their basic metadata.
#### _Returns_

- **Type:** `Dict[str, Any] | None`
  - A dict containing basic metadata of uploaded shorts or None.

<a id="channel-videos"></a>
#### `videos`

```python
videos(self) -> Dict[str, Any] | None
```

Fetches upto 30 uploaded videos and their basic metadata.
#### _Returns_

- **Type:** `Dict[str, Any] | None`
  - A dict containing basic metadata of uploaded videos or None.

