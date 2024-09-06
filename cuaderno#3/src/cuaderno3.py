import pandas as pd
import numpy as np

# Taller
#https://colab.research.google.com/github/edelgado-1975/PandasOk/blob/main/Taller%20Pandas2.ipynb

best_sellers = pd.read_csv('bestsellers with categories.csv')
df = pd.DataFrame(best_sellers)

print(df)