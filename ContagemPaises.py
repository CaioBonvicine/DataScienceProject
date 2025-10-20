import pandas as pd

ds = pd.read_csv(r'C:\Users\Meu-PC\Documents\C11PythonProject\global_arms_transfer_2000_2023.csv', delimiter=',')

todos_paises = pd.concat([ds["source"], ds["target"]])

num_paises = todos_paises.nunique()
print(f"Total de paises do dataset: {num_paises}\n")

contagem = todos_paises.value_counts()
print("Numero de transacoes de cada pais:\n")
for pais, qtd in contagem.items():
    print(f"{pais}: {qtd}")

