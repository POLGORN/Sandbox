/////////////
// Display //
/////////////
use std::fmt;

#[derive(Debug)]
struct MinMax(i64, i64);

impl fmt::Display for MinMax {
    fn fmt (&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({}, {})", self.0, self.1)
    }
}

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

impl fmt::Display for Point2D {
    fn fmt (&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

#[derive(Debug)]
struct Complex {
    real: f64,
    imag: f64,
}

impl fmt::Display for Complex {
    fn fmt (&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} + {}", self.real, self.imag)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("\n-- Сравниваем структуры --");
    println!("Display: {}", minmax);
    println!("Debug:   {:?}", minmax);

    let big_range = MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("Большой диапазон - {big} и маленький диапазон {small}",
        small = small_range,
        big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("\n-- Сравниваем точки: --");
    println!("Display: {}", point);
    println!("Debug:   {:?}", point);
    
    let complex = Complex { real: 3.3, imag: 7.2 };

    println!("\n-- Задание --");
    println!("Display: {}i", complex);
    println!("Debug:   {:?}", complex);
}
