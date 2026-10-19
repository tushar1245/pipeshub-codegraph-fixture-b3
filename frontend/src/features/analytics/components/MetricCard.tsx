import { formatDate, formatLabel as label } from "../../../lib/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Metric } from "../types";

interface MetricCardProps {
  item: Metric;
  onSelect?: (id: string) => void;
}

export function MetricCard({ item, onSelect }: MetricCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.name)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
    </div>
  );
}
