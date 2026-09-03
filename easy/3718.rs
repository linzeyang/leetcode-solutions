// 3718. Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/
// Weekly Contest 472

use std::collections::HashSet;

impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let nums_set: HashSet<i32> = nums.clone().into_iter().collect();

        for factor in 1..=nums.len() {
            if !nums_set.contains(&(k * factor as i32)) {
                return k * factor as i32;
            }
        }

        k * (nums.len() as i32 + 1)
    }
}
