// 4034. Minimum Bishop Moves to Reach Target
// https://leetcode.com/problems/minimum-bishop-moves-to-reach-target/
// Biweekly Contest 190

impl Solution {
    pub fn min_bishop_moves(source: Vec<i32>, target: Vec<i32>) -> i32 {
        let s1: i32 = source[0];
        let s2: i32 = source[1];
        let t1: i32 = target[0];
        let t2: i32 = target[1];

        if (s1 + s2) & 1 != (t1 + t2) & 1 {
            return -1;
        }

        ((t1 - s1).abs() != (t2 - s2).abs()) as i32 + 1
    }
}
