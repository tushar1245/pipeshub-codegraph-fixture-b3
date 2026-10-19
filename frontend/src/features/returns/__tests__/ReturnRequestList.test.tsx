import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { ReturnRequestList } from "../components/ReturnRequestList";

describe("ReturnRequestList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchReturns").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", orderId: "x", reason: "x" },
    ]);
    render(<ReturnRequestList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchReturns").mockReturnValue(new Promise(() => undefined));
    render(<ReturnRequestList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
