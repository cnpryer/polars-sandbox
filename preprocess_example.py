# %%
import numpy as np
import polars as pl

n, m = 10, 10
data = np.random.random((n, m))
cols = list("abcdefghij"[:m])
df = pl.DataFrame(data, columns=cols)

# %%
# optimizing memory footprint
df = df.with_columns([(pl.col(_) * 1000000).cast(pl.UInt32) for _ in cols])
