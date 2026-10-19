import { ApiClient } from "../lib/client.js";
import { createLogger } from "../lib/logger.js";
import { withRetry } from "../lib/retry.js";

const log = createLogger("sync-notifications");

export async function run(client = new ApiClient(process.env.API_URL)) {
  const items = await withRetry(() => client.get("/api/notifications?updated_since=" + since()), { attempts: 5 });
  log.info("synced", { count: items.length });
  return items.length;
}

function since() {
  return new Date(Date.now() - 15 * 60 * 1000).toISOString();
}
