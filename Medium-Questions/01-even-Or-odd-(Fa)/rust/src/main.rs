use std::io;
fn main() {
    let mut input = String::new();
    println!("Enter your number: ");

    io::stdin().read_line(&mut input).expect("Try Again!");

    let input: u32 = input.trim().parse().expect("Enter an number between 1-100: ");

    let res:&'static str = validtion_number(input);

    println!("{}",res);

}


fn validtion_number(input:u32) -> &'static str  {
    if input >= 100 || input == 0{
        return "Invalid Number - Number must Between 1 to 100";
    }

    if input%2==0 {
        "Even Number"
    } else {
        "Odd Number"
    }
}
