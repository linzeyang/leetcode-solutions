// 4014. Minimum Total Price After Applying Discounts
// https://leetcode.com/problems/minimum-total-price-after-applying-discounts/
// Weekly Contest 514

use std::cmp::min;

impl Solution {
    pub fn min_price(prices: Vec<i32>, discounts: Vec<i32>) -> f64 {
        let mut prices: Vec<i32> = prices;
        let mut discounts: Vec<i32> = discounts;

        prices.sort_unstable_by(|a, b| b.cmp(a));
        discounts.sort_unstable_by(|a, b| b.cmp(a));

        let mut out: f64 = 0.0;

        let middle: usize = min(prices.len(), discounts.len());

        for idx in 0..middle {
            out += prices[idx] as f64 * (1.0 - discounts[idx] as f64 / 100.0);
        }

        for jdx in middle..prices.len() {
            out += prices[jdx] as f64;
        }

        out
    }
}
