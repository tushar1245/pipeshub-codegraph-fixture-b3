import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createProduct } from "../api";
import type { Product, ProductInput } from "../types";

const EMPTY: ProductInput = { sku: "", title: "" };

const submit = (input: ProductInput): Promise<Product> => createProduct(input);

export function ProductForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<ProductInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New product" onClose={onClose}>
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
