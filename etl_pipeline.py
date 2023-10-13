import pandas as pd

# Passo 1: Extração
data = pd.read_csv("dados.csv")

# Passo 2: Transformação (multiplicar a coluna "valor" por 2)
data['valor'] = data['valor'] * 2

# Passo 3: Carregamento
data.to_csv("dados_transformados.csv", index=False)

print("Pipeline de ETL concluída com sucesso. Dados transformados salvos em 'dados_transformados.csv'.")
