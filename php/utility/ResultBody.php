<?php
declare(strict_types=1);

// Sotaproject SDK utility: result_body

class SotaprojectResultBody
{
    public static function call(SotaprojectContext $ctx): ?SotaprojectResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result && $response && $response->json_func && $response->body) {
            $result->body = ($response->json_func)();
        }
        return $result;
    }
}
