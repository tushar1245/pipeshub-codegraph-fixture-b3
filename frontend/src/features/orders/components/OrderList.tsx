import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useOrders } from "../hooks/useOrders";
import { OrderCard } from "./OrderCard";

export function OrderList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useOrders();
  if (loading) {
    return <Spinner label="Loading orders" />;
  }
  return (
    <Table title="Orders">
      {items.map((item) => (
        <OrderCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
