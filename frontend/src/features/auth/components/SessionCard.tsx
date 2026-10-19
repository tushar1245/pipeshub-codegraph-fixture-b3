import { formatDate, formatLabel as label } from "../../../lib/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Session } from "../types";

interface SessionCardProps {
  item: Session;
  onSelect?: (id: string) => void;
}

export function SessionCard({ item, onSelect }: SessionCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.userId)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
