import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { SearchQueryList } from "../components/SearchQueryList";

describe("SearchQueryList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchSearch").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", text: "x", limit: 1 },
    ]);
    render(<SearchQueryList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchSearch").mockReturnValue(new Promise(() => undefined));
    render(<SearchQueryList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
