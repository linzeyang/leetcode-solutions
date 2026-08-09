// 3110. Score of a String
// https://leetcode.com/problems/score-of-a-string/
// Biweekly Contest 128

impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let mut out: i32 = 0;
        let bytes: &[u8] = s.as_bytes();

        for idx in 1..bytes.len() {
            out += (bytes[idx] as i32 - bytes[idx - 1] as i32).abs();
        }

        out
    }
}
