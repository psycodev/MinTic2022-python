notas = input("").upper().split(",")
sc = []
rep = []
cont = 1
for i in range(len(notas)-1):
  if notas[i] == notas[i+1]:    
    cont += 1;   
  else:
    sc.append(notas[i])
    rep.append(cont)
    cont = 1
print(" ".join(sc))
print(" ".join([str(_) for _ in rep])) 