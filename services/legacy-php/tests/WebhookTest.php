<?php

declare(strict_types=1);

namespace Acme\Webhook\Tests;

use Acme\Webhook\Handler;
use Acme\Webhook\Signer;
use PHPUnit\Framework\TestCase;

final class WebhookTest extends TestCase
{
    public function testRejectsBadSignature(): void
    {
        $handler = new Handler(new Signer('secret'));
        $result = $handler->process('{"id":"1","type":"order.paid"}', 'bad');
        $this->assertSame(401, $result['status']);
    }

    public function testAcceptsSignedPayload(): void
    {
        $signer = new Signer('secret');
        $payload = '{"id":"2","type":"order.paid"}';
        $result = (new Handler($signer))->process($payload, $signer->sign($payload));
        $this->assertSame(202, $result['status']);
    }
}
