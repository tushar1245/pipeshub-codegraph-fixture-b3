import { createBus } from "../lib/events.js";
import type { ChargeResult, PaymentProvider } from "./providers/PaymentProvider";

const bus = createBus();

export async function checkout(
  provider: PaymentProvider,
  amountCents: number,
  token: string,
): Promise<ChargeResult | null> {
  const result = await provider.charge(amountCents, token);
  if (result.status === "declined") {
    await provider.refund(result.id);
    return null;
  }
  bus.emit("payment.charged", result);
  return result;
}
