// 2091. Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
// Weekly Contest 269

impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let mut min_idx: usize = 0;
        let mut max_idx: usize = 0;

        for (idx, num) in nums.iter().enumerate() {
            if *num < nums[min_idx] {
                min_idx = idx;
            }
            if *num > nums[max_idx] {
                max_idx = idx;
            }
        }

        let low: i32 = min_idx.min(max_idx) as i32;
        let high: i32 = min_idx.max(max_idx) as i32;

        (high + 1).min(nums.len() as i32 - low).min(nums.len() as i32 - high + low + 1)
    }
}
