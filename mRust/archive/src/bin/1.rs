///////////////////////////
// Вывод числа Фибоначчи //
///////////////////////////

use std::io::{self, Write};
use std::process;

/// Выводит сообщение с ANSI цветом
fn print_colored(msg: &str, color_code: u8) {
    println!("\x1B[{}m{}\x1B[0m", color_code, msg);
}

/// Устанавливает обработчик сигнала Ctrc+C для корректного завершения программы
fn graceful_shutdown() {
    ctrlc::set_handler(|| {
        print_colored("\n[ Завершение программы ]", 92);
        process::exit(0);
    })
    .expect("Не удалось установить обработчик Ctrl+C");
}

/// Запрашиваем у пользователя число от 0 до 46
///
/// Возвращаем 'Ok(number)' при корректном вводе,
/// либо ошибку ввода
fn get_value() -> io::Result<u32> {
    loop {
        print!("Введите порядковый номер числа Фибоначчи (0..46): ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        match input.trim().parse::<u32>() {
            Ok(num @ 0..=46) => return Ok(num),
            _ => print_colored("[ Введено недопустимое значение ]", 31),
        }
    }
}

/// Вычисляет n-е число Фибоначчи
fn calculate_value(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let (mut a, mut b) = (0u64, 1u64);
            for _ in 2..=n {
                let next = a + b;
                a = b;
                b = next;
            }
            b
        }
    }
}

fn main() {
    print_colored("\n[ Запуск программы ]", 92);

    graceful_shutdown();

    match get_value() {
        Ok(n) => {
            let result = calculate_value(n);
            println!("Значение \x1B[92m{n}\x1B[0m-го числа Фибоначчи: \x1B[92m{result}\x1B[0m");
        }
        Err(e) => {
            eprintln!("[ Ошибка при вводе числа ]: {e}");
            process::exit(1);
        }
    }

    print_colored("[ Завершение программы ]", 92);
}
