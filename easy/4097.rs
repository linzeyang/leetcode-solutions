// 4097. Minimum Value of Merged Integers
// https://leetcode.com/problems/minimum-value-of-merged-integers/
// Weekly Contest 526

impl Solution {
    pub fn min_merged_integer(nums: Vec<i32>) -> i32 {
        nums.chunks(2)
            .map(|pair| format!("{}{}", pair[0], pair[1]).parse::<i32>().unwrap())
            .min()
            .unwrap()
    }
}
