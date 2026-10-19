export interface ChargeResult {
  id: string;
  status: "ok" | "declined";
}

export interface PaymentProvider {
  readonly name: string;
  charge(amountCents: number, token: string): Promise<ChargeResult>;
  refund(chargeId: string): Promise<void>;
}

export interface RefundingProvider extends PaymentProvider {
  partialRefund(chargeId: string, amountCents: number): Promise<void>;
}
