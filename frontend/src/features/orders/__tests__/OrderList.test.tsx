import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { OrderList } from "../components/OrderList";

describe("OrderList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchOrders").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", customerId: "x", total: 1 },
    ]);
    render(<OrderList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchOrders").mockReturnValue(new Promise(() => undefined));
    render(<OrderList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
