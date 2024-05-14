# Исходный код
``` rust
use core::num;
use std::io;

fn main() {
    loop{
    println!("Введите число для конверации");
    let mut number = String::new();
    io::stdin().read_line(&mut number).expect("Fail");
    
    let mut number:f32 = match number.trim().parse(){
        Ok(num) => num,
        Err(_) => continue, 
    };
    let mut ph = number *9.0/5.0  + 32.0;
    println!("В Фаренгейтах: {}", ph)
    
}
}
```
# Результат работы
<image src="images/out.png" alt="img">