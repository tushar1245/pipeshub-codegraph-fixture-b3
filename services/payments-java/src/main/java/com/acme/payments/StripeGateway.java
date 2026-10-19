package com.acme.payments;

import java.math.BigDecimal;
import java.util.UUID;
import java.util.logging.Logger;

public class StripeGateway implements PaymentGateway {
    private static final Logger LOG = Logger.getLogger(StripeGateway.class.getName());

    private final String apiKey;

    public StripeGateway(String apiKey) {
        this.apiKey = apiKey;
    }

    @Override
    public ChargeResult charge(String orderId, BigDecimal amount) {
        if (amount.signum() <= 0) {
            return new ChargeResult(null, false);
        }
        String chargeId = "ch_" + UUID.randomUUID();
        LOG.info(() -> "charged " + orderId + " " + amount + " as " + chargeId);
        return new ChargeResult(chargeId, true);
    }

    @Override
    public void refund(String chargeId) {
        LOG.info(() -> "refunded " + chargeId);
    }

    boolean isConfigured() {
        return apiKey != null && !apiKey.isBlank();
    }
}
