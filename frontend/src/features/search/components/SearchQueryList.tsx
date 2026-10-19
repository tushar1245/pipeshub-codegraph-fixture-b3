import { Spinner } from "../../../components/ui/Spinner";
import { Table } from "../../../components/ui/Table";
import { useSearch } from "../hooks/useSearch";
import { SearchQueryCard } from "./SearchQueryCard";

export function SearchQueryList({ onSelect }: { onSelect?: (id: string) => void }) {
  const { items, loading } = useSearch();
  if (loading) {
    return <Spinner label="Loading search" />;
  }
  return (
    <Table title="Search">
      {items.map((item) => (
        <SearchQueryCard key={item.id} item={item} onSelect={onSelect} />
      ))}
    </Table>
  );
}
