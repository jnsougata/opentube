import re

from .https import request


def _extract_og(prop: str, source: str):
    matched = re.search(rf'<meta property="og:{prop}" content="(.*?)">', source)
    return matched.group(1) if matched else None


def _extract_itemprop(prop: str, source: str, tag: str = "meta"):
    matched = re.search(rf'<{tag} itemprop="{prop}" content="(.*?)">', source)
    return matched.group(1) if matched else None


class Short:
    def __init__(self, url: str):
        self.url = url
        self._html = request(self.url)

    @property
    def author(self):
        matched = re.search(
            r'<span itemprop="author" itemscope itemtype="http://schema.org/Person">(.*?)</span>',
            self._html,
        )
        return {
            "name": _extract_itemprop("name", matched.group(1), "link"),
            "url": re.search(
                r'<link itemprop="url" href="(.*?)">', matched.group(1)
            ).group(1),
        }

    @property
    def title(self):
        return _extract_og("title", self._html)

    @property
    def description(self):
        return _extract_og("description", self._html)

    @property
    def thumbnail(self):
        return _extract_og("image", self._html)

    @property
    def date(self):
        return _extract_itemprop("datePublished", self._html)

    @property
    def regions_allowed(self):
        return _extract_itemprop("regionsAllowed", self._html).split(",")

    @property
    def genre(self):
        return _extract_itemprop("genre", self._html)

    @property
    def views(self):
        matched = re.search(r'"views":{"simpleText":"(.*?) views"},', self._html)
        return int(matched.group(1).replace(",", ""))

    @property
    def likes(self):
        matched = re.search(
            r'\[{"factoidRenderer":{"value":{"simpleText":"(.*?)"}', self._html
        )
        return matched.group(1)
