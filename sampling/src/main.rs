use rand::{rngs::SmallRng, RngCore, SeedableRng};

fn get_num() -> u64 {
    let mut rng = SmallRng::from_entropy();

    let res = rng.next_u64();

    res
}

fn main() {
    println!("{}", get_num())
}
