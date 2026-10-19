use pricing::engine::LineItem;
use pricing::rules::Tier;
use pricing::PriceEngine;

#[test]
fn gold_quote_applies_discount_before_tax() {
    let engine = PriceEngine::new(0.2);
    let items = vec![LineItem { sku: "A1".into(), unit_cents: 5_000, quantity: 3 }];
    let quote = engine.quote(&items, Tier::Gold);
    assert_eq!(quote.subtotal_cents, 15_000);
    assert_eq!(quote.discount_cents, 1_500);
    assert_eq!(quote.tax_cents, 2_700);
}
