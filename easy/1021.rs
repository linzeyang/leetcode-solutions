// 1021. Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/
// Weekly Contest 131

impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut out: Vec<char> = Vec::new();
        let mut counter: i32 = 0;

        for letter in s.chars() {
            if letter == '(' {
                if counter > 0 {
                    out.push(letter);
                }
                counter += 1
            } else {
                if counter != 1 {
                    out.push(letter);
                }
                counter -= 1
            }
        }

        out.into_iter().collect::<String>()
    }
}
