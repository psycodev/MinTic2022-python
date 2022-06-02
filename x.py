def puedocambiar(x,y,cont):
    for i in y:
        if i not in x:
            cont+=1
    return(cont)
print(puedocambiar(a,b,cont))