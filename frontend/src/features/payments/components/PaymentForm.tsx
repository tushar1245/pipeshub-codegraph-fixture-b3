import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createPayment } from "../api";
import type { Payment, PaymentInput } from "../types";

const EMPTY: PaymentInput = { orderId: "", amount: 0 };

const submit = (input: PaymentInput): Promise<Payment> => createPayment(input);

export function PaymentForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<PaymentInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New payment" onClose={onClose}>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          setSaving(true);
          submit(input)
            .then(onClose)
            .finally(() => setSaving(false));
        }}
      >
        <input
          name="orderId"
          value={String(input.orderId)}
          onChange={(event) => setInput({ ...input, orderId: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
