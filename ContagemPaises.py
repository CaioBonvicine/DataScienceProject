import pandas as pd
df = pd.read_csv("global_arms_transfer_2000_2023.csv")

todos_paises = pd.concat([df["source"], df["target"]], ignore_index=True)

num_paises = todos_paises.nunique()
print(f"🌍 Total de países diferentes: {num_paises}\n")

contagem = todos_paises.value_counts()
print("📋 Transações por país:\n")
for pais, qtd in contagem.items():
    print(f"{pais}: {qtd} transações")

