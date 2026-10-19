import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createCoupon } from "../api";
import type { Coupon, CouponInput } from "../types";

const EMPTY: CouponInput = { code: "", percent: 0 };

const submit = (input: CouponInput): Promise<Coupon> => createCoupon(input);

export function CouponForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<CouponInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New coupon" onClose={onClose}>
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
          name="code"
          value={String(input.code)}
          onChange={(event) => setInput({ ...input, code: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
