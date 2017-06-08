"""A imobiliária imobilis vende apenas terrenos retangulares.
Faça um algoritmo para ler as dimensões de um terreno e,
depois, exibir a área do terreno."""
a, b = float(input("Digite um dos lados do terreno: ")), float(input("Digite outro lado do terreno: "))
c, d = float(input("Digite um dos lados do terreno: ")), float(input("Digite outro lado do terreno: "))
area1, area2 = a * b, c * d
print("A area do terreno 1 é: ",area1)
print("A area do terreno 2 é: ",area2)
