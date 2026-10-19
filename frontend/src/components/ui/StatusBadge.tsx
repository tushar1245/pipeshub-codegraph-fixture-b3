import { formatLabel } from "../../lib/text/format";

export interface StatusBadgeProps {
  status: string;
}

const TONES: Record<string, string> = { draft: "grey", active: "green", archived: "red" };

export function StatusBadge({ status }: StatusBadgeProps) {
  return <span className={`badge badge-${TONES[status] ?? "grey"}`}>{formatLabel(status)}</span>;
}
