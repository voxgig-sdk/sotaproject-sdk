<?php
declare(strict_types=1);

// Sotaproject SDK feature factory

require_once __DIR__ . '/feature/BaseFeature.php';
require_once __DIR__ . '/feature/TestFeature.php';


class SotaprojectFeatures
{
    public static function make_feature(string $name)
    {
        switch ($name) {
            case "base":
                return new SotaprojectBaseFeature();
            case "test":
                return new SotaprojectTestFeature();
            default:
                return new SotaprojectBaseFeature();
        }
    }
}
