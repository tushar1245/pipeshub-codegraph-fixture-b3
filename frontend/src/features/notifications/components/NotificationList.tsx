import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useNotifications } from "../hooks/useNotifications";
import { NotificationCard } from "./NotificationCard";

export function NotificationList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useNotifications();
  if (loading) {
    return <Spinner label="Loading notifications" />;
  }
  return (
    <Table title="Notifications">
      {items.map((item) => (
        <NotificationCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
