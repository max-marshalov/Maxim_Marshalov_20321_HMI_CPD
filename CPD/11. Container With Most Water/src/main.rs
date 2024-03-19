use std::cmp::{min, max};
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut biggest = 0;
    let mut start = 0;
    let mut end = height.len() - 1;
    while start < end {
        let val = min(height.get(start), height.get(end)).unwrap() * (end - start) as i32;
        biggest = max(biggest, val);
        if height.get(start) < height.get(end){
            start += 1;
        } else {
            end -= 1;
        }

    }
    return biggest;
    }
}     
