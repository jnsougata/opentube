from typing import List, Optional

from .https import (_get_trending_learning_videos, trending_feeds,
                    trending_games, trending_songs, trending_sports,
                    trending_streams, trending_videos)
from .patterns import _ExtraPatterns as Patterns
from .utils import dup_filter


class Extras:

    @staticmethod
    def trending_videos() -> Optional[List[str]]:
        data = Patterns.video_id.findall(trending_videos())
        return dup_filter(data) if data else None

    @staticmethod
    def music_videos() -> Optional[List[str]]:
        data = Patterns.video_id.findall(trending_songs())
        return dup_filter(data) if data else None

    @staticmethod
    def gaming_videos() -> Optional[List[str]]:
        return dup_filter(Patterns.video_id.findall(trending_games()))

    @staticmethod
    def news_videos() -> Optional[List[str]]:
        return dup_filter(Patterns.video_id.findall(trending_feeds()))

    @staticmethod
    def live_videos() -> Optional[List[str]]:
        return dup_filter(Patterns.video_id.findall(trending_streams()))

    @staticmethod
    def educational_videos() -> Optional[List[str]]:
        return dup_filter(Patterns.video_id.findall(_get_trending_learning_videos()))

    @staticmethod
    def sport_videos() -> Optional[List[str]]:
        return dup_filter(Patterns.video_id.findall(trending_sports()))
