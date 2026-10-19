import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { usePayments } from "../hooks/usePayments";
import { PaymentCard } from "./PaymentCard";

export function PaymentList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = usePayments();
  if (loading) {
    return <Spinner label="Loading payments" />;
  }
  return (
    <Table title="Payments">
      {items.map((item) => (
        <PaymentCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
