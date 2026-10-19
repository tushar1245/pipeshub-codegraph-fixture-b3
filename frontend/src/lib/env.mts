export function readEnv(name: string, fallback = ""): string {
  const env = (import.meta as unknown as { env: Record<string, string | undefined> }).env;
  return env[name] ?? fallback;
}
