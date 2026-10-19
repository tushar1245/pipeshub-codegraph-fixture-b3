use crate::discount::compute_discount;
use crate::rules::Tier;

pub struct LineItem {
    pub sku: String,
    pub unit_cents: i64,
    pub quantity: u32,
}

pub struct PriceEngine {
    tax_rate: f64,
}

impl PriceEngine {
    pub fn new(tax_rate: f64) -> Self {
        PriceEngine { tax_rate }
    }

    pub fn subtotal(&self, items: &[LineItem]) -> i64 {
        items.iter().map(|i| i.unit_cents * i64::from(i.quantity)).sum()
    }

    pub fn quote(&self, items: &[LineItem], tier: Tier) -> Quote {
        let subtotal = self.subtotal(items);
        let discount = compute_discount(subtotal, tier);
        let taxable = subtotal - discount;
        Quote {
            subtotal_cents: subtotal,
            discount_cents: discount,
            tax_cents: self.tax(taxable),
        }
    }

    fn tax(&self, taxable_cents: i64) -> i64 {
        (taxable_cents as f64 * self.tax_rate).round() as i64
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct Quote {
    pub subtotal_cents: i64,
    pub discount_cents: i64,
    pub tax_cents: i64,
}
