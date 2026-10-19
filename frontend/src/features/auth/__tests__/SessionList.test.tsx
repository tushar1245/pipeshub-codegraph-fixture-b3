import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { SessionList } from "../components/SessionList";

describe("SessionList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchAuth").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", userId: "x", token: "x" },
    ]);
    render(<SessionList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchAuth").mockReturnValue(new Promise(() => undefined));
    render(<SessionList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
