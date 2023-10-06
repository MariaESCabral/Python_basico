# -*- coding: utf-8 -*-
"""Python_If_Else06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-bHoEt9GsvMvqVXOlg_zg-5hanjZgS_Z
"""

#1- Faça um programa que peça dois números e imprima o maior deles Dica: para realizar a inserção de dados pelo usuário utilize a função input("texto para o usuario")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
else:
    print("O maior número é:", numero2)

#2- Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#3- Faça um programa que verifique se uma letra digitada é “F” ou “M”. Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido.

genero = input("Digite F para feminino ou M para masculino: ")

if genero == 'F' or genero == 'f':
    print("Feminino")
elif genero == 'M' or genero == 'm':
    print("Masculino")
else:
    print("Sexo inválido")

#4- Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra in 'aeiouAEIOU':
    print("É uma vogal.")
else:
    print("É uma consoante.")


#5- Faça um programa para a leitura de duas notas parciais de um aluno.
#● A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#● A mensagem “Aprovado com Distinção”, se a média for igual a dez;
#● A mensagem “Reprovado” se a média for menor de do que sete;

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

#6- Faça um programa que leia três números e mostre o maior deles;
# Declaração e atribuição de variáveis
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

print("O maior número é:", maior)


#7- Faça um programa que leia três números e mostre o maior e o menor deles;

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print("O maior número é:", maior)
print("O menor número é:", menor)


#8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato.
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 <= preco2 and preco1 <= preco3:
    print("Compre o primeiro produto.")
elif preco2 <= preco1 and preco2 <= preco3:
    print("Compre o segundo produto.")
else:
    print("Compre o terceiro produto.")

#9- Faça um programa que leia três números e mostre-os em ordem decrescente.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

print("Números em ordem decrescente:", numeros)


#10- Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou
#“Boa Noite” ou “Valor inválido”, conforme o caso.
turno = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor inválido")




#11- As organizações CSM resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#● Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual;
#● Salários até RS 280,00 (incluindo): aumento de 20%;
#● Salários entre RS 280,00 e RS 700,00: aumento de 15%;
#● Salários entre RS 700,00 e RS 1500,00: aumento de 10%;
#● Salários de RS 1500,00 em diante: aumento de 5% Após o aumento ser realizado;
#Informe na tela os seguintes dados;
#● O salário antes do reajuste;
#● O percentual de aumento aplicado;
#● O valor do aumento;
#● O novo salário, após o aumento.
salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = (salario * percentual) / 100
novo_salario = salario + aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")



#12- Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o
#Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não é descontado (é a empresa que deposita.) O salário líquido corresponde ao salário bruto menos os descontos O
#programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#● Desconto do IR;
#● Salário Bruto ate RS900,00 (inclusive) – Isento;
#● Salário Bruto de RS 1500, 00 (inclusive) – desconto de 5%;
#● Salario bruto até RS 2500,00 (Inclusive) – desconto de 10%;
#● Salário bruto acima de 2500 – Desconto de 20%.
# Solicitar ao usuário o valor da hora e a quantidade de horas trabalhadas
#Imprima na tela as informações, dispostas conforme o exemplo abaixo, no exemplo valor da hora é 5 e a quantidade de horas é 220.plaintext
#Salário bruto (5 * 220) : RS 1100,00 ( - ) IR (5%) : RS 55,00 ( - ) INSS ( 10% ) : RS 110,00 FGTS ( 11%) : RS 121,00
#Total de descontos : RS 165,00
#Salário Líquido : RS 935,00

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

desconto_ir = (salario_bruto * desconto_ir) / 100
desconto_inss = (salario_bruto * 10) / 100
fgts = (salario_bruto * 11) / 100
total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário bruto ({valor_hora:.2f} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir}%): R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%): R$ {desconto_inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

#13 – Faça um Programa que leia um número e exiba o dia correspondente da semana. (1- Domingo , 2- Segunda, etc.) se digitar outro valor deve aparecer “valor inválido)
# Solicitar ao usuário um número de 1 a 7

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Valor inválido")


#14 – Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela
#abaixo: plaintext
#Média de aproveitamento Conceito
#Entre 9.0 e 10.0 A
#Entre 7.5 e 9.0 B
#Entre 6.0 e 7.5 C
#Entre 4.0 e 6.0 D
#Entre 4.0 e zero E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = "A"
    situacao = "APROVADO"
elif media >= 7.5:
    conceito = "B"
    situacao = "APROVADO"
elif media >= 6.0:
    conceito = "C"
    situacao = "APROVADO"
elif media >= 4.0:
    conceito = "D"
    situacao = "REPROVADO"
else:
    conceito = "E"
    situacao = "REPROVADO"

print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")


#15- Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
#equilátero, isósceles ou escaleno. Dicas:
#● Três lados formam um triangulo quando a soma de quaisquer dos dois lados é menor que o terceiro.
#● Triângulo Equilátero: três lados iguais;
#● Triângulo isósceles: quaisquer dois lados iguais;
#● Triângulo Escaleno: três lados diferentes;
#a = int(input("primeiro lado"))
#b = int(input("segundo lado"))
#c = int(input ("terceiro lado"))

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        tipo = "equilátero"
    elif a == b or a == c or b == c:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"É um triângulo {tipo}.")
