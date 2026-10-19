import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useCatalog } from "../hooks/useCatalog";
import { ProductCard } from "./ProductCard";

export function ProductList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useCatalog();
  if (loading) {
    return <Spinner label="Loading catalog" />;
  }
  return (
    <Table title="Catalog">
      {items.map((item) => (
        <ProductCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
