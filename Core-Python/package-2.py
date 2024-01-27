import pandas as pd
df = pd.read_parquet('D:\pythonProjects\Core-Python\Python_Geegks_for_Geeks\lbd_pq_10k.parquet')
df.to_csv('my_file_1.csv')