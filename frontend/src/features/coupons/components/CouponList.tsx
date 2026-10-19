import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useCoupons } from "../hooks/useCoupons";
import { CouponCard } from "./CouponCard";

export function CouponList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useCoupons();
  if (loading) {
    return <Spinner label="Loading coupons" />;
  }
  return (
    <Table title="Coupons">
      {items.map((item) => (
        <CouponCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
