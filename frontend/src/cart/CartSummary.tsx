import { formatMoney } from "../lib/text/format";
import type { Cart } from "./Cart";

export function CartSummary({ cart, taxRate = 0.2 }: { cart: Cart; taxRate?: number }) {
  return (
    <dl className="cart-summary">
      <dt>Subtotal</dt>
      <dd>{formatMoney(cart.total())}</dd>
      <dt>Total</dt>
      <dd>{formatMoney(cart.totalWithTax(taxRate))}</dd>
    </dl>
  );
}
