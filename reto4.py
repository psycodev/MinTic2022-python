import json
entrada1=input("")
d = json.loads(entrada1)
entrada2=input("")

listasal=[]
tarjetasal=[]

for i in entrada2:
    solbusq=d.get(i)
    if solbusq != None :
        listasal.append(solbusq)
        tarjetasal.append(i)
        
segundafil=" ".join(tarjetasal)
print(sum(listasal))
print(segundafil)