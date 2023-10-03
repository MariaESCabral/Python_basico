# -*- coding: utf-8 -*-
"""Exemplos_Python_basico

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LBABG8VTqkhZxODGC1wpnpy9kQkJSRMp
"""

#1.Faça um Programa que mostra a mensagem "Alô mundo" na tela.
print("Alô mundo")

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = float(input("Digite um número: "))
print("O numero digitado foi:", numero)

#3.Faça um Programa que peça dois números e imprima a soma
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é:",soma)

#4-Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média das notas é:",media)

#5. Faça um Programa que converte metros para centímetros.
metros = float(input("Digite a medida em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centímetros.")

#6. Faça um Programa que parte o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * (raio ** 2)
print("A área do círculo é:",area)

#7. Faça um programa que calcula a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o comprimento do lado do quadrado: "))
area = lado ** 2
dobro_area = 2 * area
print("A área do quadrado é:", area)
print("O dobro da área é:",dobro_area)

#8. Faça um Programa que pergunta quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
valor_por_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = valor_por_hora * horas_trabalhadas
print(f"Seu salário no referido mês é: R${salario:.2f}")

#9. Faça um Programa que parte a temperatura em graus Farenheit, transforma e mostra a temperatura em graus Celsius. C=(5*(F-32)/9).
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
celsius = (5 * (fahrenheit - 32)) / 9
print(f"A temperatura em graus Celsius é: {celsius:.2f}°C")

#10. Faça um programa que parte a temperatura em graus Celsius, transforma e mostra em graus Farenheit.
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}°F")
