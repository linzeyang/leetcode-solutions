// 4070. Minimum Rotations to Dial a Number I
// https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/
// Weekly Contest 522

impl Solution {
    pub fn min_rotations(s: String) -> i32 {
        let mut out = 0;
        let mut current = 0;

        for digit in s.chars() {
            let destination: i32 = digit.to_digit(10).unwrap().try_into().unwrap();
            let distance: i32 = (destination - current).abs();

            if distance <= 5 {
                out += distance;
            } else {
                out += 10 - distance;
            }

            current = destination;
        }

        out
    }
}
