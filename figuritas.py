def tipodefigurita(lista1):
    noRep=set(lista1)
    return(noRep)

def mefaltandeltipodefigurita(list,a,c):
    d=[]
    for i in a:
        x=list[i]
        if x==c:
            d.append(i)
    return(d)          

def notengo(mia,companero):
    fal=[]
    for i in companero:
        if i not in mia:
            fal.append(i)
    return(fal)

def puedocambiar(mia,companero):
    cont=int(0)
    for i in mia:
        if i not in companero:
            cont+=1
    return(cont)