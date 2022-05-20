cantidadPan= int(input("Cuantos panes quieres llevar: "))
cantidadLeche= int(input("Cuantas bolsas de leche quieres llevar: "))
cantidadHuevo= int(input("Cuantos huevos quieres llevar: "))

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
    precioTotal=totalCompra()
    billete=int(input("Con cuanto dinero vas a pagar: "))
    while billete<totalCompra():
      restante=precioTotal-billete  
      print("No te alcanza para pagar, te falta ", restante,"por favor ingrese una cantidad mayor")
      billete=int(input("Con cuanto dinero vas a pagar: "))
    if billete>totalCompra():
      vuelta=billete-precioTotal
    elif billete==totalCompra():
      vuelta=0
    return(int(vuelta))

print("LLevas: ", panes(),"de pan")
print("LLevas: ", leche(),"de leche")
print("LLevas: ", huevo(),"de huevo")
print("El total de la compra es: ",totalCompra())
print("Tus vueltas son: ",vueltas())