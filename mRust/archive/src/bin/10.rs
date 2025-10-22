#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// unit-структура
struct Unit;

// Кортежная структура
struct Pair(i32, f32);

// Структура с двумя полями
struct Point {
    x: f32,
    y: f32,
}

// Структуры могут быть использованы в качестве полей другой структуры
#[allow(dead_code)]
struct Rectangle {
    // Прямоугольник может быть определен по расположению в пространстве
    // его верхнего левого и нижнего правого углов
    top_left: Point,
    bottom_right: Point,
}

// з1. Высчитать площадь прямоугольника
fn rect_area(a: Point, b: Point) -> f32 {
    let Point { x: ax, y: ay } = a;
    let Point { x: bx, y: by } = b;

    (ax - bx).abs() * (ay - by).abs()
}
// ---

fn main() {
    // Создадим структуру при помощи сокращенной инициализации полей
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // Распечатаем отладочную информацию о структуре
    println!("{:?}", peter);

    // Инициализируем `Point`
    let point: Point = Point { x: 10.3, y: 0.4 };

    // Получаем доступ к полям структуры
    println!("Первая точка: ({}, {})", point.x, point.y);

    // Создадим новую точку используя обновленную структуру и существующую точку
    let bottom_right = Point { x: 5.3, ..point };

    // `bottom_right.y` будет таким же как и у `point.y` так как мы взяли это поле из `point`
    println!("Вторая точка: ({}, {})", bottom_right.x, bottom_right.y);

    // ---
    let exp_point = Point { x: 3.3, ..point };
    println!("Тестовая точка: ({}, {})", exp_point.x, exp_point.y);
    // --- 

    // Деструктурируем структуру при помощи `let`
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // создание структуры так же является выражением
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // Создадим unit-структуру
    let _unit = Unit;

    // Создадим кортежную структуру
    let pair = Pair(1, 0.1);
    
    // Доступ к полям кортежной структуры
    println!("pair содержит {:?} и {:?}", pair.0, pair.1);

    // Деструктурируем кортежную структуру
    let Pair(integer, decimal) = pair;

    println!("pair2 содержит {:?} и {:?}", decimal, integer);

    // ---
    println!("Площадь прямоугольника равна: {}", rect_area(point, exp_point));
    // ---
}
