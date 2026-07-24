import re
import vitedoc
from vitedoc import Action, Feature


version = ""
with open("opentube/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

if __name__ == '__main__':
    vitedoc.init(
        base_dir="docs",
        title="OpenTube",
        description="Access YouTube Public Data without YouTubeAPI.",
        actions=[
            Action(
                theme="brand",
                text="Get started",
                link=f"/guide/{version}/introduction",
            ),
            Action(
                theme="alt",
                text="GitHub",
                link="https://github.com/jnsougata/opentube",
            ),
        ],
        features=[
            Feature(
                icon_emoji="🔑",
                title="No API Key Required",
                details="Access YouTube public data without the need for an API key, making it easier "
                        "to integrate into your applications."
            ),
            Feature(
                icon_emoji="🧩",
                title="Comprehensive Data Access",
                details="Retrieve a wide range of YouTube channel information, including metadata, playlists, and video details."
            )
        ]
    )