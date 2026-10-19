import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createUser } from "../api";
import type { User, UserInput } from "../types";

const EMPTY: UserInput = { email: "", name: "" };

const submit = (input: UserInput): Promise<User> => createUser(input);

export function UserForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<UserInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New user" onClose={onClose}>
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
          name="email"
          value={String(input.email)}
          onChange={(event) => setInput({ ...input, email: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
