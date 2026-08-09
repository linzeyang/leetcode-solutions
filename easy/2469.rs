// 2469. Convert the Temperature
// https://leetcode.com/problems/convert-the-temperature/
// Weekly Contest 319

impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let kelvin: f64 = celsius + 273.15;
        let fahrenheit: f64 = celsius * 1.8 + 32.0;
        vec![kelvin, fahrenheit]
    }
}
