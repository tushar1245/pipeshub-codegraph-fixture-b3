const http = require("node:http");
const { chunk, sleep } = require("./util.cjs");

function post(batch) {
  return new Promise((resolve, reject) => {
    const req = http.request(
      { host: process.env.API_HOST || "localhost", port: 8000, path: "/internal/reindex", method: "POST" },
      (res) => (res.statusCode < 300 ? resolve() : reject(new Error(`reindex failed: ${res.statusCode}`))),
    );
    req.on("error", reject);
    req.end(JSON.stringify({ ids: batch }));
  });
}

async function reindexAll(ids) {
  for (const batch of chunk(ids, 50)) {
    await post(batch);
    await sleep(100);
  }
  return ids.length;
}

module.exports = { reindexAll };
