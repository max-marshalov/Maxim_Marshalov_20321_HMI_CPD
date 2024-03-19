use core::num;
use std::{io, thread::yield_now};

fn fibonachi(n:i32) -> i32{
    if n <= 0 {
        return 0;
    } else if n== 1{
            return 1;
    } else {
        return fibonachi (n-1)  + fibonachi(n-2);
    }
}
fn main() {
    loop {
        println!("Введите ваше число: ");
        let mut number = String::new();
        io::stdin().read_line(&mut number).expect("Fail");
        let number:i32 = match number.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        for i in 1..number{
        println!("Ваша последовательность: {}", fibonachi(i));
        }
        
    }
}
