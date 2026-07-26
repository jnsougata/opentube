import json
import re
from typing import Any, Dict, List, Optional

from .https import video_data
from .utils import extract_initial_data


# noinspection shadowing-builtins
class Video:

    _HEAD = "https://www.youtube.com/watch?v="

    def __init__(self, id: str):
        """
        Represents a YouTube video.

        args:
            id (str): The id or url of the video.
        """
        pattern = re.compile(r".be/(.*?)$|=(.*?)$|^(\w{11})$")
        self._matched_id = (
            pattern.search(id).group(1)
            or pattern.search(id).group(2)
            or pattern.search(id).group(3)
        )
        if self._matched_id:
            self._url = self._HEAD + self._matched_id
            self._raw_html = video_data(self._matched_id)
            self._video_data = extract_initial_data(self._raw_html)
            self._info_section = self._video_data["contents"][
                "twoColumnWatchNextResults"
            ]["results"]["results"]["contents"]
            self._primary_info = None
            self._secondary_info = None
            for section in self._info_section:
                _primary_info = section.get("videoPrimaryInfoRenderer")
                if _primary_info:
                    self._primary_info = _primary_info
                _secondary_info = section.get("videoSecondaryInfoRenderer")
                if _secondary_info:
                    self._secondary_info = _secondary_info

        else:
            raise ValueError("Invalid video id or url.")

    def __repr__(self):
        return f"<Video {self._url}>"

    @property
    def url(self) -> str:
        """
        Returns the url of the video.

        Returns:
            str: Url of the video.
        """
        return self._url

    @property
    def title(self) -> Optional[str]:
        """
        Returns the title of the video.

        Returns:
            str: Title of the video.
        """
        if self._primary_info:
            return (
                self._primary_info.get("title", {}).get("runs", [{}])[0].get("text", "")
            )
        return None

    @property
    def description(self) -> Optional[str]:
        """
        Returns the description of the video.

        Returns:
            str: Description of the video.
        """
        if self._secondary_info:
            return self._secondary_info.get("attributedDescription", {}).get("content")
        return None

    @property
    def thumbnail(self) -> str:
        """
        Returns the thumbnail of the video.

        Returns:
            str: Thumbnail of the video.
        """
        return f"https://i.ytimg.com/vi/{self._matched_id}/maxresdefault.jpg"

    @property
    def views(self) -> str:
        """
        Returns the view count of the video.

        Returns:
            str: View count of the video.
        """
        return (
            (
                self._primary_info["viewCount"]["videoViewCountRenderer"]["viewCount"][
                    "simpleText"
                ]
            )
            .replace("views", "")
            .replace(",", "")
            .strip()
        )

    @property
    def published(self) -> str:
        """
        Returns the date of publication of the video.

        Returns:
            str: Date of publication of the video.
        """
        return self._primary_info["dateText"]["simpleText"]

    @property
    def likes(self) -> Optional[str]:
        """
        Returns the likes count of the video.

        Returns:
            str | None: Likes count of the video.
        """
        # YouTube is not consistent with the data structure for likes across all videos,
        # so we have to use regex to extract it from the string representation of the data.
        # It's a lot faster than traversing deeply nested JSON.
        matched = re.search(
            r"{'iconName': 'LIKE', 'title': (.*?),",
            str(self._primary_info["videoActions"]),
        )
        if matched:
            return matched.group(1).strip("'")
        return None

    @property
    def owner(self) -> Optional[Dict[str, Any]]:
        """
        Returns the details such as, id, title, avatars, subscribers of the owner of the video.

        Returns:
            Dict[str, Any]: Details of the owner.
        """
        return {
            "title": self._secondary_info["owner"]["videoOwnerRenderer"]["title"][
                "runs"
            ][0]["text"],
            "id": self._secondary_info["owner"]["videoOwnerRenderer"]["title"]["runs"][
                0
            ]["navigationEndpoint"]["browseEndpoint"]["browseId"],
            "avatars": self._secondary_info["owner"]["videoOwnerRenderer"]["thumbnail"][
                "thumbnails"
            ],
            "subscribers": self._secondary_info["owner"]["videoOwnerRenderer"][
                "subscriberCountText"
            ]["simpleText"],
        }

    @property
    def duration_ms(self) -> int:
        """
        Returns the approximate duration of the video in milliseconds.

        Returns:
            int: Duration of the video.
        """
        matched = re.search(r"\"approxDurationMs\":(.*?),", self._raw_html)
        return int(matched.group(1).strip('"'))  # noqa

    @property
    def genre(self) -> Optional[str]:
        """
        Returns the genre of the video.

        Returns:
            str | None: Genre of the video.
        """
        matched = re.search(r"<meta itemprop=\"genre\" content=(.*?)>", self._raw_html)
        if matched:
            return matched.group(1).strip('"')
        return None

    @property
    def keywords(self) -> Optional[List[str]]:
        """
        Returns the keywords of the video.

        Returns:
            List[str] | None: Keywords of the video.
        """
        matched = re.search(r"<meta name=\"keywords\" content=(.*?)>", self._raw_html)
        if matched:
            return matched.group(1).strip('"').split(",")  # noqa
        return None

    @property
    def livestream(self) -> bool:
        """
        Returns whether the video is a livestream or not.

        Returns:
            bool: True if the video is a livestream, False otherwise.
        """
        matched = re.search(r"\"isLiveContent\":(.*?),", self._raw_html)
        if matched:
            return matched.group(1).strip('"') == "true"
        return False

    @property
    def watermark(self) -> Optional[str]:
        """
        Returns the watermark image url of the video.

        Returns:
            str | None: Watermark of the video.
        """
        matched = re.search(r"\"watermark\":(.*?),", self._raw_html)
        if matched:
            return json.loads(matched.group(1).strip('"') + '"}]}')["thumbnails"][0][
                "url"
            ]
        return None
