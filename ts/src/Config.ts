
import { BaseFeature } from './feature/base/BaseFeature'
import { TestFeature } from './feature/test/TestFeature'



const FEATURE_CLASS: Record<string, typeof BaseFeature> = {
   test: TestFeature,

}


class Config {

  makeFeature(this: any, fn: string) {
    const fc = FEATURE_CLASS[fn]
    const fi = new fc()
    // TODO: errors etc
    return fi
  }

  // False for a feature added at runtime via options.extend (station's
  // adopt path) - the constructor uses this to skip makeFeature for names
  // no generated class backs.
  hasFeature(this: any, fn: string) {
    return null != FEATURE_CLASS[fn]
  }


  main = {
    name: 'Sotaproject',
        slug: "sotaproject",
    version: "0.0.1",
    target: "ts",

  }


  feature = {
     test:     {
      "options": {
        "active": false
      },
      "transport": "base"
    },

  }


  options = {
    base: "https://sotaproject.com/api/v1",

    headers: {
      "content-type": "application/json"
    },

    entity: {
      
      publication: {
      },

    }
  }


  entity = {
    "publication": {
      "fields": [
        {
          "name": "author",
          "short": "Author of the publication",
          "type": "`$STRING`"
        },
        {
          "name": "category",
          "short": "Category of the publication (e.g., investigation, news)",
          "type": "`$STRING`"
        },
        {
          "name": "content",
          "short": "Content body of the publication",
          "type": "`$STRING`"
        },
        {
          "name": "id",
          "short": "Unique identifier for the publication",
          "type": "`$STRING`"
        },
        {
          "name": "media",
          "short": "Media content associated with the publication",
          "type": "`$ARRAY`"
        },
        {
          "name": "published_at",
          "short": "Publication date and time",
          "type": "`$STRING`"
        },
        {
          "name": "title",
          "short": "Title of the publication",
          "type": "`$STRING`"
        },
        {
          "name": "url",
          "short": "URL to the full publication",
          "type": "`$STRING`"
        }
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
                    "type": "`$INTEGER`"
                  },
                  {
                    "example": 0,
                    "kind": "query",
                    "name": "offset",
                    "orig": "offset",
                    "type": "`$INTEGER`"
                  }
                ]
              },
              "kind": "http",
              "method": "GET",
              "orig": "/tg-news",
              "parts": [
                "tg-news"
              ],
              "select": {
                "exist": [
                  "limit",
                  "offset"
                ]
              },
              "transform": {
                "req": "`reqdata`",
                "res": "`body.publications`"
              }
            }
          ]
        }
      },
      "relations": {
        "ancestors": []
      }
    }
  }
}


const config = new Config()

export {
  config
}

