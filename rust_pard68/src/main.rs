use std::time;

fn fib(max: usize) -> Vec<usize> {
    let mut seq = vec![0, 1];
    let mut prev: usize = 1;
    let mut curr: usize = 1;
    let mut next: usize;

    while curr < max {
        next = curr + prev;
        prev = curr;
        if is_prime(curr) {
            seq.push(curr);
        }
        curr = next;
    }

    seq
}

fn is_prime(n: usize) -> bool {
    if n < 2 {
        return false
    }
    if n == 3 {
        return true
    }
    if n % 2 == 0 {
        return false
    }
    if n % 3 == 0 {
        return false
    }

    let mut i: usize = 5;
    while i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false
        }
        i = i + 6;
    }
    true
}

fn mask(n: u128) -> bool {
    if n & 0xf == 0x9 {
        return true
    } else {
        return false
    }
}

fn main() {
    let start = time::Instant::now();
    let seq = fib(9_000_000_000_000_000_000);
    for n in seq.iter().rev() {
        let r: u128 = *n as u128 * *n as u128;
        if mask(r) {
            let elapsed = start.elapsed();
            let time = ((elapsed.as_secs() as f64) + (elapsed.subsec_nanos() as f64 / 1_000_000_000.0)) * 1000.0;
            println!("pard68, Rust, {}, {}, non-optimized", *n, time);
            break;
        }
    }
}
