# %%
import polars as pl
import numpy as np


n = 1000
df = pl.DataFrame(
    {
        "a": np.random.randint(0, 100, (n,)),
        "b": np.random.randint(0, 1000, (n,)),
    }
)
