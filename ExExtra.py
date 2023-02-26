pa = float(input('Qual o preço do produto? R$ '))
d = pa - (pa*10/100)
a = pa + (pa*5/100)
print(f'Caso compre o produto a vista, o preço que antes era R${pa:.2f}, com o desconto de 10% acaba valendo R${d:.2f}')
print(f'Caso opte pela opção de boleto, o preço que antes era R${pa:.2f}, haverá um aumento de 5% e acabará valendo R${a:.2f}!')


