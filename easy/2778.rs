// 2778. Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/
// Weekly Contest 354

impl Solution {
    pub fn sum_of_squares(nums: Vec<i32>) -> i32 {
        let n = nums.len();

        nums.iter()
            .enumerate()
            .filter(|(idx, _)| n % (idx + 1) == 0)
            .map(|(_, num)| num * num)
            .sum()
    }
}
