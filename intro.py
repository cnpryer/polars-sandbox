# %%
import polars as pl
import numpy as np

from random import randint


n = 1000
df = pl.DataFrame(
    {
        "a": np.random.randint(0, 100, (n,)),
        "b": np.random.randint(0, 1000, (n,)),
    }
)

df = df.with_column(pl.lit("Thing").alias("c"))
df = df.with_column(
    pl.when(pl.col("a") > 50)
    .then(pl.lit("More than 50"))
    .otherwise(pl.col("c"))
    .alias("c")
)

# %%
df.sample(1, seed=randint(0, len(df)))


# %%
df = df.with_column(
    pl.when(pl.col("a") > 50)
    .then(pl.col("c").str.replace("More", "Greater"))
    .otherwise(pl.col("c"))
    .alias("c")
)

# %%``
df = df.with_column(df["a"].apply(lambda x: x * 100).alias("a"))
df = df.with_column(df.apply(lambda x: x["a"]))

# %%
