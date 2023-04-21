first_name = "Marjorie"
last_name = "Matus de la Parra"
print(first_name + " " + last_name)

mensaje1 = "Hola " *3
print(mensaje1)

mensaj3 = "Marjorie"
print(mensaj3)
mensaj3 += ","
print(mensaj3)
mensaj3 += " lisette"
print(mensaj3)

print(len(mensaj3))

cadena = "esto es una oracion por ucrania"
posicion = cadena.find("pelo")
print("pelo se encuentra en: ", posicion)
posicion = cadena.find("ucrania")
print("ucrania se encuentra en:", posicion)

utilizalower = ("mi name is mayo")
print(utilizalower)

mensaje3 = "me gusta el aguacate"
x = mensaje3.replace("tomate", "durazno")
print(x)
print(mensaje3.replace("tomate", "lechuga"))

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4, [2, "a"], {"name": "Marjorie"}, (1, 3, 5)]
print(fullfiled_list)

range_one = range(50)
print(list(range_one))

numeros = (1, 4, 6)
print(numeros)
numeros.append(10)
print(numeros)

print(numeros(2))


print("======= Tupas ======= ")

empty_tuple = ()
fullfiled_tuple = (1, "Marjorie", 900.87)

print(empty_tuple, fullfiled_tuple)

print(type(fullfiled_tuple))

one_tuple = ('maggy')
print(type(one_tuple))

hojas = 'carta', 'oficio'
print(type(hojas))
print(hojas)

empty_tuple_2 = tuple()
print(empty_tuple_2)

list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)