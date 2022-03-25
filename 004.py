#004

a = input('Digite algo: ')
# "a" é um objeto. Objetos possuem CARACTERISTICAS e realizam FUNCIONALIDADES, ou seja, ATRIBUTOS e MÉTODOS.
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizado?', a.istitle())