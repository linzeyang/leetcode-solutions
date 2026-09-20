// 4057. Number of Intersecting Interval Pairs II
// https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii/
// Weekly Contest 520

impl Solution {
    pub fn count_intersecting_intervals(intervals: Vec<Vec<i32>>) -> i64 {
        let mut intervals: Vec<Vec<i32>> = intervals;
        intervals.sort_unstable();

        let mut out: i64 = 0;

        for (idx, interval) in intervals.iter().enumerate() {
            let target: Vec<i32> = vec![interval[1] + 1, 0];
            let jdx: usize = intervals.partition_point(|x| x <= &target);
            out += jdx as i64 - idx as i64 - 1;
        }

        out
    }
}
