<?php
declare(strict_types=1);

// Sotaproject SDK utility: result_headers

class SotaprojectResultHeaders
{
    public static function call(SotaprojectContext $ctx): ?SotaprojectResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result) {
            if ($response && is_array($response->headers)) {
                $result->headers = $response->headers;
            } else {
                $result->headers = [];
            }
        }
        return $result;
    }
}
