import type { ApiClient } from "../../lib/apiClient";
import type { ChargeResult, RefundingProvider } from "./PaymentProvider";

export class WalletProvider implements RefundingProvider {
  readonly name = "wallet";

  constructor(private readonly client: ApiClient) {}

  async charge(amountCents: number, token: string): Promise<ChargeResult> {
    const result = await this.client.post<ChargeResult>("/wallet/debit", { amountCents, token });
    return { ...result, status: result.status === "ok" ? "ok" : "declined" };
  }

  async refund(chargeId: string): Promise<void> {
    await this.client.post<void>("/wallet/credit", { chargeId });
  }

  async partialRefund(chargeId: string, amountCents: number): Promise<void> {
    await this.client.post<void>("/wallet/credit", { chargeId, amountCents });
  }
}
