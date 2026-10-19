import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { PaymentList } from "../components/PaymentList";

describe("PaymentList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchPayments").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", orderId: "x", amount: 1 },
    ]);
    render(<PaymentList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchPayments").mockReturnValue(new Promise(() => undefined));
    render(<PaymentList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
