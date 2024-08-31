import json

def analisar_faturamento(arquivo_json):
  
  with open(arquivo_json, 'r') as f:
    dados = json.load(f)

  # Extrai os valores de faturamento, ignorando os dias sem venda
  valores_faturamento = [valor['valor'] for valor in dados if valor['valor'] > 0]

  # Calcula a média, o menor e o maior valor
  media = sum(valores_faturamento) / len(valores_faturamento)
  menor_valor = min(valores_faturamento)
  maior_valor = max(valores_faturamento)

  # Calcula o número de dias com faturamento acima da média
  dias_acima_media = sum(1 for valor in valores_faturamento if valor > media)

  return menor_valor, maior_valor, media, dias_acima_media

# Exemplo de uso
arquivo = 'faturamento.json'  
resultado = analisar_faturamento(arquivo)

if resultado:
  menor, maior, media, acima_media = resultado
  print(f"Menor valor de faturamento: R$ {menor:.2f}")
  print(f"Maior valor de faturamento: R$ {maior:.2f}")
  print(f"Média mensal: R$ {media:.2f}")
  print(f"Número de dias acima da média: {acima_media}")
else:
  print("Não há dados de faturamento válidos.")