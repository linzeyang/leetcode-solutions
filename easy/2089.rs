// 2089. Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/
// Weekly Contest 269

impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums = nums;
        nums.sort_unstable();

        let mut out: Vec<i32> = Vec::new();

        for (idx, num) in nums.iter().enumerate() {
            if *num == target {
                out.push(idx as i32);
            } else if *num > target {
                break;
            }
        }

        out
    }
}
