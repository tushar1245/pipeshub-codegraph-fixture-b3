use crate::rules::{Rule, Tier};

pub fn compute_discount(subtotal_cents: i64, tier: Tier) -> i64 {
    let rule: Box<dyn Rule> = tier.rule();
    let rate = rule.rate(subtotal_cents);
    round_cents(subtotal_cents as f64 * rate)
}

fn round_cents(value: f64) -> i64 {
    value.round() as i64
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn gold_tier_gets_ten_percent_over_threshold() {
        assert_eq!(compute_discount(20_000, Tier::Gold), 2_000);
    }
}
