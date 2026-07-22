<?php
declare(strict_types=1);

// Sotaproject SDK exists test

require_once __DIR__ . '/../sotaproject_sdk.php';

use PHPUnit\Framework\TestCase;

class ExistsTest extends TestCase
{
    public function test_create_test_sdk(): void
    {
        $testsdk = SotaprojectSDK::test(null, null);
        $this->assertNotNull($testsdk);
    }
}
