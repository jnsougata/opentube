---
title: opentube.video
---

# `opentube.video`

## Classes

- [Video](#class-video)

<a id="class-video"></a>
## Video

`opentube.video.Video`

### Property Index

- [description](#video-description)
- [duration_ms](#video-duration-ms)
- [genre](#video-genre)
- [keywords](#video-keywords)
- [likes](#video-likes)
- [livestream](#video-livestream)
- [owner](#video-owner)
- [published](#video-published)
- [thumbnail](#video-thumbnail)
- [title](#video-title)
- [url](#video-url)
- [views](#video-views)
- [watermark](#video-watermark)

### Properties

<a id="video-description"></a>
#### `description`

Returns the description of the video.
#### _Returns_

- **Type:** `str`
  - Description of the video.

<a id="video-duration-ms"></a>
#### `duration_ms`

Returns the approximate duration of the video in milliseconds.
#### _Returns_

- **Type:** `int`
  - Duration of the video.

<a id="video-genre"></a>
#### `genre`

Returns the genre of the video.
#### _Returns_

- **Type:** `str | None`
  - Genre of the video.

<a id="video-keywords"></a>
#### `keywords`

Returns the keywords of the video.
#### _Returns_

- **Type:** `List[str] | None`
  - Keywords of the video.

<a id="video-likes"></a>
#### `likes`

Returns the likes count of the video.
#### _Returns_

- **Type:** `str | None`
  - Likes count of the video.

<a id="video-livestream"></a>
#### `livestream`

Returns whether the video is a livestream or not.
#### _Returns_

- **Type:** `bool`
  - True if the video is a livestream, False otherwise.

<a id="video-owner"></a>
#### `owner`

Returns the details such as, id, title, avatars, subscribers of the owner of the video.
#### _Returns_

- **Type:** `Dict[str, Any]`
  - Details of the owner.

<a id="video-published"></a>
#### `published`

Returns the date of publication of the video.
#### _Returns_

- **Type:** `str`
  - Date of publication of the video.

<a id="video-thumbnail"></a>
#### `thumbnail`

Returns the thumbnail of the video.
#### _Returns_

- **Type:** `str`
  - Thumbnail of the video.

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

<a id="video-views"></a>
#### `views`

Returns the view count of the video.
#### _Returns_

- **Type:** `str`
  - View count of the video.

<a id="video-watermark"></a>
#### `watermark`

Returns the watermark image url of the video.
#### _Returns_

- **Type:** `str | None`
  - Watermark of the video.

