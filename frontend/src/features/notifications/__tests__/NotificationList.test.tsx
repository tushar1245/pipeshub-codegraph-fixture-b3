import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { NotificationList } from "../components/NotificationList";

describe("NotificationList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchNotifications").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", userId: "x", channel: "x" },
    ]);
    render(<NotificationList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchNotifications").mockReturnValue(new Promise(() => undefined));
    render(<NotificationList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
