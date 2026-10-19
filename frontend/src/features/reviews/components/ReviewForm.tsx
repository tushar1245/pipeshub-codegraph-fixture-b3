import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createReview } from "../api";
import type { Review, ReviewInput } from "../types";

const EMPTY: ReviewInput = { productId: "", rating: 0 };

const submit = (input: ReviewInput): Promise<Review> => createReview(input);

export function ReviewForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<ReviewInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New review" onClose={onClose}>
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
          name="productId"
          value={String(input.productId)}
          onChange={(event) => setInput({ ...input, productId: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
