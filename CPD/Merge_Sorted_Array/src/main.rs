fn main() {
    let mut nums1 = vec![1,2,3,0,0,0];
    let nums2 = vec![2,5,6];
    let m:i32 = 3;
    let n:i32 = 3;
    for i in 0..n{
        nums1[(m + i) as usize] = nums2[i as usize];

    }
    nums1.sort();
    
}