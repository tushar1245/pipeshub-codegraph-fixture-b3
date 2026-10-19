package com.acme.payments;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.math.BigDecimal;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PaymentServiceTest {
    private PaymentService service;

    @BeforeEach
    void setUp() {
        service = new PaymentService(new StripeGateway("test-key"));
    }

    @Test
    void approvesPositiveAmounts() {
        ChargeResult result = service.pay("order-1", new BigDecimal("12.50"));
        assertTrue(result.isApproved());
    }

    @Test
    void rejectsMissingOrderId() {
        assertThrows(IllegalArgumentException.class, () -> service.pay("", BigDecimal.ONE));
    }

    @Test
    void cancelSkipsDeclinedCharges() {
        ChargeResult declined = new ChargeResult(null, false);
        service.cancel(declined);
        assertFalse(declined.isApproved());
    }
}
