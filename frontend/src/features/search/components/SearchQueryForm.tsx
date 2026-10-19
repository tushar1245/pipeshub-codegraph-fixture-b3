import { useState } from "react";
import { Button } from "../../../components/ui/Button";
import { Modal } from "../../../components/ui/Modal";
import { createSearchQuery } from "../api";
import type { SearchQuery, SearchQueryInput } from "../types";

const EMPTY: SearchQueryInput = { text: "", limit: 0 };

const submit = (input: SearchQueryInput): Promise<SearchQuery> => createSearchQuery(input);

export function SearchQueryForm({ open, onClose }: { open: boolean; onClose: () => void }) {
  const [input, setInput] = useState<SearchQueryInput>(EMPTY);
  const [saving, setSaving] = useState(false);
  return (
    <Modal open={open} title="New search query" onClose={onClose}>
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
          name="text"
          value={String(input.text)}
          onChange={(event) => setInput({ ...input, text: event.target.value })}
        />
        <Button type="submit" disabled={saving}>
          Save
        </Button>
      </form>
    </Modal>
  );
}
