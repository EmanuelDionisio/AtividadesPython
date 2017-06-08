"""Construa um algoritmo para ler os coeficientes do
polinômio P(x) = Ax4 + Bx3 + Cx2 + Dx + E. Depois, leia
o valor de x, calcule e imprima o valor de P(x)."""
print("Calcular o polinômio ---> P(x) = Ax4 + Bx3 + Cx2 + Dx + E")
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
D = float(input("Digite o valor de D: "))
E = float(input("Digite o valor de E: "))
X = float(input("Digite o valor de X: "))
P = A*X*4 + B*X*3 + C*X*2 + D*X + E
print("O valor de P(x) é: ", P)