db={}
cont=len(db)
nom=input("ingrese sus nombres: ")
ape=input("ingrese sus apellidos: ")
edad=input("ingrese su edad: ")
id=input("ingrese su id: ")
cont1=len(db)

def creacionUser(nom,ape,edad,id):
  user=dict(nombre=nom, apellido=ape, edad=edad, id=id)
  return user
  
def almacenarEnDb():
    db.update({cont:creacionUser(nom,ape,edad,id)})
    print ("El usuario quedara almacenaod con el codigo: ",cont)
    return db
  
def addUser(cont):
    res=input("quiere agregar otro usuario")
    cont+=1
    while res=="si":
        nom=input("ingrese sus nombres: ")
        ape=input("ingrese sus apellidos: ")
        edad=input("ingrese su edad: ")
        id=input("ingrese su id: ")
        user=dict(nombre=nom, apellido=ape, edad=edad, id=id)
        db.update({cont:user})
        print ("El usuario quedara almacenaod con el codigo: ",cont)
        res=input("quiere agregar otro usuario")
        cont+=1
        
def listarUser(db,cont):
  print("Los usuarios creados son: ")
  contenido = db.values()
  contenido = list(contenido)
  for i in contenido:
    print("cod: ",cont," ",i)
    cont+=1

def buscarUnUser(db):
  res=int(input("Ingrese el codigo de usuario que desea ver: "))
  indice=db [res]
  print("el usuario que llamo fue: ", indice)

def buscarUnUseryModificar(db):
  r=input("Quiere modificar algun valor?: ")
  while r=="si":
    res=int(input("Ingrese el codigo del usuario al que desea acceder: "))
    indice=db [res]
    res2=input("Ingrese el valor que desea modificar: ")
    mod=indice[res2]
    print("El valor: ",res2,"es", mod)
    res3=input("Quiere modificar el valor: (s/n)")
    if res3=="s":
      res4=input("Ingrese el nuevo valor: ")
      modi = { **indice, res2: res4}
      db.update({res:indice, res:modi})
      print("Usuario modificado con exito")
    r=input("Quiere modificar algun otro valor?: ")
  return modi
creacionUser(nom,ape,edad,id)
almacenarEnDb()
addUser(cont)
listarUser(db,cont)
buscarUnUseryModificar(db)
print("La lista fue actualizada:")
listarUser(db,cont)