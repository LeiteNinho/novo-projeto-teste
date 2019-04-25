from random import randint

sorteado = randint(1, 20)
tentativas = 0
while tentativas <= 6:
    palpite = int(input('Dê um palpite: '))
    if palpite == sorteado:
        print('Você acertou!')
        break
    if palpite > sorteado:
        print('Errou, palpite ALTO!')
    if palpite < sorteado:
        print('Errou, palpite Baixo!')
    tentativas += 1
