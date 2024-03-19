fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut j = 1;
        for i in 1..nums.len(){
            if nums[i] != nums[i-1]{
                nums[j] = nums[i];
                j+= 1;
            }
        }
        return j as i32;
}
fn main() {
   let mut nums = vec![0,0,1,1,1,2,2,3,3,4];
   println!("{}", remove_duplicates(&mut nums));
}
