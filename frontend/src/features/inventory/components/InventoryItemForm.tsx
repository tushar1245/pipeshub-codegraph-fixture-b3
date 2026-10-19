import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createInventoryItem } from "../api";
import type { InventoryItem, InventoryItemInput } from "../types";

const EMPTY: InventoryItemInput = { sku: "", quantity: 0 };

const submit = (input: InventoryItemInput): Promise<InventoryItem> => createInventoryItem(input);

export function InventoryItemForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<InventoryItemInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New inventory item" onClose={onClose}>
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
          name="sku"
          value={String(input.sku)}
          onChange={(event) => setInput({ ...input, sku: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
