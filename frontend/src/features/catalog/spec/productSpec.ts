export interface ProductSpec {
  dimensions: string;
  weightGrams: number;
}

export function parseSpec(raw: string): ProductSpec {
  const [dimensions = "", weight = "0"] = raw.split(";").map((part) => part.trim());
  return { dimensions, weightGrams: Number.parseInt(weight, 10) || 0 };
}

export function describeSpec(spec: ProductSpec): string {
  return `${spec.dimensions} · ${formatWeight(spec.weightGrams)}`;
}

function formatWeight(grams: number): string {
  return grams >= 1000 ? `${(grams / 1000).toFixed(1)} kg` : `${grams} g`;
}
