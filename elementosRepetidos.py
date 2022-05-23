'''Desarrollar un programa que determine si en una lista no existen
elementos repetidos.'''

x=input('ingrese los elementos separados por comas de la lista aca: ').split(",")
print("la lista ingresada es: ", x)
lista2=[]
rep=[]
for i in x:
    if i in lista2:
        rep.append(i)
    else:
        lista2.append(i)
if len(x)==len(lista2):
    print("No ha datos repetidos")

else:
    print("Hay datos repetidos")
    print("La lista sin repetidos es: ",lista2)
    print("Se encontraron estos numeros repetidos",rep)


