lista1=input("ingrese sus palabras separadas por comas: ").split(",")
print(lista1)
def palindromos(lista1):
    for i in range(len(lista1)):
        normales=[i for i in (lista1[i])] 
        reverso=[i for i in reversed(lista1[i])] 
        normal=("".join(normales).replace(" ",""))
        reversa=("".join(reverso).replace(" ",""))
        
        if normal==reversa:
            print(f"{normal} y {reversa} Son palindromos")
        else:
            print(f"{normal} y {reversa} No son palindromos")

palindromos(lista1)

