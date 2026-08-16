// 4025. Minimize the Maximum Waiting Time at Synchronized Traffic Lights
// https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/
// Weekly Contest 515

impl Solution {
    pub fn min_penalty(period: i32, lights: Vec<i32>, arrival_time: Vec<i32>) -> i32 {
        let max_light: i32 = *lights.iter().max().unwrap();
        let mut out: i32 = 0;

        for &time in &arrival_time {
            let time: i32 = time % period;

            if time >= max_light {
                out = out.max(period - time);
            }
        }

        out
    }
}
