<?php
declare(strict_types=1);

// Sotaproject SDK base feature

class SotaprojectBaseFeature
{
    public string $version;
    public string $name;
    public bool $active;

    // Positions this feature when added via the client `extend` option:
    // "__before__" / "__after__" / "__replace__" name an already-added
    // feature (mirrors the ts feature `_options`). Declared so setting it
    // on an extension instance avoids the dynamic-property deprecation.
    public ?array $_options = null;

    public function __construct()
    {
        $this->version = '0.0.1';
        $this->name = 'base';
        $this->active = true;
    }

    public function get_version(): string { return $this->version; }
    public function get_name(): string { return $this->name; }
    public function get_active(): bool { return $this->active; }

    public function init(SotaprojectContext $ctx, array $options): void {}
    public function PostConstruct(SotaprojectContext $ctx): void {}
    public function PostConstructEntity(SotaprojectContext $ctx): void {}
    public function SetData(SotaprojectContext $ctx): void {}
    public function GetData(SotaprojectContext $ctx): void {}
    public function GetMatch(SotaprojectContext $ctx): void {}
    public function SetMatch(SotaprojectContext $ctx): void {}
    public function PrePoint(SotaprojectContext $ctx): void {}
    public function PreSpec(SotaprojectContext $ctx): void {}
    public function PreRequest(SotaprojectContext $ctx): void {}
    public function PreResponse(SotaprojectContext $ctx): void {}
    public function PreResult(SotaprojectContext $ctx): void {}
    public function PreDone(SotaprojectContext $ctx): void {}
    public function PreUnexpected(SotaprojectContext $ctx): void {}
}
