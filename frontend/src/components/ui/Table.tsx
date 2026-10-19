import type { ReactNode } from "react";

export interface TableProps {
  title: string;
  children: ReactNode;
  empty?: string;
}

export function Table({ title, children, empty = "Nothing here yet" }: TableProps) {
  const rows = Array.isArray(children) ? children : [children];
  return (
    <section className="table">
      <h2>{title}</h2>
      {rows.length === 0 ? <p>{empty}</p> : rows}
    </section>
  );
}
