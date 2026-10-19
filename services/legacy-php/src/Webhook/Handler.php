<?php

declare(strict_types=1);

namespace Acme\Webhook;

final class Handler extends BaseHandler
{
    private array $processed = [];

    protected function handle(array $event): array
    {
        $type = $event['type'] ?? 'unknown';
        if (isset($this->processed[$event['id'] ?? ''])) {
            return ['status' => 200, 'body' => 'duplicate'];
        }
        $this->processed[$event['id'] ?? ''] = $type;
        return ['status' => 202, 'body' => $this->describe($type)];
    }

    private function describe(string $type): string
    {
        return sprintf('accepted %s', $type);
    }

    public static function fromEnv(): self
    {
        return new self(new Signer(getenv('WEBHOOK_SECRET') ?: 'dev-only'));
    }
}
