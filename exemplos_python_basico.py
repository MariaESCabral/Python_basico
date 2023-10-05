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

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#● o produto do dobro do primeiro com metade do segundo.
#● a soma do triplo do primeiro com o terceiro.
#● o terceiro elevado ao cubo.

numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

produto = (2 * numero_inteiro1) * (numero_inteiro2 / 2)

soma = (3 * numero_inteiro1) + numero_real

cubo = numero_real ** 3

print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro elevado ao cubo é:", cubo)

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcula seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite sua altura em metros: "))
peso_ideal = (72.7 * altura) - 58

print(f"Seu peso ideal é {peso_ideal:.2f} kg")

#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72,7*h) - 58
#● Para mulheres: (62,1*h) - 44,7
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo não reconhecido.")
    peso_ideal = 0
if peso_ideal > 0:
    print(f"Seu peso ideal é {peso_ideal:.2f} kg")

#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele trouxer um peso de
#peixes maior que o previsto pelo regulamento de pesca do estado de São Paulo (50quilos) deverá pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
#você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
#multa variável o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens apropriadas.
peso_peixes = float(input("Digite o peso de peixes em quilos: "))
limite = 50

if peso_peixes > limite:
    excesso = peso_peixes - limite
    multa = excesso * 4.0
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a ser paga: R${multa:.2f}")
else:
    print("Dentro do limite de peso, sem multa.")

#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no mês específico, sabendo-se que são descontados 11% para o Imposto de Renda, 8%
#para o INSS e 5% para o sindicato, faça um programa que nos dê:
#● salário bruto.
#● quanto pagou ao INSS.
#● quanto pagou ao sindicato.
#● o salário líquido.
#calcule os descontos e o salário líquido, conforme tabela abaixo:
#● Salário Bruto: R$
#● IR (11%): R$
#● INSS (8%): R$
#● Sindicato (5%): R$
#● Salário Líquido: R$
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato

print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"IR (11%): R${ir:.2f}")
print(f"INSS (8%): R${inss:.2f}")
print(f"Sindicato (5%): R${sindicato:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura de tinta é 
#de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custa R$ 80,00. Informe ao usuário as quantidades de latas de tinta que
#serão compradas e o preço total.
area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 3  
litros_necessarios = area_pintada / cobertura_por_litro
latas_necessarias = int(litros_necessarios / 18) + (litros_necessarios % 18 > 0)
preco_total = latas_necessarias * 80.0

print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R${preco_total:.2f}")




#17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura de tinta é
#de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custa R$ 80,00 ou em galões de 3,6 litros, que custa R$ 25,00 .
#● Informe ao usuário as quantidades de tinta a serem compradas e os preços relevantes em 3 situações:
#● comprar apenas latas de 18 litros;
#● comprar apenas galões de 3,6 litros;
#● Ajuste latas e galões, de forma que o preço seja o menor. Adicione 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
area_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
cobertura_por_litro = 6 
litros_necessarios = area_pintada / cobertura_por_litro

latas18 = int(litros_necessarios / 18) + (litros_necessarios % 18 > 0)
galoes36 = int(litros_necessarios / 3.6) + (litros_necessarios % 3.6 > 0)

preco_latas18 = latas18 * 80.0
preco_galoes36 = galoes36 * 25.0

# Mistura latas e galões se for mais econômico
while litros_necessarios > 0:
    if litros_necessarios >= 18:
        latas18 += 1
        litros_necessarios -= 18
    else:
        galoes36 += 1
        litros_necessarios -= 3.6

preco_misto = latas18 * 80.0 + galoes36 * 25.0

print(f"Quantidade de latas de 18 litros: {latas18}")
print(f"Quantidade de galões de 3,6 litros: {galoes36}")
print(f"Preço com apenas latas de 18 litros: R${preco_latas18:.2f}")
print(f"Preço com apenas galões de 3,6 litros: R${preco_galoes36:.2f}")
print(f"Preço misturando latas e galões: R${preco_misto:.2f}")



#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Digite o tamanho do arquivo para download em MB: "))
velocidade_internet = float(input("Digite a velocidade do link de Internet em Mbps: "))

tempo_aproximado_minutos = (tamanho_arquivo * 8) / (velocidade_internet * 60)
print(f"Tempo aproximado de download: {tempo_aproximado_minutos:.2f} minutos")
