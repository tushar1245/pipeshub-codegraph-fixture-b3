pub trait Rule {
    fn rate(&self, subtotal_cents: i64) -> f64;
    fn name(&self) -> &'static str;
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Tier {
    Standard,
    Silver,
    Gold,
}

pub struct FlatRule {
    pub percent: f64,
}

pub struct ThresholdRule {
    pub threshold_cents: i64,
    pub percent: f64,
}

impl Rule for FlatRule {
    fn rate(&self, _subtotal_cents: i64) -> f64 {
        self.percent / 100.0
    }

    fn name(&self) -> &'static str {
        "flat"
    }
}

impl Rule for ThresholdRule {
    fn rate(&self, subtotal_cents: i64) -> f64 {
        if subtotal_cents >= self.threshold_cents {
            self.percent / 100.0
        } else {
            0.0
        }
    }

    fn name(&self) -> &'static str {
        "threshold"
    }
}

impl Tier {
    pub fn rule(self) -> Box<dyn Rule> {
        match self {
            Tier::Standard => Box::new(FlatRule { percent: 0.0 }),
            Tier::Silver => Box::new(FlatRule { percent: 5.0 }),
            Tier::Gold => Box::new(ThresholdRule { threshold_cents: 10_000, percent: 10.0 }),
        }
    }
}
