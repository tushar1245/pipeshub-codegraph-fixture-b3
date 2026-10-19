import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { ShipmentList } from "../components/ShipmentList";

describe("ShipmentList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchShipping").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", orderId: "x", carrier: "x" },
    ]);
    render(<ShipmentList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchShipping").mockReturnValue(new Promise(() => undefined));
    render(<ShipmentList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
