// 4056. Number of Intersecting Interval Pairs I
// https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/
// Weekly Contest 520

// Rust 1.88.0, using edition 2024.. Your code will be compiled with opt-level 2.
// Supports rand v0.8 and regex v1 and itertools v0.14 from crates.io

impl Solution {
    pub fn count_intersecting_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals;
        intervals.sort_unstable();

        let mut out: i32 = 0;

        for (idx, interval) in intervals.iter().enumerate() {
            let target: Vec<i32> = vec![interval[1] + 1, 0];
            let jdx: usize = intervals.partition_point(|x| x <= &target);
            out += jdx as i32 - idx as i32 - 1;
        }

        out
    }
}
