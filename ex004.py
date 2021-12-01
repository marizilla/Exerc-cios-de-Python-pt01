n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('Está escrito em letras maiúsculas? ', n.isupper())
print('Está escrito em letras minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())

