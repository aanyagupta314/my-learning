fn main() {
    let mut num = 5;

    let r1 = &num as *const i32;

    println!("Hello, world! Address of variable num is {r1}");
}
