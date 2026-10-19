import { formatDate, formatLabel as label } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { User } from "../types";

interface UserCardProps {
  item: User;
  onSelect?: (id: string) => void;
}

export function UserCard({ item, onSelect }: UserCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.email)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
