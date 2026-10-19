import { useState } from "react";
import { CartSummary } from "../cart/CartSummary";
import { Cart } from "../cart/Cart";
import { Layout } from "../components/ui/Layout";
import { OrderForm } from "../features/orders";
import { CheckoutButton } from "../payments/CheckoutButton";
import { buildRoutes } from "./routes";

export default function App() {
  const routes = buildRoutes();
  const [active, setActive] = useState(routes[0].path);
  const [creating, setCreating] = useState(false);
  const [cart] = useState(() => new Cart());
  const current = routes.find((route) => route.path === active) ?? routes[0];
  const Page = current.component;
  return (
    <Layout
      title={current.title}
      nav={routes.map((route) => ({ label: route.title, href: route.path }))}
      onNavigate={setActive}
    >
      <Page />
      <CartSummary cart={cart} />
      <CheckoutButton amountCents={1999} token="tok_demo" />
      <button type="button" onClick={() => setCreating(true)}>
        New order
      </button>
      <OrderForm open={creating} onClose={() => setCreating(false)} />
    </Layout>
  );
}
