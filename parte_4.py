# ...
# Substitua os cálculos de diferença de visualizações por uma função avalia_diferenca() com dois argumentos de entrada visualizacoes e youtuber.
# A partir do mês 1, calcule a diferença de visualizações entre os canais
# A diferença pode ser calculada subtraindo a quantidade do último mês menos a do mês anterior
# Compare e imprima a diferença de visualizações entre os canais ao decorrer dos meses


# Substituindo os cálculos por uma função
def avalia_diferenca(youtuber, vizualizacoes):
    youtuber = 

# ...
youtuber_a = "Roberta Viradona"[0]
youtuber_b = "Pacheco X9"[1]
youtuber = [youtuber_a, youtuber_b]

visualizacoes_a = []
visualizacoes_b = []
visualizacoes = [visualizacoes_a, visualizacoes_b]

# ---------
print("Mês 0")
visualizacoes[0].append(1)
visualizacoes[1].append(1)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][0]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][0]}")

# ---------
print("Mês 1")
visualizacoes[0].append(10)
visualizacoes[1].append(10)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][1]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][1]}")

# --------- cálculo da diferença de visualizações mes 1 para mes 0
diferenca_a = visualizacoes[0][1] - visualizacoes[0][0]
diferenca_b = visualizacoes[1][1] - visualizacoes[1][0]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a} visualizações a mais do que o canal {youtuber[1]}.")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b} visualizações a mais do que o canal {youtuber[0]}.")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")

# ---------
print("Mês 2")
visualizacoes[0].append(1000)
visualizacoes[1].append(500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][2]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][2]}")

# --------- cálculo da diferença de visualizações mes 2 para mes 1
diferenca_a = visualizacoes[0][2] - visualizacoes[0][1]
diferenca_b = visualizacoes[1][2] - visualizacoes[1][1]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a} visualizações a mais do que o canal {youtuber[1]}.")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b} visualizações a mais do que o canal {youtuber[0]}.")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")


# ---------
print("Mês 3")
visualizacoes[0].append(2000)
visualizacoes[1].append(1500)
print(f"Visualizações do canal {youtuber[0]}: {visualizacoes[0][3]}")
print(f"Visualizações do canal {youtuber[1]}: {visualizacoes[1][3]}")

# --------- cálculo da diferença de visualizações mes 3 para mes 2
diferenca_a = visualizacoes[0][3] - visualizacoes[0][2]
diferenca_b = visualizacoes[1][3] - visualizacoes[1][2]
if diferenca_a > diferenca_b:
    print(f"O canal {youtuber[0]} teve {diferenca_a} visualizações a mais do que o canal {youtuber[1]}.")
elif diferenca_a < diferenca_b:
    print(f"O canal {youtuber[1]} teve {diferenca_b} visualizações a mais do que o canal {youtuber[0]}.")
else:
    print("Os canais tiveram a mesma quantidade de visualizações.")

