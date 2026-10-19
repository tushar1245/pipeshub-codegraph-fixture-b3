import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createNotification } from "../api";
import type { Notification, NotificationInput } from "../types";

const EMPTY: NotificationInput = { userId: "", channel: "" };

const submit = (input: NotificationInput): Promise<Notification> => createNotification(input);

export function NotificationForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<NotificationInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New notification" onClose={onClose}>
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
