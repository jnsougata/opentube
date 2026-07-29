import re
from typing import List

from .https import request


def _extract_og(prop: str, source: str):
    matched = re.search(rf'<meta property="og:{prop}" content="(.*?)">', source)
    return matched.group(1) if matched else None


def _extract_itemprop(prop: str, source: str, tag: str = "meta"):
    matched = re.search(rf'<{tag} itemprop="{prop}" content="(.*?)">', source)
    return matched.group(1) if matched else None


class Short:
    """
    Represents a YouTube Short video and provides methods to extract its metadata.
    """
    def __init__(self, url: str):
        self.url = url
        self._html = request(self.url)

    @property
    def author(self):
        """
        Returns the author of the short video.

        Returns:
            Dict[str, str]: Author of the short video.
        """
        matched = re.search(
            r'<span itemprop="author" itemscope itemtype="http://schema.org/Person">(.*?)</span>',
            self._html,
        )
        return {
            "name": _extract_itemprop("name", matched.group(1), "link"),
            "url": re.search(
                r'<link itemprop="url" href="(.*?)">', matched.group(1)
            ).group(1)
        }

    @property
    def title(self) -> str:
        """
        Returns the title of the short video.

        Returns:
            str: Title of the short video.
        """
        return _extract_og("title", self._html)

    @property
    def description(self) -> str:
        """
        Returns the description of the short video.

        Returns:
            str: Description of the short video.
        """
        return _extract_og("description", self._html)

    @property
    def thumbnail(self) -> str:
        """
        Returns the thumbnail of the short video.

        Returns:
            str: Thumbnail url of the short video.
        """
        return _extract_og("image", self._html)

    @property
    def date(self) -> str:
        """
        Returns the date of publishing of the short video.

        Returns:
            str: Date of publishing of the short video.
        """
        return _extract_itemprop("datePublished", self._html)

    @property
    def regions_allowed(self) -> List[str]:
        """
        Returns the regions allowed for the short video.

        Returns:
            List[str]: List of regions allowed for the short video.
        """
        return _extract_itemprop("regionsAllowed", self._html).split(",")

    @property
    def genre(self) -> str:
        """
        Returns the genre of the short video.

        Returns:
            str: Genre of the short video.
        """
        return _extract_itemprop("genre", self._html)

    @property
    def views(self) -> int:
        """
        Returns the view count of the short video.

        Returns:
            int: View count of the short video.
        """
        matched = re.search(r'"views":{"simpleText":"(.*?) views"},', self._html)
        return int(matched.group(1).replace(",", ""))

    @property
    def likes(self) -> str:
        """
        Returns the likes count of the short video.

        Returns:
            str: Likes count of the short video.
        """
        matched = re.search(
            r'\[{"factoidRenderer":{"value":{"simpleText":"(.*?)"}', self._html
        )
        return matched.group(1)
