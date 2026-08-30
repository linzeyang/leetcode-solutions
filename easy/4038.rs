// 4038. Count Integers Appearing in a Single Block
// https://leetcode.com/problems/count-integers-appearing-in-a-single-block/
// Weekly Contest 517

use std::collections::HashMap;

impl Solution {
    pub fn count_special_integers(nums: Vec<i32>) -> i32 {
        let mut mapping: HashMap<i32, Vec<usize>> = HashMap::new();

        for (idx, num) in nums.iter().enumerate() {
            if let Some(indices) = mapping.get_mut(num) {
                if !(*num == nums[idx - 1]) {
                    indices.push(idx);
                } else {
                    let length: usize = indices.len();
                    indices[length - 1] = idx;
                }
            } else {
                mapping.insert(*num, vec![idx]);
            }
        }

        mapping.values().filter(|indices| indices.len() == 1).count() as i32
    }
}
