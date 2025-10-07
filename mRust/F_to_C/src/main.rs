use std::io::{self, Write};

enum Status {
    Success,
    Warning,
    Failure,
}

impl Status {
    fn color_code(&self) -> u8 {
        match self {
            Status::Success => 92, // зелёный
            Status::Warning => 34, // синий
            Status::Failure => 31, // зелёный
        }
    }
    fn label(&self) -> &'static str {
        match self {
            Status::Success => "Success",
            Status::Warning => "Warning",
            Status::Failure => "Failure",
        }
    }
    fn colored_label(&self) -> String {
        format!("\x1B[{}m{}\x1B[0m", self.color_code(), self.label())
    }
}

fn print_status(status: Status, msg: &str) {
    println!("[ {} ] {}", status.colored_label(), msg);
}

fn read_trimmed_line() -> io::Result<String> {
    let mut s = String::new();
    io::stdin().read_line(&mut s)?;
    Ok(s.trim().to_string())
}

fn normalize_and_parse(s: &str) -> Result<f32, &'static str> {
    let s = s.trim();
    if s.is_empty() {
        return Err("empty");
    }
    if s.eq_ignore_ascii_case("error") || s.eq_ignore_ascii_case("fail") {
        return Err("failure");
    }
    // Заменяет запятую на точку (адаптация ввода)
    let normalized = s.replace(',', ".");
    // Отвергаем строки с более чем одним '.' (например "1.2.3.")
    if normalized.matches('.').count() > 1 {
        return Err("invalid");
    }
    normalized.parse::<f32>().map_err(|_| "invalid")
}

fn read_choice() -> io::Result<u8> {
    loop {
        print!("Доступные конвертации:\n1. Фаренгейт(°F) в Цельсий(°C)\n2. Цельсий(°C) в Фаренгейт(°F)\nВведите нужную(1/2): ");
        io::stdout().flush()?;
        let input = read_trimmed_line()?;
        match input.as_str() {
            "1" => return Ok(1),
            "2" => return Ok(2),
            "" => {
                print_status(Status::Warning, "Пустой ввод - попробуйте ещё раз");
                continue;
            }
            s if s.eq_ignore_ascii_case("error") || s.eq_ignore_ascii_case("fail") => {
                print_status(Status::Failure, "Введено запрещённое слово");
                continue;
            }
            _ => {
                print_status(Status::Warning, "Неверный выбор - введите 1 или 2");
                continue;
            }
        }
    }
}

fn read_value(prompt: &str) -> io::Result<f32> {
    loop {
        print!("{}", prompt);
        io::stdout().flush()?;
        let input = read_trimmed_line()?;
        match normalize_and_parse(&input) {
            Ok(v) => return Ok(v),
            Err("empty") => {
                print_status(Status::Warning, "Пустой ввод - попробуйте ещё раз");
                continue;
            }
            Err("failure") => {
                print_status(Status::Failure, "Введено запрещённое ключевое слово");
                continue;
            }
            Err("invalid") => {
                print_status(Status::Warning, "Неверный формат числа - используйте цифры и разделитель '.' или ','");
                continue;
            }
            Err(_) => {
                print_status(Status::Failure, "Неизвестная ошибка");
                continue;
            }
        }
    }
}

fn f_to_c(f: f32) -> f32 {
    (5.0 / 9.0) * (f - 32.0)
}

fn c_to_f(c:f32) -> f32 {
    (c * 1.8) + 32.0
}

fn main() -> io::Result<()> {
    let choice = read_choice()?;
    if choice == 1 {
        let f = read_value("Введите температуру в Фаренгейтах: ")?;
        let c = f_to_c(f);
        print_status(Status::Success, &format!("{} °F -> {:.4} °C", f, c));
    } else {
        let c = read_value("Введите температуру в Цельсиях: ")?;
        let f = c_to_f(c);
        print_status(Status::Success, &format!("{} °C -> {:.4} °F", c, f));
    }
    Ok(())
}
