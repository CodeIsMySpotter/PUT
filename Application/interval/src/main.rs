use rug::{Float, float::Constant};



fn main() {
    let precision = 128;
    let number_str = "0.1";

    let parsed = Float::parse(number_str).expect("[ERROR]");
    let mut number = Float::with_val(precision, parsed); 

    let next = number.next_up();
    let prev = number.next_down();

    // Wyświetlenie wyników z wysoką precyzją
    println!("x          = {:.50}", number);
    println!("Next up    = {:.50}", next);
    println!("Next down  = {:.50}", prev);

    //println!("Next Float128 = {}", next);
    //println!("Previous Float128 = {}", prev);
}
