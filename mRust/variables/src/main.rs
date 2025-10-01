fn main() {
    // === Scalar data types ===
    println!("=== Scalar data types ===");
    /*
    --- INT ---
    */
    let u8_max: u8 = 255;
    let i8_min: i8 = -128;
    let u16_max: u16 = 65_535;
    let i16_min: i16 = -32_768;
    let u32_max: u32 = 4_294_967_295;
    let i32_min: i32 = -2_147_483_648;

    let hex = 0xff;
    let oct = 0o377;
    let bin = 0b1111_1111;
    let byte = b'\xFF';

    println!("--- INT ---");
    println!("u8 max:               {}", u8_max);
    println!("i8 min:               {}", i8_min);
    println!("u16 max:              {}", u16_max);
    println!("i16 min:              {}", i16_min);
    println!("u32 max:              {}", u32_max);
    println!("i32 min:              {}", i32_min);
    println!("u64+:                 ...");
    println!("i64+:                 ...");
    println!("Hexadecimal(0xff):    {}", hex);
    println!("Octal(0o377):         {}", oct);
    println!("Binary(0b1111_1111):  {}", bin);
    println!("Byte:                 {}", byte);
    /*
    --- FLOAT ---
    */
    let x = 2.0;                    // f64
    let y: f32 = 3.0;               // f32

    println!("--- FLOAT ---");
    println!("f64:                  {}", x);
    println!("f32:                  {}", y);
    /*
    --- BOOL ---
    */
    let t = true;
    let f: bool = false;

    println!("--- BOOL ---");
    println!("true is:              {}", t);
    println!("false is:             {}", f);
    /*
    --- CHAR ---
    */
    let c = 'z';
    let z: char = 'Z';
    let emoji = '\u{1F30D}'; 

    println!("--- CHAR ---");
    println!("char 'z' is:          {}", c);
    println!("char 'Z' is:          {}", z);
    println!("emoji is:             {}", emoji);
    // === Composite data types ===
    println!("=== Composite data types ===");
    /*
    --- TUPLE ---
    */
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;
    let five_hundred = tup.0;
    let six_point_four = tup.1;
    let one = tup.2;

    println!("--- TUPLE ---");
    println!("prime tuple is:       {:?}", tup);
    println!("tuple is:             {}, {}, {}", x, y, z);
    println!("1st element is:       {}", five_hundred);
    println!("2st element is:       {}", six_point_four);
    println!("3st element is:       {}", one);
    /*
    --- ARRAY
    */
    let a = [1, 2, 3, 4, 5];
    let b: [i32; 5] = [6, 7, 8, 9, 0];
    let c = [3; 5];
    let first = a[0];
    let second = a[1];
    let third = a[2];

    println!("--- ARRAY ---");
    println!("array is:             {:?}", a);
    println!("type-array is:        {:?}", b);
    println!("same-value-array is:  {:?}", c);
    println!("array[0] is:          {}", first);
    println!("array[1] is:          {}", second);
    println!("array[2] is:          {}", third);
}
