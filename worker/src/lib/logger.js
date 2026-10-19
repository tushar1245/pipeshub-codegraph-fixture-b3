export function createLogger(scope) {
  return {
    info: (message, meta) => write("info", scope, message, meta),
    error: (message, meta) => write("error", scope, message, meta),
  };
}

function write(level, scope, message, meta = {}) {
  const line = JSON.stringify({ ts: new Date().toISOString(), level, scope, message, ...meta });
  process.stdout.write(line + "\n");
}
