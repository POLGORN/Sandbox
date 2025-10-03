fn main() {
    fun0();
    fun1();
    fun2();
    fun3();
    fun4();
    fun5();
    fun6();
    fun7();
    fun8();
    fun9();
    fun10();
    fun11();
}

fn fun0() {
    let number = 9;

    if number < 5 {
        println!("fun0: condition was true");
    } else {
        println!("fun0: condition was false");
    }
}

fn fun1() {
    let number = 3;

    if number != 0 {
        println!("fun1: number was something other than zero");
    }
}

fn fun2() {
    let number = 6;

    if number % 4 == 0 {
        println!("fun2: number is divisible by 4");
    } else if number % 3 == 0 {
        println!("fun2: number is divisible by 3");
    } else if number % 2 == 0 {
        println!("fun2: number is divisible by 2");
    } else {
        println!("fun2: number is not divisible by 4, 3, or 2");
    }
}

fn fun3() {
    let condition = false;
    let number = if condition { 5 } else { 6 };

    println!("fun3: The value of number is: {number}");
}

fn fun4() {
    loop {
        println!{"fun4: again!"};
        break
    }
}

fn fun5() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("fun5: The result is {result}");
}

fn fun6() {
    let mut count = 0;
    'counting_up: loop {
        println!("fun6: count = {count}");
        let mut remaining = 10;

        loop {
            println!("fun6: remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("fun6: End count = {count}");
}

fn fun7() {
    let mut number = 3;

    while number != 0 {
        println!("fun7: {number}!");

        number -= 1;
    }

    println!("fun7: LIFTOFF!!!");
}

fn fun8() {
    let mut number = 3;

    loop {
        if number == 0 {
            println!("fun8: LIFTOFF!!!");
            break
        }
        println!("fun8: {number}!");
        number -= 1;
    }
}

fn fun9() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("fun9: the value is: {}", a[index]);

        index += 1;
    }
}

fn fun10() {
    let a = [10, 20, 30, 40, 50];
    
    for element in a {
        println!("fun10: the value is: {element}"); 
    }
}

fn fun11() {
    for number in (1..4).rev() {
        println!("fun11: {number}!");
    }
    println!("fun11: LIFTOFF!!!");
}
