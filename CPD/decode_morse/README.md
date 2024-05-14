# Исходный код
``` rust
mod preloaded;
use preloaded::MORSE_CODE;
// MORSE_CODE is `HashMap<String, String>`. e.g. ".-" -> "A".

fn decode_morse(encoded: &str) -> String {
    
    let arr: Vec<&str> = encoded.trim().split("   ").collect();
    let mut phrase = String::new();
    for i in arr{
        for j in &mut i.split(" "){
            if j != ""{
                phrase += MORSE_CODE.get(j).unwrap();
            }
        }
        phrase += " "
    }
    return String::from(phrase.trim());
}
```
# Результат работы
<image src="images/out.png" alt="img">