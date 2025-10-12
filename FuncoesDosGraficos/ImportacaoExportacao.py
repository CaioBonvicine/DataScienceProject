import matplotlib.pyplot as plt

def graficos_importacao_exportacao(ds):
    exportadores = ds.groupby('source')['quantity'].sum().sort_values(ascending=False).head(10)
    importadores = ds.groupby('target')['quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    exportadores.plot(kind='bar', color='steelblue')
    plt.title('Top Exportadores')
    plt.ylabel('Quantidade')
    plt.xlabel('Países')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10,5))
    importadores.plot(kind='bar', color='darkorange')
    plt.title('Top Importadores')
    plt.ylabel('Quantidade')
    plt.xlabel('Países')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
