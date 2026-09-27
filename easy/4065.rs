// 4065. Rearrange Array by Removing Distinct Values
// https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/
// Weekly Contest 521

use std::collections::HashSet;

impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::with_capacity(nums.len());
        let mut nums = nums;

        while !nums.is_empty() {
            let mut distinct: HashSet<i32> = HashSet::new();
            let mut remaining: Vec<i32> = Vec::new();

            for num in nums.drain(..) {
                if !distinct.contains(&num) {
                    distinct.insert(num);
                } else {
                    remaining.push(num);
                }
            }

            let mut sorted_distinct: Vec<i32> = distinct.into_iter().collect();
            sorted_distinct.sort_unstable();
            ans.extend(sorted_distinct);
            nums = remaining;
        }

        ans
    }
}
