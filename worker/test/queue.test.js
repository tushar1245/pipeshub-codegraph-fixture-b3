import assert from "node:assert/strict";
import { test } from "node:test";
import { JobQueue } from "../src/lib/queue.js";

const silent = { info() {}, error() {} };

test("runAll records a failed job as null", async () => {
  const queue = new JobQueue(silent);
  queue.register("ok", async () => 3);
  queue.register("broken", async () => {
    throw new Error("nope");
  });
  assert.deepEqual(await queue.runAll(), { ok: 3, broken: null });
});
