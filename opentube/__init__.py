"""
Access YouTube Public Data without YouTubeAPI.
"""

__title__ = "OpenTube"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present Sougata Jana"
__author__ = "Sougata Jana"
__version__ = "1.7.4"
__url__ = "https://github.com/jnsougata/opentube"

from .channel import Channel
from .errors import *
from .extras import Extras
from .playlist import Playlist
from .query import Search
from .video import Video