else:
    print("Não é um triângulo válido.")


#16- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#● Se o usuário informar o valor de A igual a zero. a equação não e do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#● Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#● Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;
#● Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;

import math

a = float(input("Digite o valor de a: "))
if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui uma raiz real: x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")


#17- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano e ou não bissexto.
#Acesse aqui mais informações sobre ano bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")





#18- Faça um Programa que peça um número inteiro e determine se ele e par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#19- Faça um Programa que leia 1 número e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número e:
#● Par ou ímpar;
#● Positivo ou negativo;

numero = float(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("O número é par e positivo.")
    else:
        print("O número é ímpar e positivo.")
elif numero < 0:
    if numero % 2 == 0:
        print("O número é par e negativo.")
    else:
        print("O número é ímpar e negativo.")
else:
    print("O número é zero.")



#20- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#● "Telefonou para a vítima?"
#● "Esteve no local do crime?"
#● "Mora perto da vítima?"
#● "Devia para a vítima?"
#● "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre
#3 e 4 como "Cúmplice" e 5 como “Assassino“. Caso contrário, ele será classificado como "Inocente“.

telefonou = input("Telefonou para a vítima? (S/N): ").upper()
esteve_no_local = input("Esteve no local do crime? (S/N): ").upper()
mora_perto = input("Mora perto da vítima? (S/N): ").upper()
devia = input("Devia para a vítima? (S/N): ").upper()
trabalhou_com_vitima = input("Já trabalhou com a vítima? (S/N): ").upper()

contagem_sim = 0

if telefonou == "S":
    contagem_sim += 1
if esteve_no_local == "S":
    contagem_sim += 1
if mora_perto == "S":
    contagem_sim += 1
if devia == "S":
    contagem_sim += 1
if trabalhou_com_vitima == "S":
    contagem_sim += 1

if contagem_sim == 2:
    print("Você é Suspeito(a)!")
elif contagem_sim >= 3 and contagem_sim <= 4:
    print("Você é Cúmplice!")
elif contagem_sim == 5:
    print("Você é o Assassino!")
else:
    print("Você é Inocente!")


#21- Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
    print(f"O menor número é {num2}")
elif num2 > num1:
    print(f"O maior número é {num2}")
    print(f"O menor número é {num1}")
else:
    print("Os números são iguais.")


#22- Faça um programa que receba três inteiros e diga qual deles é o maior e qual o menor. DESAFIO: você consegue criar mais de uma solução?

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")


#23- Escreva um programa em C que recebe um inteiro e diga se é par ou ímpar. Dica: Use o operador matemático % (resto da divisão ou módulo) e o teste condicional if.
#include <stdio.h>

int main() {
    int numero;

    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    if (numero % 2 == 0) {
        printf("O número é par.\n");
    } else {
        printf("O número é ímpar.\n");
    }

    return 0;
}



#24- Escreva um programa que pergunte o raio de uma circunferência, e sem seguida mostre o diâmetro, comprimento e área da circunferência

import math

raio = float(input("Digite o raio da circunferência: "))

diametro = 2 * raio
comprimento = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print(f"Diâmetro: {diametro:.2f}")
print(f"Comprimento: {comprimento:.2f}")
print(f"Área: {area:.2f}")


#25- Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não. Use alguns dos operadores lógicos OU (||) e E (&&).

idade = int(input("Digite a idade: "))

if idade >= 18 and idade <= 67:
    print("Pode doar sangue.")
else:
    print("Não pode doar sangue.")


#26- Escreva um programa que pergunte o dia, mês e ano do aniversário de uma pessoa e diga se a data é válida ou não. Caso não seja, diga o motivo. Suponha que todos os meses tem 31dias e que estejamos no ano de 2013.
dia = int(input("Digite o dia do aniversário: "))
mes = int(input("Digite o mês do aniversário: "))
ano = int(input("Digite o ano do aniversário: "))

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano == 2013:
    print("Data válida.")
else:
    print("Data inválida.")



#27- Crie um programa que peça um número ao usuário e armazene ele na variável x. Depois peça outro número e armazene na variável y. Mostre esses números. Em seguida, faça com que x passe a ter o valor de y, e que y passe a ter o valor de x
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

print(f"Valor de x antes da troca: {x}")
print(f"Valor de y antes da troca: {y}")

temp = x
x = y
y = temp

print(f"Valor de x após a troca: {x}")
print(f"Valor de y após a troca: {y}")