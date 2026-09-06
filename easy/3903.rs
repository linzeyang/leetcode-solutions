// 3903. Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/
// Weekly Contest 498

impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let mut forward_max: Vec<i32> = Vec::new();
        let mut backward_min: Vec<i32> = Vec::new();

        for num in &nums {
            if forward_max.is_empty() {
                forward_max.push(*num);
            } else {
                forward_max.push(*num.max(forward_max.last().unwrap()));
            }
        }

        for num in nums.iter().rev() {
            if backward_min.is_empty() {
                backward_min.push(*num);
            } else {
                backward_min.push(*num.min(backward_min.last().unwrap()));
            }
        }

        for idx in 0..nums.len() {
            if forward_max[idx] - backward_min[backward_min.len() - idx - 1] <= k {
                return idx as i32;
            }
        }

        -1
    }
}
