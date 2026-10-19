import assert from "node:assert/strict";
import { test } from "node:test";
import { sleep, withRetry } from "../src/lib/retry.js";

test("withRetry returns the first success", async () => {
  let calls = 0;
  const value = await withRetry(async () => {
    calls += 1;
    if (calls < 2) throw new Error("flaky");
    return "ok";
  }, { baseMs: 1 });
  assert.equal(value, "ok");
  assert.equal(calls, 2);
});

test("sleep waits at least the given time", async () => {
  const started = Date.now();
  await sleep(20);
  assert.ok(Date.now() - started >= 15);
});
