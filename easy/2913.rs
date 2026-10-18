// 2913. Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
// Biweekly Contest 116

use std::collections::HashSet;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let mut count: i32 = 0;

        for (idx, num) in nums.iter().enumerate() {
            let mut sett: HashSet<i32> = HashSet::new();
            sett.insert(*num);
            count += 1;

            for jdx in idx + 1..nums.len() {
                sett.insert(nums[jdx]);
                count += (sett.len() as i32) * (sett.len() as i32);
            }
        }

        count
    }
}
