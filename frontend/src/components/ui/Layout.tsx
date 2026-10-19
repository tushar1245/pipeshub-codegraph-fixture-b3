import type { ReactNode } from "react";
import { formatLabel } from "../../lib/format";
import { useWindowWidth } from "../../app/useWindowWidth";

export interface NavItem {
  label: string;
  href: string;
}

export interface LayoutProps {
  title: string;
  nav: NavItem[];
  onNavigate: (href: string) => void;
  children: ReactNode;
}

export function Layout({ title, nav, onNavigate, children }: LayoutProps) {
  const width = useWindowWidth();
  return (
    <div className={width < 768 ? "layout compact" : "layout"}>
      <nav>
        {nav.map((item) => (
          <a
            key={item.href}
            href={item.href}
            onClick={(event) => {
              event.preventDefault();
              onNavigate(item.href);
            }}
          >
            {formatLabel(item.label)}
          </a>
        ))}
      </nav>
      <main>
        <h1>{title}</h1>
        {children}
      </main>
    </div>
  );
}
