import pandas as pd
from FuncoesDosGraficos.ImportacaoExportacao import graficos_importacao_exportacao
from FuncoesDosGraficos.Categorias import grafico_categorias
from FuncoesDosGraficos.TendenciasDeExportacao import grafico_tendencias_de_exportacao
from FuncoesDosGraficos.FornecedoresDesconhecidos import grafico_fornecedores_desconhecidos
from FuncoesDosGraficos.RotasComerciais import grafico_rotas_comerciais
from FuncoesDosGraficos.EvolucaoDasCategorias import grafico_categorias_em_crescimento

ds = pd.read_csv(r'C:\Users\Meu-PC\Documents\C11PythonProject\global_arms_transfer_2000_2023.csv', delimiter=',')


graficos_importacao_exportacao(ds)

grafico_categorias(ds)

grafico_tendencias_de_exportacao(ds)

grafico_rotas_comerciais(ds)

grafico_fornecedores_desconhecidos(ds)

grafico_categorias_em_crescimento(ds)



