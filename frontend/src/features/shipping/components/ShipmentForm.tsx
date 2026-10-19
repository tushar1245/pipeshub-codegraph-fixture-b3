import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createShipment } from "../api";
import type { Shipment, ShipmentInput } from "../types";

const EMPTY: ShipmentInput = { orderId: "", carrier: "" };

const submit = (input: ShipmentInput): Promise<Shipment> => createShipment(input);

export function ShipmentForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<ShipmentInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New shipment" onClose={onClose}>
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
