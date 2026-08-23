<?php
declare(strict_types=1);

// Sotaproject SDK configuration

class SotaprojectConfig
{
    /** @var array<string,mixed>|null */
    private static ?array $shared_config = null;

    /**
     * Return the process-wide config, built once on first use. The SDK reads
     * the config on every request and never writes to it, so one instance is
     * shared by every client rather than rebuilt per client.
     *
     * PHP arrays are copy-on-write, so callers that do mutate the result get
     * their own copy and cannot disturb the shared one.
     */
    public static function shared_config(): array
    {
        if (self::$shared_config === null) {
            self::$shared_config = self::make_config();
        }
        return self::$shared_config;
    }

    /**
     * Build a fresh, fully materialised config array. Every call rebuilds the
     * whole structure, so prefer shared_config unless you need a private copy.
     */
    public static function make_config(): array
    {
        return [
            "main" => [
                "name" => "Sotaproject",
                "slug" => "sotaproject",
                "version" => "0.0.1",
                "target" => "php",
            ],
            "feature" => [
                "test" => [
          'options' => [
            'active' => false,
          ],
        ],
            ],
            "options" => [
                "base" => "https://sotaproject.com/api/v1",
                "headers" => [
          'content-type' => 'application/json',
        ],
                "entity" => [
                    "publication" => [],
                ],
            ],
            "entity" => [
        'publication' => [
          'fields' => [
            [
              'name' => 'author',
              'short' => 'Author of the publication',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'category',
              'short' => 'Category of the publication (e.g., investigation, news)',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'content',
              'short' => 'Content body of the publication',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'id',
              'short' => 'Unique identifier for the publication',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'media',
              'short' => 'Media content associated with the publication',
              'type' => '`$ARRAY`',
            ],
            [
              'name' => 'published_at',
              'short' => 'Publication date and time',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'title',
              'short' => 'Title of the publication',
              'type' => '`$STRING`',
            ],
            [
              'name' => 'url',
              'short' => 'URL to the full publication',
              'type' => '`$STRING`',
            ],
          ],
          'name' => 'publication',
          'op' => [
            'list' => [
              'input' => 'data',
              'name' => 'list',
              'points' => [
                [
                  'args' => [
                    'query' => [
                      [
                        'example' => 50,
                        'kind' => 'query',
                        'name' => 'limit',
                        'orig' => 'limit',
                        'type' => '`$INTEGER`',
                      ],
                      [
                        'example' => 0,
                        'kind' => 'query',
                        'name' => 'offset',
                        'orig' => 'offset',
                        'type' => '`$INTEGER`',
                      ],
                    ],
                  ],
                  'kind' => 'http',
                  'method' => 'GET',
                  'orig' => '/tg-news',
                  'parts' => [
                    'tg-news',
                  ],
                  'select' => [
                    'exist' => [
                      'limit',
                      'offset',
                    ],
                  ],
                  'transform' => [
                    'req' => '`reqdata`',
                    'res' => '`body.publications`',
                  ],
                ],
              ],
            ],
          ],
          'relations' => [
            'ancestors' => [],
          ],
        ],
      ],
        ];
    }


    public static function make_feature(string $name)
    {
        require_once __DIR__ . '/features.php';
        return SotaprojectFeatures::make_feature($name);
    }
}
