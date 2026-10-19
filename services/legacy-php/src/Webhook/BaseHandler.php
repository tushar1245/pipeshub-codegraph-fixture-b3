<?php

declare(strict_types=1);

namespace Acme\Webhook;

abstract class BaseHandler
{
    public function __construct(protected Signer $signer)
    {
    }

    public function process(string $payload, string $signature): array
    {
        if (!$this->signer->verify($payload, $signature)) {
            return ['status' => 401, 'body' => 'invalid signature'];
        }
        $event = json_decode($payload, true, 512, JSON_THROW_ON_ERROR);
        return $this->handle($event);
    }

    abstract protected function handle(array $event): array;
}
