import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createMetric } from "../api";
import type { Metric, MetricInput } from "../types";

const EMPTY: MetricInput = { name: "", value: 0 };

const submit = (input: MetricInput): Promise<Metric> => createMetric(input);

export function MetricForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<MetricInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New metric" onClose={onClose}>
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
          name="name"
          value={String(input.name)}
          onChange={(event) => setInput({ ...input, name: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
