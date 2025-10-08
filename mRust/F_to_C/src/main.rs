use std::io::{self, Write};
use std::process;

fn select_action() -> io::Result<u8> {
    println!("1. Фаренгейт(°F) в Цельсий(°C)\n2. Цельсий(°C) в Фаренгейт(°F)");

    loop {
        print!("Введите вариант 1 или 2: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        match input.trim().parse::<u8>() {
            Ok(num @ 1..=2) => return Ok(num),
            _ => print_colored("[ ВАРИАНТ ВВЕДЕН НЕКОРРЕКТНО ]", 31),
        }
    }
}

fn f_to_c(f: f32) -> f32 {
    (5.0 / 9.0) * (f - 32.0)
}

fn c_to_f(c: f32) -> f32 {
    (c * 1.8) + 32.0
}

fn enter_value() -> io::Result<f32> {
    loop {
        print!("Введите значение температуры: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        match input.trim().parse::<f32>() {
            Ok(value) => return Ok(value),
            _ => print_colored("[ ЗНАЧЕНИЕ ВВЕДЕНО НЕКОРРЕКТНО ]", 31),
        }
    }
}

fn print_colored(msg: &str, color_code: u8) {
    println!("\x1B[{}m{}\x1B[0m", color_code, msg);
}

fn main() -> io::Result<()> {
    print_colored("\n[ Начало программы ]", 92);

    ctrlc::set_handler(|| {
        print_colored("\n[ Конец программы ]", 92);
        process::exit(0);
    }).expect("Не удалось установить обработчик");

    let conversion_type = select_action()?;
    let input_temperature = enter_value()?;

    match conversion_type {
        1 => {
            let celsius = f_to_c(input_temperature);
            println!("{:.2}°F = \x1B[92m{:.2}\x1B[0m°C", input_temperature, celsius);
        }
        2 => {
            let fahrenheit = c_to_f(input_temperature);
            println!("{:.2}°C = \x1B[92m{:.2}\x1B[0m°F", input_temperature, fahrenheit);
        }
        _ => unreachable!(),
    };

    print_colored("[ Конец программы ]", 92);

    Ok(())
}
