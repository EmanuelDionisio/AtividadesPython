"""Calcule e apresente o valor do volume de uma lata de óleo
utilizando a fórmula: VOLUME = 3.14159 * RAIO / 2 *
ALTURA."""
from math import pi
print("O volume da ata de óleo é de ", (pi*float(input("Digite o Raio da lata: ")))/(2 * float(input("Digite a altura da lata: "))))