import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useShipping } from "../hooks/useShipping";
import { ShipmentCard } from "./ShipmentCard";

export function ShipmentList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useShipping();
  if (loading) {
    return <Spinner label="Loading shipping" />;
  }
  return (
    <Table title="Shipping">
      {items.map((item) => (
        <ShipmentCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
