// 4043. Count Rotations With Exactly K Equal Adjacent Pairs
// https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/
// Weekly Contest 518

impl Solution {
    pub fn count_rotations(s: String, k: i32) -> i32 {
        let bytes: Vec<u8> = s.as_bytes().to_vec();
        let mut equals: Vec<i32> = Vec::new();

        for idx in 0..bytes.len() {
            equals.push((bytes[idx] == bytes[(idx + 1) % bytes.len()]) as i32);
        }

        let mut score: i32 = equals.iter().take(equals.len() - 1).sum();

        let mut out: i32 = (score == k) as i32;

        for idx in 0..equals.len() - 1 {
            score = score - equals[idx] + equals[(equals.len() + idx - 1) % equals.len()];
            out += if score == k { 1 } else { 0 };
        }

        out
    }
}
