// 4083. Minimum Deletions to Make Array Sharp
// https://leetcode.com/problems/minimum-deletions-to-make-array-sharp/
// Weekly Contest 524

impl Solution {
    pub fn min_deletions(nums: Vec<i32>) -> i32 {
        let mut out = 0;
        let mut local = 1;

        for idx in 1..nums.len() {
            let num = nums[idx];

            if num == nums[idx - 1] {
                local += 1;
            } else {
                out += local - 1;
                local = 1;
            }
        }

        out += local - 1;

        out
    }
}
