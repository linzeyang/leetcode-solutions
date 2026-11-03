// 3963. Create Grid With Exactly One Path
// https://leetcode.com/problems/create-grid-with-exactly-one-path/
// Biweekly Contest 185

impl Solution {
    pub fn create_grid(m: i32, n: i32) -> Vec<String> {
        let (m, n) = (m as usize, n as usize);
        let mut grid = vec![".".repeat(n)];

        grid.extend(vec!["#".repeat(n - 1) + "."; m - 1]);

        grid
    }
}
