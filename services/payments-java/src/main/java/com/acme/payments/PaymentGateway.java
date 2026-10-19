package com.acme.payments;

import java.math.BigDecimal;

public interface PaymentGateway {
    ChargeResult charge(String orderId, BigDecimal amount);

    void refund(String chargeId);
}
