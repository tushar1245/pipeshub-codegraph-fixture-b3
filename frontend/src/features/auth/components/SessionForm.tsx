import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createSession } from "../api";
import type { Session, SessionInput } from "../types";

const EMPTY: SessionInput = { userId: "", token: "" };

const submit = (input: SessionInput): Promise<Session> => createSession(input);

export function SessionForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<SessionInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New session" onClose={onClose}>
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
