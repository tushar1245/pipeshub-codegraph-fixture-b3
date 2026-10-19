import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { WishlistItemList } from "../components/WishlistItemList";

describe("WishlistItemList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchWishlist").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", userId: "x", productId: "x" },
    ]);
    render(<WishlistItemList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchWishlist").mockReturnValue(new Promise(() => undefined));
    render(<WishlistItemList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
