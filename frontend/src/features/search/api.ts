import { deleteJson, getJson, postJson, putJson } from "../../lib/http";
import type { SearchQuery, SearchQueryInput } from "./types";

const BASE = "/api/search";

export function fetchSearch(): Promise<SearchQuery[]> {
  return getJson<SearchQuery[]>(BASE);
}

export function fetchSearchQuery(id: string): Promise<SearchQuery> {
  return getJson<SearchQuery>(`${BASE}/${id}`);
}

export function createSearchQuery(input: SearchQueryInput): Promise<SearchQuery> {
  return postJson<SearchQuery>(BASE, input);
}

export function updateSearchQuery(id: string, input: Partial<SearchQueryInput>): Promise<SearchQuery> {
  return putJson<SearchQuery>(`${BASE}/${id}`, input);
}

export function removeSearchQuery(id: string): Promise<void> {
  return deleteJson(`${BASE}/${id}`);
}
