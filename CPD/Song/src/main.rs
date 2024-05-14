fn main() {
    let objects_given = [
        "A Partridge in a Pear Tree",
        "Two Turtle Doves",
        "Three French Hens",
        "Four Calling Birds",
        "Five Gold Rings",
        "Six Geese A-Laying",
        "Seven Swans A-Swimming",
        "Eight Maids A-Milking",
        "Nine Ladies Dancing",
        "Ten Lords A-Leaping",
        "Eleven Pipers Piping",
        "Twelve Drummers Drumming"
    ];
    let mut suffix = "";
    for (i, object) in objects_given.iter().enumerate() {
        println!("On the {} day of Christmas my true love gave to me,", i+1);
        if i == 0 {println!("{}.", object);} else {
            for x in (0..(i+1)).rev() {
                if let 0 = x {println!("And {}.", objects_given[0]);} 
                else {println!("{},", objects_given[x]);} 
            }
        }
    }
}
