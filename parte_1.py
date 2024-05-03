# Descrição: Crie um programa que simule a quantidade de visualizações de dois canais do YouTube.
# 
# Defina dois canais de YouTube (`youtuber_a` e `youtuber_b`) e duas listas vazias (`visualizacoes_a` e `visualizacoes_b`).
# 
# Adicione 1 visualizações para cada canal no mês 0.
# Imprima o número de visualizações de cada canal no mês 0.
# Adicione 10 e 10 visualizações para cada canal no mês 1.
# Imprima o número de visualizações de cada canal no mês 1.
# Adicione 1000 e 500 visualizações para cada canal no mês 2.
# Imprima o número de visualizações de cada canal no mês 2.



youtuber_a = "Roberta Viradona"
youtuber_b = "Pacheco X9"

visualizacoes_a = []
visualizacoes_b = []

# ---------
print("Mês 0")
visualizacoes_a.append(1)
visualizacoes_b.append(1)
print(f"Visualizações do canal {youtuber_a}: {visualizacoes_a[0]}")
print(f"Visualizações do canal {youtuber_b}: {visualizacoes_b[0]}")

# ---------
print("Mês 1")
visualizacoes_a.append(10)
visualizacoes_b.append(10)
print(f"Visualizações do canal {youtuber_a}: {visualizacoes_a[1]}")
print(f"Visualizações do canal {youtuber_b}: {visualizacoes_b[1]}")

# ---------
print("Mês 2")
visualizacoes_a.append(1000)
visualizacoes_b.append(500)
print(f"Visualizações do canal {youtuber_a}: {visualizacoes_a[2]}")
print(f"Visualizações do canal {youtuber_b}: {visualizacoes_b[2]}")