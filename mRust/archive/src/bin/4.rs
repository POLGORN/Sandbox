///////////////////
// Display: List //
///////////////////

// Импортируем модуль `fmt`
use std::fmt; 

// Определяем структуру с именем `List`, которая хранит в себе `Vec`
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Получаем значение с помощью индекса кортежа 
        // и создаём ссылку на `vec`
        let vec = &self.0;

        write!(f, "[")?;

        // Пройдёмся по каждому `v` в `vec` 
        // Номер итерации хранится в `count`
        for (count, v) in vec.iter().enumerate() {
            // Для каждого элемента кроме первого добавляем запятую
            // до вызова `write!`. Используем оператор `?` или `try!`,
            // чтобы вернуться при наличии ошибок.
            if count != 0 { write!(f, ", ")?; }
            write!(f, "{}: {}", count, v)?;
        }

        // Закроем открытую скобку и вернём значение `fmt::Result`
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
