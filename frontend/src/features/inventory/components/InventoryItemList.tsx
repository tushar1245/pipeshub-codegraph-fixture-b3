import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useInventory } from "../hooks/useInventory";
import { InventoryItemCard } from "./InventoryItemCard";

export function InventoryItemList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useInventory();
  if (loading) {
    return <Spinner label="Loading inventory" />;
  }
  return (
    <Table title="Inventory">
      {items.map((item) => (
        <InventoryItemCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
