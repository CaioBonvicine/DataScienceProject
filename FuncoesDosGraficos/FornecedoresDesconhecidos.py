import matplotlib.pyplot as plt

def grafico_fornecedores_desconhecidos(ds):
    desconhecidos = ds['source'].str.lower().str.contains('unknown')
    recebidores = ds[desconhecidos].groupby('target')['quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    recebidores.plot(kind='bar', color='red')
    plt.title('Top 10 recebidores de fornecedores desconhecidos')
    plt.ylabel('Quantidade')
    plt.xlabel('Países')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
