import matplotlib.pyplot as plt

def grafico_categorias(ds):
    cats = ds.groupby('category')['quantity'].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10,5))
    cats.plot(kind='bar', color='seagreen')
    plt.title('Top Categories')
    plt.ylabel('Quantidade')
    plt.xlabel('Categorias')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
