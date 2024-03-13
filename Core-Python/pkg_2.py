import pandas as pd

import pkg_1 as p

r = p.func(20)

data = {'Name': ['Prashant', 'Boogie', 'X'],
        'Age': [28, 30, 27],
        'Sex': ['M', 'F', 'M']}

df = pd.DataFrame(data)

print(df)