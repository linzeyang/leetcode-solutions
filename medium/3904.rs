// 3904. Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/
// Weekly Contest 498

impl Solution {
    pub fn first_stable_index(nums: Vec<i32>, k: i32) -> i32 {
        let mut backward_min: Vec<i32> = Vec::new();

        for num in nums.iter().rev() {
            if backward_min.is_empty() {
                backward_min.push(*num);
            } else {
                backward_min.push(*num.min(backward_min.last().unwrap()));
            }
        }

        let mut current_max: i32 = 0;

        for (idx, num) in nums.iter().enumerate() {
            current_max = current_max.max(*num);

            if current_max - backward_min[backward_min.len() - idx - 1] <= k {
                return idx as i32;
            }
        }

        -1
    }
}
