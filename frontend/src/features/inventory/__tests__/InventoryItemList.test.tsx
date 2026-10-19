import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { InventoryItemList } from "../components/InventoryItemList";

describe("InventoryItemList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchInventory").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", sku: "x", quantity: 1 },
    ]);
    render(<InventoryItemList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchInventory").mockReturnValue(new Promise(() => undefined));
    render(<InventoryItemList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
