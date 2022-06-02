"""una hmbugueseria ofrece hamburguesas sencillas, dobles y triples las cuales tienen un costo de 20000, 25000 y 28000 respectivamente. la empresa acepta tarjetas de credico con un cargo de 7%, otros medios de pago 0%. suponiendo que los clientes adquieren solo un tipo de hambuirguesa, realice un programa para determinar cuando debe pagar un cliente por N hamburguesa"""

sencilla=20000
doble=25000
triple=28000
contS=0
contD=0
contT=0
pedido=[]
valorP=[]
ped=True
res=""
print("---------------------------")
print ("BIENVENIDO A IN-OUT-BURGER")
print("---------------------------")
print("      NUESTRO MENU")
print("---------------------------")
print("HAMBRUGUESA SENCILLA - 20000")    
print("HAMBRUGUESA DOBLE    - 25000")
print("HAMBRUGUESA TRIPLE   - 28000") 
print("---------------------------")

while ped==True: 
    order=input("CUAL DESEAS ORDENAR: ").upper()
    print("Tu pedido fue: ", order)
    if order=="HAMBURGUESA SENCILLA" or order=="SENCILLA":
      contS+=1
      pedido.append(order)
      valorP.append(sencilla)
      print("Total del pedido es: ",sum(valorP))
      res=input("DESEA PEDIR ALGO MAS: ").upper()
      if res=="NO":
        ped=False
    elif order=="HAMBURGUESA DOBLE" or order=="DOBLE":
      contD+=1
      pedido.append(order)
      valorP.append(doble)
      print("Total del pedido es: ",sum(valorP))
      res=input("DESEA PEDIR ALGO MAS: ").upper()
      if res=="NO":
        ped=False
    elif order=="HAMBURGUESA TRIPLE" or order=="TRIPLE":
      contT+=1
      pedido.append(order)
      valorP.append(triple)
      print("Total del pedido es: ",sum(valorP))
      res=input("DESEA PEDIR ALGO MAS: ").upper()
      if res=="NO":
        ped=False
print("---------------------------")
res2=input("¿Quieres ver tu orden antes de proseguir al pago?").upper()
if res2=="SI":
  print("El total de hamburguesas sencillas fue: ",contS)
  print("El total de hamburguesas dobles fue: ",contD)
  print("El total de hamburguesas triples fue: ",contT)
print("---------------------------")
print("EL TOTAL DEL PEDIDO FUE: ", sum(valorP)) 
print("---------------------------")
print("Gracias por ordenar")
print("---------------------------")