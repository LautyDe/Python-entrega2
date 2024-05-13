users = {'lautaro': '123456', 'matias': '257983'}

def create_user():
  username = input("Ingrese su nombre de usuario: ")
  password = input("Ingrese su contrasenia: ")
  users[username] = password
  print("Usuario guardado con exito")

def see_users():
  for user, password in users.items():
    print(f"Usuario: {user}, password: {password}")

def login(username, password):
  attempts = 3
  while attempts > 0:
    if username not in users or users[username] != password:
       print("Usuario o contraseña incorrectos.")
       attempts -= 1
       if attempts == 0:
        print("Has excedido el número de intentos permitidos.")
        return False
       username = input("Ingrese su nombre de usuario: ")
       password = input("Ingrese su contraseña: ")
    else:
      return True
    


def main():
  opcion = ''
  while(opcion != 'd'):
    print("Seleccione A para agregar un usuario\nSeleccione B para ver los usuarios\nSeleccione C para loguearse\nSeleccione D para finalizar")
    opcion = input("Ingrese la opcion seleccionada: ").capitalize()

    if(opcion == 'A'):
      create_user()
    elif(opcion == 'B'):
      see_users()
    elif(opcion == 'C'):
      username = input("Ingrese su nombre de usuario: ")
      password = input("Ingrese su contrasenia: ")
      if not login(username, password):
        print("Credenciales invalidas, cerrando ejecucion")
        break
      else :
        print("Logueo completo!")
        break
    elif(opcion == 'D'):
      print("Hasta pronto!")
      break
    else:
      print("Opcion invalida, por favor ingrese una correcta")


main()
