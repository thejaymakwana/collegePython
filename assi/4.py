import pandas as pd
import numpy as np
dict = {'First Score':[21, 22, np.nan, 54],
    'Second Score': [20, 69, 52, np.nan],
    'Third Score':[np.nan, 1, 20, 21]}
df = pd.DataFrame(dict)

print(df.isnull())