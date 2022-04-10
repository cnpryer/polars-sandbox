use core::mem::size_of;
use polars::prelude::{DataFrame, NamedFrom, Series};

const FILLER_INT: u32 = 1;
const N: usize = 10_000_000;

// create df
fn get_df() -> DataFrame {
    let a = Series::new("a", vec![FILLER_INT; N]);
    let b = Series::new("b", vec![FILLER_INT; N]);
    let c = Series::new("c", vec![FILLER_INT; N]);

    DataFrame::new(vec![a, b, c]).unwrap()
}

// get size of each col from df as summary df
// TODO: derive type of series data (is this even possible?)
fn get_columns_summary(df: &DataFrame) -> Vec<Series> {
    let totals = df
        .get_columns()
        .iter()
        .map(|s| Series::new(s.name(), &[(s.len() * size_of::<u32>()) as u32]))
        .collect();

    totals
}

// sum sizes from each col
fn get_total_col(df: &Vec<Series>) -> Series {
    let mut sum: u32 = 0;
    for col in df {
        sum += col.sum().unwrap_or_else(|| 0);
    }
    let total = Series::new("total", vec![sum]);

    total
}

// TODO: add memory usage from any extras
fn main() {
    let df = get_df();
    let mut totals = get_columns_summary(&df);
    totals.push(get_total_col(&totals));

    // create summary df
    let summary = DataFrame::new_no_checks(totals);

    println!("{}", summary);
}
