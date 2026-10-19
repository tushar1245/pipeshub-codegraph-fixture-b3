import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createOrder } from "../api";
import type { Order, OrderInput } from "../types";

const EMPTY: OrderInput = { customerId: "", total: 0 };

const submit = (input: OrderInput): Promise<Order> => createOrder(input);

export function OrderForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<OrderInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New order" onClose={onClose}>
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
          name="customerId"
          value={String(input.customerId)}
          onChange={(event) => setInput({ ...input, customerId: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
