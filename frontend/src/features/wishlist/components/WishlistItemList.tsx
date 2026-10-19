import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useWishlist } from "../hooks/useWishlist";
import { WishlistItemCard } from "./WishlistItemCard";

export function WishlistItemList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useWishlist();
  if (loading) {
    return <Spinner label="Loading wishlist" />;
  }
  return (
    <Table title="Wishlist">
      {items.map((item) => (
        <WishlistItemCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
