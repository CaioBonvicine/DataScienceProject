import pandas as pd
import matplotlib.pyplot as plt

def grafico_tendencias_de_exportacao(ds):
    ds_ano = pd.to_datetime(ds['order_date']).dt.year
    top_5 = ds['source'].value_counts().nlargest(5).index


    plt.figure(figsize=(10,5))
    for pais in top_5:
        dados_pais = ds[ds['source'] == pais]
        tendencia = dados_pais.groupby(ds_ano).size()
        plt.plot(tendencia.index, tendencia.values, marker='o', label=pais)

    plt.title('Tendência de Exportações - Top 5 Países')
    plt.xlabel('Ano')
    plt.ylabel('Número de Exportações')
    plt.legend()
    plt.tight_layout()
    plt.show()
