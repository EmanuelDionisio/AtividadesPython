"""Efetue o cálculo e a apresentação do valor de uma
prestação em atraso utilizando a fórmula PRETAÇÃO =
VALOR + (VALOR * (TAXA / 100) * TEMPO)"""
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa: "))
tempo = float(input("Digite o tempo de atraso: "))
prestacao = valor+valor+(valor*(taxa/100)*tempo)
print("O valor da prestação com a taxa é de: ",prestacao)