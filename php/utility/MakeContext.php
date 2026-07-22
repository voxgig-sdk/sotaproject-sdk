<?php
declare(strict_types=1);

// Sotaproject SDK utility: make_context

require_once __DIR__ . '/../core/Context.php';

class SotaprojectMakeContext
{
    public static function call(array $ctxmap, ?SotaprojectContext $basectx): SotaprojectContext
    {
        return new SotaprojectContext($ctxmap, $basectx);
    }
}
