import matplotlib.pyplot as plt

def grafico_fornecedores_desconhecidos(ds):
    mask = ds['source'].str.lower().str.contains('unknown')
    receivers = ds[mask].groupby('target')['quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    receivers.plot(kind='bar', color='red')
    plt.title('Top 10 recebidores de fornecedores desconhecidos')
    plt.ylabel('Quantidade')
    plt.xlabel('Países')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
