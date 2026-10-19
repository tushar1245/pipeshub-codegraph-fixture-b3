import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import * as api from "../api";
import { MetricList } from "../components/MetricList";

describe("MetricList", () => {
  it("renders one card per item", async () => {
    vi.spyOn(api, "fetchAnalytics").mockResolvedValue([
      { id: "1", status: "active", createdAt: "2024-01-01T00:00:00Z", name: "x", value: 1 },
    ]);
    render(<MetricList />);
    expect(await screen.findByRole("heading")).toBeTruthy();
  });

  it("shows a spinner while loading", () => {
    vi.spyOn(api, "fetchAnalytics").mockReturnValue(new Promise(() => undefined));
    render(<MetricList />);
    expect(screen.getByRole("status")).toBeTruthy();
  });
});
