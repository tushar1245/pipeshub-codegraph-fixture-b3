import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { ReviewList } from "../components/ReviewList";

describe("ReviewList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchReviews").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", productId: "x", rating: 1 },
    ]);
    render(<ReviewList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchReviews").mockReturnValue(new Promise(() => undefined));
    render(<ReviewList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
