"""Faça um algoritmo que leia dois inteiros A e B, e crie um
algoritmo para trocar os valores dessas variáveis"""
A,B = int(input("Digite o valor A: ")), int(input("Digite o valor de B: "))
print("A ",A," e B ",B," (antes de trocarem os valores)")
A,B = B,A
print("A ",A," e B ",B," (depois de trocarem os valores)")