export type MetricStatus = "draft" | "active" | "archived";

export interface Metric {
  id: string;
  status: MetricStatus;
  createdAt: string;
  name: string;
  value: number;
}

export interface MetricInput {
  name: string;
  value: number;
}
