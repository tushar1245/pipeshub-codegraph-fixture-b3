import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useBilling } from "../hooks/useBilling";
import { InvoiceCard } from "./InvoiceCard";

export function InvoiceList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useBilling();
  if (loading) {
    return <Spinner label="Loading billing" />;
  }
  return (
    <Table title="Billing">
      {items.map((item) => (
        <InvoiceCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
