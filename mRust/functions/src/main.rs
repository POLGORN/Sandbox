fn main() {
    println!("Hello, world!");

    fun0();
    fun1(5);
    fun2(5, 'h');
    let x = fun3();
    println!("fun3: The value of x is: {x}");
    let x = fun4(5);
    println!("fun4: The value of x is: {x}");
}

fn fun0() {
    println!("fun0: This is fun0");
}

fn fun1(x: i32) {
    println!("fun1: The value of x is: {x}");
}

fn fun2(value: i32, unit_label: char) {
    println!("fun2: The measurement is: {value}{unit_label}");
}

fn fun3() -> i32 {
    5
}

fn fun4(x: i32) -> i32 {
    x + 1
}
