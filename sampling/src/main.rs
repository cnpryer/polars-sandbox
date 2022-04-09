#![feature(once_cell)]
use rand::{rngs::SmallRng, RngCore, SeedableRng};

fn get_seed() -> u64 {
    let mut rng = SmallRng::from_entropy();

    let res = rng.next_u64();

    res
}

fn get_random_num(seed: Option<u64>) -> u64 {
    let mut rng = SmallRng::seed_from_u64(seed.unwrap_or(get_seed()));

    rng.next_u64()
}

fn main() {
    println!("{}", get_random_num(None))
}
