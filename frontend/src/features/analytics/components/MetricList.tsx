import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useAnalytics } from "../hooks/useAnalytics";
import { MetricCard } from "./MetricCard";

export function MetricList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useAnalytics();
  if (loading) {
    return <Spinner label="Loading analytics" />;
  }
  return (
    <Table title="Analytics">
      {items.map((item) => (
        <MetricCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
