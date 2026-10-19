package com.acme.payments;

public final class ChargeResult {
    private final String chargeId;
    private final boolean approved;

    public ChargeResult(String chargeId, boolean approved) {
        this.chargeId = chargeId;
        this.approved = approved;
    }

    public String getChargeId() {
        return chargeId;
    }

    public boolean isApproved() {
        return approved;
    }
}
