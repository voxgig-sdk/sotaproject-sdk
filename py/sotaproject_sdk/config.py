# Sotaproject SDK configuration


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
            "name": "url",
            "short": "URL to the full publication",
            "type": "`$STRING`",
          },
        ],
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
                "parts": [
                  "tg-news",
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
