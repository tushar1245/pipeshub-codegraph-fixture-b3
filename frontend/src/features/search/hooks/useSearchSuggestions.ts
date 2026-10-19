import { debounce } from "lodash";
import { useMemo } from "react";
import { fetchSearch } from "../api";
import type { SearchQuery } from "../types";

export function useSearchSuggestions(onResults: (items: SearchQuery[]) => void) {
  return useMemo(
    () =>
      debounce((text: string) => {
        if (text.trim().length > 1) {
          fetchSearch().then(onResults);
        }
      }, 250),
    [onResults],
  );
}
