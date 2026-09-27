// 4062. Transform Array Using Pair Operations
// https://leetcode.com/problems/transform-array-using-pair-operations/
// Biweely Contest 192

impl Solution {
    pub fn can_transform(source: Vec<i32>, target: Vec<i32>) -> bool {
        source.iter().map(|x| *x as i64).sum::<i64>() == target.iter().map(|x| *x as i64).sum::<i64>()
    }
}
