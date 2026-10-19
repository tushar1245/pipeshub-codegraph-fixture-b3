export type SearchQueryStatus = "draft" | "active" | "archived";

export interface SearchQuery {
  id: string;
  status: SearchQueryStatus;
  createdAt: string;
  text: string;
  limit: number;
}

export interface SearchQueryInput {
  text: string;
  limit: number;
}
