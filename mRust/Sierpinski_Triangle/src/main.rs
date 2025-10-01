fn main() {
    let depth = 5;
    let size = 1 << depth; // 2^depth
    let mut canvas = vec![vec![' '; 2 * size + 1]; size];

    draw_sierpinski(&mut canvas, size, 0, size);

    for row in canvas {
        let line: String = row.into_iter().collect();
        println!("{}", line);
    }
}

fn draw_sierpinski(canvas: &mut Vec<Vec<char>>, x: usize, y: usize, size: usize) {
    if size == 1 {
        canvas[y][x] = '*';
    } else {
        let half = size / 2;
        draw_sierpinski(canvas, x, y, half);
        draw_sierpinski(canvas, x - half, y + half, half);
        draw_sierpinski(canvas, x + half, y + half, half);
    }
}
