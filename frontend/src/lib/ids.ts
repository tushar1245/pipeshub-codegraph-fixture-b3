export function newId(prefix = "id"): string {
  return `${prefix}_${randomPart()}`;
}

function randomPart(): string {
  return Math.random().toString(36).slice(2, 10);
}
