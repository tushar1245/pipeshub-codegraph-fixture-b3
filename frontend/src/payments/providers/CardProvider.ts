import type { ApiClient } from "../../lib/apiClient";
import type { ChargeResult, PaymentProvider } from "./PaymentProvider";

export class CardProvider implements PaymentProvider {
  readonly name = "card";

  constructor(private readonly client: ApiClient) {}

  async charge(amountCents: number, token: string): Promise<ChargeResult> {
    return this.client.post<ChargeResult>("/charges", { amountCents, token, method: "card" });
  }

  async refund(chargeId: string): Promise<void> {
    await this.client.post<void>("/refunds", { chargeId });
  }
}
