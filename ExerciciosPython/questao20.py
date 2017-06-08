"""Faça um algoritmo que efetue a apresentação do valor da
conversão em real de um número lido em dólar. O
programa lerá o calor da cotação do dólar e a quantidade
de dólares com o usuário, para apresentar o valor em
moeda brasileira."""
dolar = float(input("Quanto está a cotação do dólar hoje? "))
print("Vamos agora para os cálculos!!")
dinheiro = float(input("Quantos dólares você tem? "))
print("%.2f dólares em reais fica "%dinheiro, dinheiro * dolar)