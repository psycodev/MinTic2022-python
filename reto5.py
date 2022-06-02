def tipodefigurita(listaFiguras):
    figurasNoRepetidas = []
    for item in listaFiguras:
        if(item not in figurasNoRepetidas):
            figurasNoRepetidas.append(item)
    return figurasNoRepetidas

def puedocambiar(lista1, lista2):
    lista1_a_cambiar = 0
    lista2_a_cambiar = 0
    figuras_a_cambiar = 0
    for i in lista1:
        if(i not in lista2):
            lista1_a_cambiar += 1
    for i in lista2:
        if(i not in lista1):
             lista2_a_cambiar += 1
    if(lista1_a_cambiar < lista2_a_cambiar):
        figuras_a_cambiar = lista1_a_cambiar
    else:
        figuras_a_cambiar = lista2_a_cambiar
    return figuras_a_cambiar
    
def mefaltandeltipodefigurita(listaNum, listaFiguras, textoFigura):
    numerosFaltantes = []
    for i in listaNum:
        if(textoFigura == listaFiguras[i]):
            numerosFaltantes.append(i)
    return numerosFaltantes
def notengo(listaA, listaB):
    listaNoTengo = []
    for i in listaA:
        if(i not in listaB):
            listaNoTengo.append(i)
    return listaNoTengo