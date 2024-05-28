# Исходный код
``` rust

use std::fs;

fn main() {
    let file_path = &String::from("input.txt");

    let contents = fs::read_to_string(file_path).expect("Не удалось прочитать файл");

    
    let mut parts = contents.split_whitespace();
    let N: usize = parts.next().expect("Ожидалось значение N").parse().expect("Ошибка парсинга N");
    let mut numbers: Vec<i64> = Vec::with_capacity(N);
    for _ in 0..N {
        let num: i64 = parts.next().expect("Ожидалось число").parse().expect("Ошибка парсинга числа");
        numbers.push(num);
    }
    let S: i64 = parts.next().expect("Ожидалось значение S").parse().expect("Ошибка парсинга S");

    let mut result = vec![' '; N - 1];


    if find_expression(&numbers, S, 0, 0, &mut result) {
        let mut output = String::new();
        output.push_str(&format!("{}", numbers[0]));
        for i in 1..N {
            output.push(result[i - 1]);
            output.push_str(&format!("{}", numbers[i]));
        }
        output.push_str(&format!(" = {}", S));
       
        fs::write("output.txt", output).expect("Не удалось записать в файл");
    } else {
    
        fs::write("output.txt", "no solution").expect("Не удалось записать в файл");
    }
}
fn find_expression(
    numbers: &[i64],
    S: i64,
    index: usize,
    current_sum: i64,
    result: &mut Vec<char>,
) -> bool {
    if index == numbers.len() - 1 {
        if current_sum + numbers[index] == S {
            if index > 0 {
                result[index - 1] = '+'; 
            }
            true
        } else if current_sum - numbers[index] == S {
            if index > 0 {
                result[index - 1] = '-'; 
            }
            true
        } else {
            false
        }
    } else {
        if find_expression(numbers, S, index + 1, current_sum + numbers[index], result) {
            if index > 0 {
                result[index - 1] = '+';
            }
            return true;
        }

        
        if find_expression(numbers, S, index + 1, current_sum - numbers[index], result) {
            if index > 0 {
                result[index - 1] = '-';
            }
            return true;
        }

        false
    }
}

    
```
# Результат работы
### Входные данные
### <image src="images/input.png" alt="img">
### Выходные данные
### <image src="images/output.png" alt="img">
