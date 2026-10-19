import type { ComponentType } from "react";
import { UserList, OrderList, PaymentList, InventoryItemList, ProductList, ShipmentList, ReviewList, NotificationList, SessionList, InvoiceList, MetricList, SearchQueryList, CouponList, ReturnRequestList } from "../features";
import { legacyFlags } from "../lib/legacyConfig.cjs";

export interface RouteDef {
  path: string;
  title: string;
  component: ComponentType;
}

export function buildRoutes(): RouteDef[] {
  const flags = legacyFlags();
  const routes: RouteDef[] = [
    { path: "/users", title: "Users", component: UserList },
    { path: "/orders", title: "Orders", component: OrderList },
    { path: "/payments", title: "Payments", component: PaymentList },
    { path: "/inventory", title: "Inventory", component: InventoryItemList },
    { path: "/catalog", title: "Catalog", component: ProductList },
    { path: "/shipping", title: "Shipping", component: ShipmentList },
    { path: "/reviews", title: "Reviews", component: ReviewList },
    { path: "/notifications", title: "Notifications", component: NotificationList },
    { path: "/auth", title: "Auth", component: SessionList },
    { path: "/billing", title: "Billing", component: InvoiceList },
    { path: "/analytics", title: "Analytics", component: MetricList },
    { path: "/search", title: "Search", component: SearchQueryList },
    { path: "/coupons", title: "Coupons", component: CouponList },
    { path: "/returns", title: "Returns", component: ReturnRequestList },
  ];
  return flags.compactTables ? routes.slice(0, 8) : routes;
}
