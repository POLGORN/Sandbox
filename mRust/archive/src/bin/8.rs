/////////////
// Кортежи //
/////////////

// з1 Добавить std::fmt
use std::fmt::{self, Display, Formatter};

// Кортежи могут быть использованы как аргументы функции
// и как возвращаемые значения
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` можно использовать для создания связи между кортежем и переменной
    let (integer, boolean) = pair;

    (boolean, integer)
}

// з2 Добавление функции transpose
fn transpose(m: Matrix) -> Matrix {
    Matrix(m.0, m.2, m.1, m.3)
}

// Эта структура используется для задания
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

// з1 Реализовать fmt::Display
impl Display for Matrix {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        write!(f, "( {} {} )\n( {} {} )",
            self.0, self.1, self.2, self.3)
    }
}

fn main() {
    // Кортеж с множеством различных типов данных
    let long_tuple = (1u8, 2u16, 3u32, 4u64, -1i8, -2i16, -3i32, -4i64, 0.1f32, 0.2f64, 'a', true);

    // К значениям переменных внутри кортежа можно обратиться по индексу
    println!("Первое значение длинного кортежа: {}", long_tuple.0);
    println!("Второе значение длинного кортежа: {}", long_tuple.1);

    // Кортежи могут содержать в себе кортежи
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Кортеж можно напечатать
    println!("Кортеж из кортежей: {:?}", tuple_of_tuples);

    // Но длинные кортежи не могут быть напечатаны
    // let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    // println!("Слишком длинный кортеж: {:?}", too_long_tuple);

    let pair = (1, true);
    println!("pair хранит в себе {:?}", pair);

    println!("перевёрнутая pair будет {:?}", reverse(pair));

    // Для создания кортежа содержащего один элемент необходимо написать элемент и 
    // поставить запятую внутри круглых скобок
    println!("Кортеж из одного элемента: {:?}", (5u32,));
    println!("Просто целочисленное значение: {:?}", (5u32));

    // Кортежи можно разобрать на части для создания связи
    let tuple = (1, "привет", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    // з1 Создать и вывести Matrix
    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{}", matrix);
    
    // з2 Добавить реализацию функции transpose
    println!("{}", transpose(matrix));
}
