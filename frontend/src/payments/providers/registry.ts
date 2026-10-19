import { ApiClient } from "../../lib/apiClient";
import { CardProvider } from "./CardProvider";
import type { PaymentProvider } from "./PaymentProvider";
import { WalletProvider } from "./WalletProvider";

export type ProviderKind = "card" | "wallet";

export function providerFor(kind: ProviderKind, client: ApiClient = new ApiClient("/payments")): PaymentProvider {
  return kind === "card" ? new CardProvider(client) : new WalletProvider(client);
}
