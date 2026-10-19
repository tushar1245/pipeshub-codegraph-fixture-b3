import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createInvoice } from "../api";
import type { Invoice, InvoiceInput } from "../types";

const EMPTY: InvoiceInput = { customerId: "", amount: 0 };

const submit = (input: InvoiceInput): Promise<Invoice> => createInvoice(input);

export function InvoiceForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<InvoiceInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New invoice" onClose={onClose}>
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
