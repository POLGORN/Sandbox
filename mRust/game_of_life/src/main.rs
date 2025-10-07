use rand::Rng;
use std::{thread, time};

const WIDTH: usize = 100;
const HEIGHT: usize = 50;

#[derive(Clone)]
struct Universe {
    cells: [[bool; WIDTH]; HEIGHT],
    generation: usize,
}

impl Universe {
    fn new() -> Self {
        let mut cells = [[false; WIDTH]; HEIGHT];

        // Стартовые паттерны
        add_pulsar(&mut cells, 40, 15);
        // add_blinker(&mut cells, 10, 5);

        Universe {
            cells,
            generation: 0,
        }
    }

    fn tick(&mut self) {
        let mut next = self.cells.clone();

        for y in 0..HEIGHT {
            for x in 0..WIDTH {
                let live_neighbors = self.live_neighbor_count(x, y);

                next[y][x] = match (self.cells[y][x], live_neighbors) {
                    (true, 2) | (true, 3) => true,
                    (false, 3) => true,
                    _ => false,
                };
            }
        }

        self.cells = next;
        self.generation += 1;

        // Периодически создаём глайдеры у краёв
        if self.generation % 50 == 0 {
            let mut rng = rand::thread_rng();
            if rng.gen_bool(0.5) {
                self.spawn_glider_at_edge();
            }
        }
    }

    fn spawn_glider_at_edge(&mut self) {
        let mut rng = rand::thread_rng();
        let edge = rng.gen_range(0..4); // 0: top, 1: bottom, 2: left, 3: right

        match edge {
            0 => { // top
                let x = rng.gen_range(1..(WIDTH - 5));
                add_glider(&mut self.cells, x, 0);
            }
            1 => { // bottom
                let x = rng.gen_range(1..(WIDTH - 5));
                let y = HEIGHT - 5;
                add_glider(&mut self.cells, x, y);
            }
            2 => { // left
                let y = rng.gen_range(1..(HEIGHT - 5));
                add_glider(&mut self.cells, 0, y);
            }
            3 => { // right
                let y = rng.gen_range(1..(HEIGHT - 5));
                let x = WIDTH - 5;
                add_glider(&mut self.cells, x, y);
            }
            _ => {}
        }
    }

    fn live_neighbor_count(&self, x: usize, y: usize) -> usize {
        let mut count = 0;
    
        for dy in [-1, 0, 1] {
            for dx in [-1, 0, 1] {
                if dx == 0 && dy == 0 {
                    continue;
                }
    
                let nx = ((x as isize + dx + WIDTH as isize) % WIDTH as isize) as usize;
                let ny = ((y as isize + dy + HEIGHT as isize) % HEIGHT as isize) as usize;
    
                if self.cells[ny][nx] {
                    count += 1;
                }
            }
        }
    
        count
    }

    fn render(&self) {
        // Верхняя рамка
        print!(".");
        for _ in 0..WIDTH {
            print!(".");
        }
        println!(".");

        // Поле с боковыми границами
        for row in &self.cells {
            print!(".");
            for &cell in row {
                print!("{}", if cell { "■" } else { " " });
            }
            println!(".");
        }

        // Нижняя рамка
        print!(".");
        for _ in 0..WIDTH {
            print!(".");
        }
        println!(".");
    }
}

// Паттерны

fn add_glider(cells: &mut [[bool; WIDTH]; HEIGHT], x: usize, y: usize) {
    let coords = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)];
    for &(dx, dy) in &coords {
        let nx = x + dx;
        let ny = y + dy;
        if nx < WIDTH && ny < HEIGHT {
            cells[ny][nx] = true;
        }
    }
}

fn add_blinker(cells: &mut [[bool; WIDTH]; HEIGHT], x: usize, y: usize) {
    let coords = [(x, y), (x + 1, y), (x + 2, y)];
    for &(nx, ny) in &coords {
        if nx < WIDTH && ny < HEIGHT {
            cells[ny][nx] = true;
        }
    }
}

fn add_pulsar(cells: &mut [[bool; WIDTH]; HEIGHT], x: usize, y: usize) {
    let relative_coords = [
        (2, 0), (3, 0), (4, 0), (8, 0), (9, 0), (10, 0),
        (0, 2), (5, 2), (7, 2), (12, 2),
        (0, 3), (5, 3), (7, 3), (12, 3),
        (0, 4), (5, 4), (7, 4), (12, 4),
        (2, 5), (3, 5), (4, 5), (8, 5), (9, 5), (10, 5),
        (2, 7), (3, 7), (4, 7), (8, 7), (9, 7), (10, 7),
        (0, 8), (5, 8), (7, 8), (12, 8),
        (0, 9), (5, 9), (7, 9), (12, 9),
        (0, 10), (5, 10), (7, 10), (12, 10),
        (2, 12), (3, 12), (4, 12), (8, 12), (9, 12), (10, 12),
    ];

    for &(dx, dy) in &relative_coords {
        let nx = x + dx;
        let ny = y + dy;
        if nx < WIDTH && ny < HEIGHT {
            cells[ny][nx] = true;
        }
    }
}

fn main() {
    let mut universe = Universe::new();
    let delay = time::Duration::from_millis(200);

    loop {
        print!("\x1B[2J\x1B[1;1H"); // очистка терминала
        universe.render();
        universe.tick();
        thread::sleep(delay);
    }
}

