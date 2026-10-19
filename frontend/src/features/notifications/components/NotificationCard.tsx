import * as fmt from "../../../lib/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Notification } from "../types";

interface NotificationCardProps {
  item: Notification;
  onSelect?: (id: string) => void;
}

export function NotificationCard({ item, onSelect }: NotificationCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.userId)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
