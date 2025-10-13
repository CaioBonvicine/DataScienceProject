import matplotlib.pyplot as plt
import pandas as pd

def grafico_categorias_em_crescimento(ds):
    ds['ano'] = pd.to_datetime(ds['order_date']).dt.year
    ultimo_ano = ds['ano'].max()
    
    decada = ds[ds['ano'] >= ultimo_ano - 10]
    vendas_por_ano = decada.groupby(['ano', 'category'])['quantity'].sum().unstack()
    
    crescimento = (vendas_por_ano.iloc[-1] - vendas_por_ano.iloc[0]) / vendas_por_ano.iloc[0]

    top_5 = crescimento.nlargest(5)
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_5.index, top_5.values, color='green')
    plt.title('Top 5 Categorias Em Crescimento')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
