import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createWishlistItem } from "../api";
import type { WishlistItem, WishlistItemInput } from "../types";

const EMPTY: WishlistItemInput = { userId: "", productId: "" };

const submit = (input: WishlistItemInput): Promise<WishlistItem> => createWishlistItem(input);

export function WishlistItemForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<WishlistItemInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New wishlist item" onClose={onClose}>
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
          name="userId"
          value={String(input.userId)}
          onChange={(event) => setInput({ ...input, userId: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
