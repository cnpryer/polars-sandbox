# %%
import polars as pl
import numpy as np
import sys

from random import randint, SystemRandom


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

# %%
df = df.with_column(df["a"].apply(lambda x: x * 100).alias("a"))
# df = df.with_column(df.apply(lambda x: x["a"]))

# %%
df = df.with_column(
    pl.when((pl.col("c").str.contains("Greater")) & (pl.col("b") < 100))
    .then(pl.lit("Special"))
    .otherwise(pl.col("c"))
    .alias("d")
)


# %%
g = df.groupby(by="c").agg(pl.n_unique("d"))


# %%
generator = SystemRandom()
seed = generator.randint(0, sys.maxsize * 2)

# %%


with pl.StringCache():
    df = df.with_column((pl.col("c").cast(pl.Categorical)))

    res = df.filter(
        pl.col("c").is_in(pl.Series(["Thing"]).cast(pl.Categorical))
    )

res
# %%

with pl.StringCache():
    res = df.with_column((pl.col("country").cast(pl.Categorical))).filter(
        pl.col("country").is_in(
            pl.Series(["Sri Lanka", "Turkey"]).cast(pl.Categorical)
        )
    )
