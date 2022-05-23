lista1=input("ingrese sus palabras separadas por comas: ").split(",")
for i in range(len(lista1)):
    normales=[i for i in (lista1[i])] 
    reverso=[i for i in reversed(lista1[i])] 
    normal=("".join(normales))
    reversa=("".join(reverso))
    
    if normal==reversa:
        print(f"{normal} y {reversa} son palindromos")