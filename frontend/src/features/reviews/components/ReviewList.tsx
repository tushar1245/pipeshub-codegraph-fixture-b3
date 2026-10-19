import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useReviews } from "../hooks/useReviews";
import { ReviewCard } from "./ReviewCard";

export function ReviewList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useReviews();
  if (loading) {
    return <Spinner label="Loading reviews" />;
  }
  return (
    <Table title="Reviews">
      {items.map((item) => (
        <ReviewCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
