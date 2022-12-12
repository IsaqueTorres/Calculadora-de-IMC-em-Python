
import os
os.system('clear')

print("....:::: Calculadora de IMC ::::....")

altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")
imc = float(peso) / (float(altura) * float(altura))
resultado = '{:.2f}'.format(imc)
print("Seu imc é: ", resultado)

if imc < 18.5:
    print("classificacao: Magreza")

elif imc > 18.5 and imc < 24.9:
    print("classificacao: Saudavel")

elif imc > 25 and imc < 29.9:
    print("classificacao: Sobrepeso")

elif imc > 30 and imc < 34.9:
    print("classificacao: Obesidade 1")

elif imc > 35 and imc < 39.9:
    print("classificacao: Obesidade 2 (Severa)")

elif imc > 40:
    print("classificacao: Obesidade 3 (morbida)")

else:
    print("Obrigado")
    
#           Calculo do IMC 
# imc = peso / (altura * altura)
# Veja a interpretação do IMC
# Entre 18,5 e 24,9	Normal	0
# Entre 25,0 e 29,9	Sobrepeso	I
# Entre 30,0 e 39,9	Obesidade	II
# Maior que 40,0	Obesidade Grave	III
# fonte: https://www.programasaudefacil.com.br/calculadora-de-imc
