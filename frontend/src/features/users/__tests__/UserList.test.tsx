import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { UserList } from "../components/UserList";

describe("UserList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchUsers").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", email: "x", name: "x" },
    ]);
    render(<UserList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchUsers").mockReturnValue(new Promise(() => undefined));
    render(<UserList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
