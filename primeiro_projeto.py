import pandas as pd
#OBJETIVO: PUXAR O VENDEDOR QUE TENHA MAIS DE 55000 EM VENDAS.

# leitor das planilhas de acordo com cada mês.
lista_meses = ['abril','fevereiro','janeiro','junho','maio','março']

for mes in lista_meses:
    lista_vendas = pd.read_excel(f'{mes}.xlsx')
    if (lista_vendas['Vendas'] > 55000).any():
        Vendedor = lista_vendas.loc[lista_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = lista_vendas.loc[lista_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} foi encontrado uma venda com mais de 55000.\n Vendedor: {Vendedor}\n Valor de venda: {Vendas}')