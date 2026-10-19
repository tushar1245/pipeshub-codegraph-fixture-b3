export interface LegacyFlags {
  newCheckout: boolean;
  compactTables: boolean;
}

export function legacyFlags(): LegacyFlags {
  return { newCheckout: true, compactTables: false };
}
