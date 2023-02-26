s = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados invalidos. Por favor, informe seu sexo correto [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))

