import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { CouponList } from "../components/CouponList";

describe("CouponList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchCoupons").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", code: "x", percent: 1 },
    ]);
    render(<CouponList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchCoupons").mockReturnValue(new Promise(() => undefined));
    render(<CouponList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
