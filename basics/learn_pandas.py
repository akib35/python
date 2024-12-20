
# %% imports
import pandas as pd
import numpy as np

# %% 10 munites to pandas
s = pd.Series([1,3,4,np.nan,np.pi,500])

dates = pd.date_range("20250101",periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=pd.Series(list("ABCD")))
my_dict = {
    "A":1,
    "B":pd.Timestamp("20250101"),
    "C":pd.Series(1,index=list(range(4)),dtype="float32"),
    "D":np.array([3]*4,dtype="int32"),
    "E":pd.Categorical(["test","train","test","train"]),
    "F":"foo"
}
df2 = pd.DataFrame(my_dict)
df.sort

# %%
ts = pd.Series(np.random.randn(1000),index=pd.date_range("20250101",periods=1000))
ts = ts.cumsum()
ts.plot()
