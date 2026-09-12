# Sotaproject SDK configuration


# The sekreto plugin DEFINITIONS the model selected per feature, imported
# above by name from the modules the catalogue's active `plugin.def`
# entries declare. Handed to each feature (secrets builds its Sekreto
# with them): a provider kind not listed here is unknown to that SDK.
FEATURE_PLUGINS = {
}


_shared_config = None


def shared_config():
    """Return the process-wide config, built once on first use.

    The SDK reads the config on every request and never writes to it, so one
    instance is shared by every client rather than rebuilt per client.

    The returned dict is shared: treat it as read-only. Callers that need to
    mutate should use make_config, which always returns a fresh copy.
    """
    global _shared_config
    if _shared_config is None:
        _shared_config = make_config()
    return _shared_config


def make_config():
    """Build a fresh, fully materialised config dict.

    Every call rebuilds the whole structure, so prefer shared_config unless
    you need a private copy you intend to mutate.
    """
    return {
        "main": {
            "name": "Sotaproject",
            "slug": "sotaproject",
            "version": "0.0.1",
            "target": "py",
        },
        "feature": {
            "test": {
        "options": {
          "active": False,
        },
        "transport": "base",
      },
        },
        "options": {
            "base": "https://sotaproject.com/api/v1",
            "headers": {
        "content-type": "application/json",
      },
            "entity": {
                "publication": {},
            },
        },
        "entity": {
      "publication": {
        "fields": [
          {
            "name": "author",
            "short": "Author of the publication",
            "type": "`$STRING`",
          },
          {
            "name": "category",
            "short": "Category of the publication (e.g., investigation, news)",
            "type": "`$STRING`",
          },
          {
            "name": "content",
            "short": "Content body of the publication",
            "type": "`$STRING`",
          },
          {
            "name": "id",
            "short": "Unique identifier for the publication",
            "type": "`$STRING`",
          },
          {
            "name": "media",
            "short": "Media content associated with the publication",
            "type": "`$ARRAY`",
          },
          {
            "format": "date-time",
            "name": "published_at",
            "short": "Publication date and time",
            "type": "`$STRING`",
          },
          {
            "name": "title",
            "short": "Title of the publication",
            "type": "`$STRING`",
          },
          {
            "format": "uri",
            "name": "url",
            "short": "URL to the full publication",
            "type": "`$STRING`",
          },
        ],
        "id": {
          "field": "id",
          "name": "id",
        },
        "name": "publication",
        "op": {
          "list": {
            "input": "data",
            "name": "list",
            "points": [
              {
                "args": {
                  "query": [
                    {
                      "example": 50,
                      "kind": "query",
                      "name": "limit",
                      "orig": "limit",
                      "type": "`$INTEGER`",
                    },
                    {
                      "example": 0,
                      "kind": "query",
                      "name": "offset",
                      "orig": "offset",
                      "type": "`$INTEGER`",
                    },
                  ],
                },
                "kind": "http",
                "method": "GET",
                "orig": "/tg-news",
                "segments": [
                  {
                    "lit": "tg-news",
                  },
                ],
                "select": {
                  "exist": [
                    "limit",
                    "offset",
                  ],
                },
                "transform": {
                  "req": "`reqdata`",
                  "res": "`body.publications`",
                },
                "parts": [
                  "tg-news",
                ],
              },
            ],
          },
        },
        "relations": {
          "ancestors": [],
        },
      },
    },
    }
