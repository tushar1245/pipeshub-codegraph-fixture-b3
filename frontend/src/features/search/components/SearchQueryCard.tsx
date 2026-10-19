import * as fmt from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { SearchQuery } from "../types";

interface SearchQueryCardProps {
  item: SearchQuery;
  onSelect?: (id: string) => void;
}

export function SearchQueryCard({ item, onSelect }: SearchQueryCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{fmt.formatLabel(item.text)}</h3>
      <StatusBadge status={item.status} />
      <time>{fmt.formatDate(item.createdAt)}</time>
    </div>
  );
}
