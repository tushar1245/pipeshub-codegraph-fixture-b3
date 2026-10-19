import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useAuth } from "../hooks/useAuth";
import { SessionCard } from "./SessionCard";

export function SessionList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useAuth();
  if (loading) {
    return <Spinner label="Loading auth" />;
  }
  return (
    <Table title="Auth">
      {items.map((item) => (
        <SessionCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
