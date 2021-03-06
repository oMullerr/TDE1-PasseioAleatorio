import random

def passeioAleatorio(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy

    return (x,y)

numberOfWalks = 10000 # numero de caminhadas

listaCaminhos = [0,0] # primeiro indice armazena o tamanho do caminho e o segundo indice armazena a %
for walk_lenght in range(1, 31): # caminhada de 1 ate 30 quarteiroes
    noTransport = 0
    for i in range(numberOfWalks):
        (x, y) = passeioAleatorio(walk_lenght)
        distance = abs(x) + abs(y)
        if distance <= 4: # se a distancia de casa for menor que 5, nao necessita de transporte
            noTransport += 1 # adicionamos 1 
    noTransportPercentage = float(noTransport)/numberOfWalks # pegamos a % 
    print("tamanho do caminho = ", walk_lenght, "/ % of no transport = ", noTransportPercentage*100)

    if listaCaminhos[0] < walk_lenght and noTransportPercentage*100 > 50: # se o tamanho do caminho for maior que o valor que tiver na lista e a % de transporte for maior que 50
        listaCaminhos[0] = walk_lenght # pegamos o novo tamanho da caminhada
        listaCaminhos[1] = noTransportPercentage*100 # pegamos a nova %

print('')
print("Desafio:")
print(listaCaminhos)
