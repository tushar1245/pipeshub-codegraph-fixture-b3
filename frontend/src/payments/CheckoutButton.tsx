import { useState } from "react";
import { Button } from "../components/ui/Button";
import { formatMoney as fm } from "../lib/format";
import { checkout } from "./checkout";
import { providerFor, type ProviderKind } from "./providers/registry";

type Status = "idle" | "paying" | "done" | "declined";

export function CheckoutButton({
  amountCents,
  token,
  kind = "card",
}: {
  amountCents: number;
  token: string;
  kind?: ProviderKind;
}) {
  const [status, setStatus] = useState<Status>("idle");
  return (
    <Button
      disabled={status === "paying"}
      onClick={() => {
        setStatus("paying");
        checkout(providerFor(kind), amountCents, token).then((result) =>
          setStatus(result ? "done" : "declined"),
        );
      }}
    >
      Pay {fm(amountCents / 100)}
    </Button>
  );
}
