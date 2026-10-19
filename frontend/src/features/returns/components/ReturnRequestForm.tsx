import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createReturnRequest } from "../api";
import type { ReturnRequest, ReturnRequestInput } from "../types";

const EMPTY: ReturnRequestInput = { orderId: "", reason: "" };

const submit = (input: ReturnRequestInput): Promise<ReturnRequest> => createReturnRequest(input);

export function ReturnRequestForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<ReturnRequestInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New return request" onClose={onClose}>
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
