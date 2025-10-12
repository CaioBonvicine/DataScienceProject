import matplotlib.pyplot as plt

def grafico_rotas_comerciais(ds): 
    top_routes = ds.groupby(['source', 'target'])['quantity'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    top_routes.plot(kind='bar', color='teal')
    plt.title('Top 10 Rotas Comerciais')
    plt.ylabel('Quantidade Total')
    plt.xlabel('Rota (Exportador, Importador)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
