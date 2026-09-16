// 3483. Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/
// Biweekly Contest 152

use std::collections::HashSet;

impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        let mut candidates: HashSet<i32> = HashSet::new();
        let n: usize = digits.len();

        for i in 0..n {
            if digits[i] == 0 {
                continue;
            }

            for j in 0..n {
                if j == i {
                    continue;
                }

                for k in 0..n {
                    if k == i || k == j || digits[k] & 1 == 1 {
                        continue;
                    }

                    candidates.insert(digits[i] * 100 + digits[j] * 10 + digits[k]);
                }
            }
        }

        candidates.len() as i32
    }
}
