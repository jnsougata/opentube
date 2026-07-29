import json
import re
from collections import OrderedDict
from typing import Any, List, Optional
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from .errors import InvalidURL, RequestError, TooManyRequests

__all__ = ["dup_filter", "request", "extract_initial_data"]


def request(url: str):
    """
    The base function for making a request with proper headers.

    Args:
        url (str): The url to make a request.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/107.0.0.0 Safari/537.36"
        ),
    }
    req = Request(url, headers=headers)
    try:
        return urlopen(req).read().decode("utf-8")
    except HTTPError as e:
        if e.code == 404:
            raise InvalidURL("can not find anything with the requested url")
        if e.code == 429:
            raise TooManyRequests(
                "you are being rate-limited for sending too many requests"
            )
    except Exception as e:
        raise RequestError(f"{e!r}") from None


def dup_filter(iterable: list, limit: Optional[int] = None) -> List[Any]:
    """
    Utility function for filtering out duplicate items.

    Args:
        iterable (list): The list of items to filter.
        limit (Optional[int]): The maximum number of items to return.
    """
    if not iterable:
        return []
    lim = limit if limit else len(iterable)
    converted = list(OrderedDict.fromkeys(iterable))
    if len(converted) - lim > 0:
        return converted[: -len(converted) + lim]
    else:
        return converted


def extract_initial_data(html: str) -> Any:
    """
    Utility function for extracting the initial data from the HTML of a YouTube page.

    Args:
        html (str): The HTML of the YouTube page.
    """
    pattern = re.compile("ytInitialData = {(.+?)};")
    results = pattern.finditer(html)
    return json.loads("{" + results.__next__().group(1) + "}")
