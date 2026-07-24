import { defineConfig } from "vitepress";

export default defineConfig({
    base: "/opentube/",
    title: "OpenTube",
    description: "Access YouTube Public Data without YouTubeAPI.",
    cleanUrls: true,

    head: [
    [
        "link",
        {
            "rel": "icon",
            "href": "/logo.png"
        }
    ]
],

    themeConfig: {
        logo: "/logo.png",

        nav: [],

        editLink: {
            pattern: "",
        },

        sidebar: [
    {
        "text": "Introduction",
        "link": "/guide/1.7.4/introduction"
    },
    {
        "text": "Reference",
        "items": [
            {
                "text": "Channel",
                "link": "/guide/1.7.4/channel"
            },
            {
                "text": "Errors",
                "link": "/guide/1.7.4/errors"
            },
            {
                "text": "Extras",
                "link": "/guide/1.7.4/extras"
            },
            {
                "text": "Https",
                "link": "/guide/1.7.4/https"
            },
            {
                "text": "Patterns",
                "link": "/guide/1.7.4/patterns"
            },
            {
                "text": "Playlist",
                "link": "/guide/1.7.4/playlist"
            },
            {
                "text": "Pool",
                "link": "/guide/1.7.4/pool"
            },
            {
                "text": "Query",
                "link": "/guide/1.7.4/query"
            },
            {
                "text": "Stream",
                "link": "/guide/1.7.4/stream"
            },
            {
                "text": "Utils",
                "link": "/guide/1.7.4/utils"
            },
            {
                "text": "Video",
                "link": "/guide/1.7.4/video"
            }
        ]
    }
],

        search: {
            provider: "local",
            options: {
                _render: (src, env, md) => {
                    if (env.relativePath.startsWith("docs")) {
                        return "";
                    }
                    return md.render(src, env);
                },
            },
        },

        socialLinks: [],
    },
});
