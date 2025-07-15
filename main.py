import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.DataFrame({
    'nome': ['joao', 'jose', 'maria', 'jose'],
    'idade': [15, 20, 20, 30]
})

hist = plt.hist(tabela['nome'])
print(hist)