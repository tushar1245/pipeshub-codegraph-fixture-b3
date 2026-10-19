import { expect, test, type Page } from "@playwright/test";

async function fillCard(page: Page, number: string): Promise<void> {
  await page.getByLabel("Card number").fill(number);
  await page.getByLabel("Expiry").fill("12/30");
  await page.getByLabel("CVC").fill("123");
}

test("a shopper can pay for their cart", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: /pay/i }).click();
  await fillCard(page, "4242424242424242");
  await expect(page.getByText("Payment complete")).toBeVisible();
});

test("a declined card shows an error", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: /pay/i }).click();
  await fillCard(page, "4000000000000002");
  await expect(page.getByText("declined", { exact: false })).toBeVisible();
});
