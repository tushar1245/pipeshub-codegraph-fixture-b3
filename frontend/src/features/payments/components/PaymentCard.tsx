import { formatDate, formatLabel as label, formatMoney as fm } from "../../../lib/text/format";
import { StatusBadge } from "../../../components/ui/StatusBadge";
import type { Payment } from "../types";

interface PaymentCardProps {
  item: Payment;
  onSelect?: (id: string) => void;
}

export function PaymentCard({ item, onSelect }: PaymentCardProps) {
  return (
    <div className="card" onClick={() => onSelect?.(item.id)}>
      <h3>{label(item.orderId)}</h3>
      <StatusBadge status={item.status} />
      <time>{formatDate(item.createdAt)}</time>
      <span className="amount">{fm(item.amount)}</span>
    </div>
  );
}
