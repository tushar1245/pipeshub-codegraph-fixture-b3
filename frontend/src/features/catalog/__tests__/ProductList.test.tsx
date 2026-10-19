import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { ProductList } from "../components/ProductList";

describe("ProductList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchCatalog").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", sku: "x", title: "x" },
    ]);
    render(<ProductList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchCatalog").mockReturnValue(new Promise(() => undefined));
    render(<ProductList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
