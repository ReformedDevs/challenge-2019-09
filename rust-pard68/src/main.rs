use num;
use rand;
use num::{FromPrimitive, Zero, One};
use num_bigint::{BigUint, RandBigInt};
use std::time;

extern crate num_bigint;

fn fib(max: usize) -> Vec<usize> {
    let mut seq = vec![0, 1];
    let mut prev: usize = 1;
    let mut curr: usize = 1;
    let mut next: usize;

    while curr < max {
        next = curr + prev;
        prev = curr;
        seq.push(curr);
        curr = next;
    }

    seq
}

fn is_prime(n: &BigUint) -> bool {
    let known_primes: [u32; 6] = [2, 3, 5, 7, 11, 13];
    let zero = BigUint::zero();
    for i in known_primes.iter() {
        if n % i == zero {
            return n==&(BigUint::from_u32(*i).unwrap())
        }
    }
    let (d,r) = decompose(n);
    let mut rng = rand::thread_rng();
    let two: BigUint = BigUint::from_u32(2).unwrap();

    let tests = 2;
    for _ in 0..tests {
        let a: BigUint = rng.gen_biguint_range(&two, &(n - 2u16));
        if composite(n, &d, &r, &a) {
            return false
        }
    }
    true
}

fn composite(n: &BigUint, d: &BigUint,
             r: &usize, a: &BigUint) -> bool
{
    let mut x = a.modpow(&d, &n);
    let one = BigUint::one();
    if x == one || x == (n - one) {
        return false
    }
    let two = BigUint::from_u32(2).unwrap();
    let n_minus_one = n - BigUint::one();
    for _ in 0..(r - 1) {
        x = x.modpow(&two, n);
        if n_minus_one == x {
            return false
        }
    }
    true
}

fn decompose(n: &BigUint) -> (BigUint, usize) {
    let mut d: BigUint = n - BigUint::one();
    let mut r: usize = 0;
    let two = BigUint::from_u32(2).unwrap();
    while (&d % &two).is_zero() {
        r += 1;
        d /= &two;
    }
    (d, r)
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
        let n128: u128 = *n as u128;
        let r: u128 = n128 * n128;
        if mask(r) {
             if is_prime(&BigUint::from_usize(*n).unwrap()) {
                let elapsed = start.elapsed();
                let time = ((elapsed.as_secs() as f64) + (elapsed.subsec_nanos() as f64 / 1_000_000_000.0)) * 1000.0;
                println!("pard68, Rust, {}, {}, Miller-rabin", *n, time);
                break;
            }
        }
    }
}
