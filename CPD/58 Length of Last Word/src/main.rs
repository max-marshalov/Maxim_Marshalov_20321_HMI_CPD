
    pub fn length_of_last_word(s: String) -> i32 {
        let mut vect:Vec<i32> = Vec::new();
    let byte = s.as_bytes();
    let mut c = String::new(); 
    for (i, &item) in byte.iter().enumerate(){
        
        if item == b' '{
            if c.len() != 0{
                vect.push(c.len() as i32);
            }
            c.clear();
            
            //println!("{}", c);
        }else{
            c.push(char::from(item));
        }
    }
    if c.len() != 0{
        vect.push(c.len() as i32);
        c.clear();
    }
    return vect.pop().unwrap();
    }
fn main(){
    println!("{:?}", length_of_last_word(String::from("hello world")))
}