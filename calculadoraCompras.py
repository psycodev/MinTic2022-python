cantidadPan= int(input("Cuantos panes quieres llevar: "))
cantidadLeche= int(input("Cuantas bolsas de leche quieres llevar: "))
cantidadHuevo= int(input("Cuantos huevos quieres llevar: "))
iva=input("ingrese el iva: ")

def panes():
  precioPan=(300)
  totalPan=0
  for i in range (cantidadPan):
    totalPan=precioPan+totalPan
  return(int(totalPan))

def leche():
  precioLeche=(3300)
  totalLeche=0
  for i in range (cantidadLeche):
    totalLeche=precioLeche+totalLeche
  return(int(totalLeche))

def huevo():
  precioHuevo=(350)
  totalHuevo=0
  for i in range (cantidadHuevo):
    totalHuevo=precioHuevo+totalHuevo
  return(int(totalHuevo))

def totalCompra():
  precio=panes()+leche()+huevo()
  return(int(precio))

def vueltas():
    precioTotal=totalConIva()
    billete=int(input("Con cuanto dinero vas a pagar: "))
    while billete<totalConIva():
      restante=precioTotal-billete  
      print("No te alcanza para pagar, te falta ", restante,"por favor ingrese una cantidad mayor")
      billete=int(input("Con cuanto dinero vas a pagar: "))
    if billete>totalConIva():
      vuelta=billete-precioTotal
    elif billete==totalConIva():
      vuelta=0
    return(int(vuelta))

def calIva(iva):
  if iva==(""):
    iva=int(19)
    ivaF=(totalCompra()*iva)//100
  else:
    ivaF=(totalCompra()*int(iva))//100
  return (ivaF)

def totalConIva():
    total=calIva(iva)+totalCompra() 
    return(total)   


print("LLevas: ", panes(),"de pan")
print("LLevas: ", leche(),"de leche")
print("LLevas: ", huevo(),"de huevo")
print("El total de la compra sin iva es: ",totalCompra())
print("el iva de esta compra es: ",calIva(iva))
print("El total de la compra con iva es: ",totalConIva())
print("Tus vueltas son: ",vueltas())