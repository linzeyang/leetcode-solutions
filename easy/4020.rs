// 4020. Elevator Requests I
// https://leetcode.com/problems/elevator-requests-i/
// Biweekly Contest 189

impl Solution {
    pub fn elevator_requests(n: i32, requests: Vec<i32>) -> i32 {
        let mut out: i32 = requests[0];

        for idx in 1..requests.len() {
            out += (requests[idx] - requests[idx - 1]).abs();
        }

        out
    }
}
