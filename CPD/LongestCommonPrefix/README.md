# Исходный код
``` rust
use std::{cmp::min, str::FromStr};

fn main() {
    let strs:Vec<String> = vec![String::from_str("flower").unwrap(), String::from_str("flow").unwrap(), String::from_str("fly").unwrap()];
    let mut ph:Vec<String> = strs.clone();
    let mut prefix = String::new();
    ph.sort();
    let mut first = ph.get(0).unwrap();
    let mut last = ph.last().unwrap();
    let mut minimal = min(first.len(), last.len());
    for i in 0..minimal{
        let fir = first.chars().nth(i).unwrap();
        let las = last.chars().nth(i).unwrap();
        if(fir != las){
            println!("{}", prefix);
            break;
        }
        else{
            prefix.push(fir);
        }
    }
    //println!("{}", prefix);
    
}
```
# Результат работы
<image src="images/out.png" alt="img">