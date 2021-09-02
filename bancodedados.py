import pyrebase

### CONFIGURACAO INICIAL ###
config = {
  "apiKey": "AIzaSyDSUDEozBnAedoc5kgUWA0onSzDXMpZatc",
    "authDomain": "bancodedados-9f6f5.firebaseapp.com",
    "databaseURL": "https://bancodedados-9f6f5-default-rtdb.firebaseio.com",
    "projectId": "bancodedados-9f6f5",
    "storageBucket": "bancodedados-9f6f5.appspot.com",
    "messagingSenderId": "874603841847",
    "appId": "1:874603841847:web:1f9d27f8ffa980d919b2b2"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

## CRUD ##

def criarDado():
  nome = input("Digite o nome: ")
  idade = int(input("Digite idade: "))
  data = {"idade":idade}
  db.child("users").child(nome).set(data)

def updateDado(nome, idadeNova):
  db.child("users").child(nome).update({"idade":idadeNova})

def removeDado(nome):
  db.child("users").child(nome).remove()

def getAllValues():
  return db.child("users").get().val()

def getValuesUser(nome):
  return db.child("users").child(nome).get().val()



## MENU ## 

while(True):
  print("")
  print("BANCO DE DADOS")
  print(" 1 - CRIAR USUARIO ")
  print(" 2 - UPDATE USUARIO ")
  print(" 3 - REMOVE USUARIO ")
  print(" 4 - READ ALL ")
  print(" 5 - READ USUARIO ")
  print(" 0 - FINALIZAR")
  print("")
  opcao = int(input("Escolha a sua opção: "))
  if opcao==0:
    break
  elif opcao==1:
    criarDado()
  elif opcao==2:
    nome = input("Digite o nome do usuario: ")
    idadeNova = int(input("Digite a idade: "))
    updateDado(nome, idadeNova)
  elif opcao==3:
    nome = input("Digite o nome do usuario: ")
    removeDado(nome)
  elif opcao==4:
    print("")
    print(getAllValues())
    print("")
  elif opcao==5:
    print("")
    nome = input("Digite o nome do usuario: ")
    print(getValuesUser(nome))
    print("")
  


