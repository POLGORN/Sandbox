#[derive(Debug)]
struct Structure(i32);

#[derive(Debug)]
struct Deep(Structure);

fn main() {
    println!("{:?} месяцев в году.", 12);
    println!("{1:?} {0:?} - это имя {actor:?}.", 
             "Слэйтер",
             "Кристиан",
             actor="актёра");
    println!("Теперь {:?} будет выведена на экран.", Structure(3));

}
