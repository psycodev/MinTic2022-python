armasVg=input("")
armasFs=input("")
reloj=input("")

scoreVg=0
scoreFs=0

for i in reloj:
    if i in armasVg:
        scoreVg+=1
    if i in armasFs:
        scoreFs+=1
    if scoreVg>scoreFs:
      print("V", end="")
    elif scoreFs>scoreVg:
      print("F", end="")
    elif scoreFs==scoreVg:   
      print("≈", end="")