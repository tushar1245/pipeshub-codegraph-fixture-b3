import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useReturns } from "../hooks/useReturns";
import { ReturnRequestCard } from "./ReturnRequestCard";

export function ReturnRequestList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useReturns();
  if (loading) {
    return <Spinner label="Loading returns" />;
  }
  return (
    <Table title="Returns">
      {items.map((item) => (
        <ReturnRequestCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
