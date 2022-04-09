# %%
import polars as pl
import numpy as np


df = pl.DataFrame({"a": [1.1, 2.2, np.nan, None]})
