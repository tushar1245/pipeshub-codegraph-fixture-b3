<?php

declare(strict_types=1);

namespace Acme\Webhook;

final class Signer
{
    public function __construct(private string $secret)
    {
    }

    public function sign(string $payload): string
    {
        return hash_hmac('sha256', $payload, $this->secret);
    }

    public function verify(string $payload, string $signature): bool
    {
        return hash_equals($this->sign($payload), $signature);
    }
}
