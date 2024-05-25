use std::collections::HashMap; 
        fn min_consecutive_chars(input: &str, target_char: char) -> usize {
            let mut min_count = usize::MAX;
            let mut current_count = 0;
        
            for c in input.chars() {
                if c == target_char {
                    current_count += 1;
                } else {
                    if current_count > 0 && current_count < min_count {
                        min_count = current_count;
                    }
                    current_count = 0;
                }
            }
        
            if current_count > 0 && current_count < min_count {
                min_count = current_count;
            }
        
            min_count
        }
        
        fn decode_bits(bits: &str) -> String {
            let mut morse_code = String::new();
            let trimmed_bits = bits.trim_matches('0');
            let mut current_char = '0';
            let mut count = 0;
            let a = trimmed_bits;
            let min_count_zeros = min_consecutive_chars(trimmed_bits, '0');
            let min_count_ones = min_consecutive_chars(trimmed_bits, '1');
            let min_count = std::cmp::min(min_count_zeros, min_count_ones);
            let b = 1 * min_count;
            let _=a.trim_start_matches('0');
            let _= a.trim_end_matches('0');
            for c in a.chars() {
                if c == current_char {
                    count += 1;
                } else {
                    match current_char {
                        '1' => {
                            if count == 1 * b {
                                morse_code.push('.');
                            } else if count == 3 * b {
                                morse_code.push('-');
                            }
                        }
                        '0' => {
                            if count == 7 * b{
                                morse_code.push_str("   ");
                            } else if count == 3 * b{
                                morse_code.push(' ');
                            } 
                        }
                        _ => {}
                    }
                    current_char = c;
                    count = 1;
                }
            }
        
            match current_char {
                '1' => {
                        if count == 1 * b {
                            morse_code.push('.');
                        } else if count == 3 * b {
                            morse_code.push('-');
                        }
                }
                '0' => {
                        if count == 7 * b{
                            morse_code.push_str("   ");
                        } else if count == 3 * b{
                            morse_code.push(' ');
                        } 
                    }
                _ => {}
            }
            morse_code
            
        }
        fn decode_morse(encoded: &str) -> String {
            let mut morse_code: HashMap<String, String> = HashMap::new();
                morse_code.insert(String::from(".-"), String::from("A"));
                morse_code.insert(String::from("-..."), String::from("B"));
                morse_code.insert(String::from("-.-."), String::from("C"));
                morse_code.insert(String::from("-.."), String::from("D"));
                morse_code.insert(String::from("."), String::from("E"));
                morse_code.insert(String::from("..-."), String::from("F"));
                morse_code.insert(String::from("--."), String::from("G"));
                morse_code.insert(String::from("...."), String::from("H"));
                morse_code.insert(String::from(".."), String::from("I"));
                morse_code.insert(String::from(".---"), String::from("J"));
                morse_code.insert(String::from("-.-"), String::from("K"));
                morse_code.insert(String::from(".-.."), String::from("L"));
                morse_code.insert(String::from("--"), String::from("M"));
                morse_code.insert(String::from("-."), String::from("N"));
                morse_code.insert(String::from("---"), String::from("O"));
                morse_code.insert(String::from(".--."), String::from("P"));
                morse_code.insert(String::from("--.-"), String::from("Q"));
                morse_code.insert(String::from(".-."), String::from("R"));
                morse_code.insert(String::from("..."), String::from("S"));
                morse_code.insert(String::from("-"), String::from("T"));
                morse_code.insert(String::from("..-"), String::from("U"));
                morse_code.insert(String::from("...-"), String::from("V"));
                morse_code.insert(String::from(".--"), String::from("W"));
                morse_code.insert(String::from("-..-"), String::from("X"));
                morse_code.insert(String::from("-.--"), String::from("Y"));
                morse_code.insert(String::from("--.."), String::from("Z"));
                morse_code.insert(String::from("-----"), String::from("0"));
                morse_code.insert(String::from(".----"), String::from("1"));
                morse_code.insert(String::from("..---"), String::from("2"));
                morse_code.insert(String::from("...--"), String::from("3"));
                morse_code.insert(String::from("....-"), String::from("4"));
                morse_code.insert(String::from("....."), String::from("5"));
                morse_code.insert(String::from("-...."), String::from("6"));
                morse_code.insert(String::from("--..."), String::from("7"));
                morse_code.insert(String::from("---.."), String::from("8"));
                morse_code.insert(String::from("----."), String::from("9"));
                morse_code.insert(String::from(".-.-.-"), String::from("."));
                morse_code.insert(String::from("--..--"), String::from(","));
                morse_code.insert(String::from("..--.."), String::from("?"));
                morse_code.insert(String::from(".----."), String::from("'"));
                morse_code.insert(String::from("-.-.--"), String::from("!"));
                morse_code.insert(String::from("-..-."), String::from("/"));
                morse_code.insert(String::from("-.--."), String::from("("));
                morse_code.insert(String::from("-.--.-"), String::from(")"));
                morse_code.insert(String::from(".-..."), String::from("&"));
                morse_code.insert(String::from("---..."), String::from(":"));
                morse_code.insert(String::from("-.-.-."), String::from(";"));
                morse_code.insert(String::from("-...-"), String::from("="));
                morse_code.insert(String::from(".-.-."), String::from("+"));
                morse_code.insert(String::from("-....-"), String::from("-"));
                morse_code.insert(String::from("..--.-"), String::from("_"));
                morse_code.insert(String::from(".-..-."), String::from("\""));
                morse_code.insert(String::from("...-..-"), String::from("$"));
                morse_code.insert(String::from(".--.-."), String::from("@"));
                morse_code.insert(String::from("...---..."), String::from("SOS"));
            let a: Vec<&str> = encoded.trim().split("   ").collect();
            let mut decoded_message = Vec::new(); 
        
            for word in a {
                let morse_letters: Vec<&str> = word.split(' ').collect();
                let decoded_word: String = morse_letters
                    .iter()
                    .map(|&letter| morse_code.get(letter).unwrap_or(&"".to_string()).to_string()) // Использование словаря MORSE_CODE для раскодирования каждой буквы Морзе.
                    .collect();
                decoded_message.push(decoded_word); 
            }
            decoded_message.join(" ")}
        
        fn main() {
            println!("{:?}", decode_morse(&decode_bits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")))
            } 
    
    




