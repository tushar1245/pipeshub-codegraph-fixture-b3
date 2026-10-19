import { createLogger } from "./lib/logger.js";
import { JobQueue } from "./lib/queue.js";
import { run as syncUsers } from "./jobs/syncUsers.js";
import { run as syncPayments } from "./jobs/syncPayments.js";
import { run as syncInventory } from "./jobs/syncInventory.js";
import { run as syncCatalog } from "./jobs/syncCatalog.js";
import { run as syncShipping } from "./jobs/syncShipping.js";
import { run as syncReviews } from "./jobs/syncReviews.js";
import { run as syncNotifications } from "./jobs/syncNotifications.js";
import { run as syncAuth } from "./jobs/syncAuth.js";
import { run as syncBilling } from "./jobs/syncBilling.js";
import { run as syncAnalytics } from "./jobs/syncAnalytics.js";
import { run as syncSearch } from "./jobs/syncSearch.js";
import { run as syncCoupons } from "./jobs/syncCoupons.js";
import { run as syncReturns } from "./jobs/syncReturns.js";

const log = createLogger("worker");

export async function main() {
  await syncUsers();
  const queue = new JobQueue(log);
  queue.register("users", syncUsers);
  queue.register("payments", syncPayments);
  queue.register("inventory", syncInventory);
  queue.register("catalog", syncCatalog);
  queue.register("shipping", syncShipping);
  queue.register("reviews", syncReviews);
  queue.register("notifications", syncNotifications);
  queue.register("auth", syncAuth);
  queue.register("billing", syncBilling);
  queue.register("analytics", syncAnalytics);
  queue.register("search", syncSearch);
  queue.register("coupons", syncCoupons);
  queue.register("returns", syncReturns);
  const orders = await import("./jobs/syncOrders.js");
  await orders.run();
  queue.register("orders", orders.run);
  return queue.runAll();
}

main().catch((err) => {
  log.error("worker crashed", { err: String(err) });
  process.exit(1);
});
