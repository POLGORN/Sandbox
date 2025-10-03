fn main() {
    let message = "Hello, world!";

    // цвета текста: базовые и яркие
    let basic_fg = 30..37;
    let bright_fg = 90..97;

    print!("--- Базовые цвета ---");
    for code in basic_fg.clone() {
        print!("\x1B[{}m{}\x1B[0m\n", code, message);
    }

    println!("--- Яркие цвета ---");
    for code in bright_fg.clone() {
        print!("\x1B[{}m{}\x1B[0m\n", code, message);
    }

    // цвета фона: базовые и яркие
    let basic_bg = 40..47;
    let bright_bg = 100..107;

    println!("--- Базовые цвета ---");
    for code in basic_bg.clone() {
        print!("\x1B[{}m{}\x1B[0m\n", code, message);
    }

    println!("--- Яркие цвета ---");
    for code in bright_bg.clone() {
        print!("\x1B[{}m{}\x1B[0m\n", code, message);
    }

    // свойства
    let properties = [
        ("сброс цвета", "0"),
        ("жирный", "1"),
        ("подчёркнутый", "4"),
        ("мигающий", "5"),
        ("инверсия", "7"),
    ];

    println!("--- Свойства ---");
    for (name, code) in &properties {
        print!("\x1B[97;{}m{}\x1B[0m // {}\n", code, message, name);
    }
}
