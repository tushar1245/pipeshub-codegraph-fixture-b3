import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { Metric, MetricInput } from "./types";

const BASE = "/api/analytics";

export function fetchAnalytics(): Promise<Metric[]> {
  return getJson<Metric[]>(BASE);
}

export function fetchMetric(id: string): Promise<Metric> {
  return getJson<Metric>(`${BASE}/${id}`);
}

export function createMetric(input: MetricInput): Promise<Metric> {
  return postJson<Metric>(BASE, input);
}

export function updateMetric(id: string, input: Partial<MetricInput>): Promise<Metric> {
  return putJson<Metric>(`${BASE}/${id}`, input);
}

export function removeMetric(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
