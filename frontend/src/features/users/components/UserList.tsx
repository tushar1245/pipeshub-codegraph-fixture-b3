import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useUsers } from "../hooks/useUsers";
import { UserCard } from "./UserCard";

export function UserList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useUsers();
  if (loading) {
    return <Spinner label="Loading users" />;
  }
  return (
    <Table title="Users">
      {items.map((item) => (
        <UserCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
