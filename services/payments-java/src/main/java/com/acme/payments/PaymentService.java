package com.acme.payments;

import com.acme.build.Builder;
import java.math.BigDecimal;
import java.util.Objects;

public class PaymentService {
    private final PaymentGateway gateway;

    public PaymentService(PaymentGateway gateway) {
        this.gateway = Objects.requireNonNull(gateway);
    }

    public ChargeResult pay(String orderId, BigDecimal amount) {
        validate(orderId, amount);
        return gateway.charge(orderId, amount);
    }

    public void cancel(ChargeResult result) {
        if (result.isApproved()) {
            gateway.refund(result.getChargeId());
        }
    }

    public String describe() {
        return Builder.describe("payments", gateway.getClass().getSimpleName());
    }

    private static void validate(String orderId, BigDecimal amount) {
        if (orderId == null || orderId.isEmpty()) {
            throw new IllegalArgumentException("orderId is required");
        }
        if (amount == null || amount.signum() <= 0) {
            throw new IllegalArgumentException("amount must be positive");
        }
    }
}
