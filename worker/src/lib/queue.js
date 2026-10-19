import { withRetry } from "./retry.js";

export class JobQueue {
  constructor(log) {
    this.log = log;
    this.jobs = new Map();
  }

  register(name, handler) {
    this.jobs.set(name, handler);
    return this;
  }

  async runAll() {
    const results = {};
    for (const [name, handler] of this.jobs) {
      try {
        results[name] = await withRetry(handler, { attempts: 3 });
      } catch (err) {
        this.log.error("job failed", { name, err: String(err) });
        results[name] = null;
      }
    }
    return results;
  }
}
