// 3701. Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/
// Weekly Contest 470

impl Solution {
    pub fn alternating_sum(nums: Vec<i32>) -> i32 {
        let mut out: i32 = 0;

        for idx in 0..nums.len() {
            if idx & 1 == 0 {
                out += nums[idx];
            } else {
                out -= nums[idx];
            }
        }

        out
    }
}
