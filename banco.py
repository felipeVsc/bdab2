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
# criar aqui um menu para ficar bonitinho no vídeo


def criarDado(nome,idade):
  nome = input("Digite o nome")
  idade = int(input("digite idade"))
  data = {"idade":idade}
  db.child("users").child(nome).set(data)


for x in range(3):
    nome = input("Digite o nome")
    idade = int(input("digite idade"))
    data = {"idade":idade}
    db.child("users").child(nome).set(data)

db.child("users").child("Taigo").update({"idade":30})
db.child("users").child("Teste").update({"idade":90})

db.child("users").child("Teste").remove()

# CONSULTAS ##

print("KEYS PRINCIPAIS")

keysPrincipais = db.child("admin").shallow().get()

print(keysPrincipais.key())

print("\n")

print("VALORES")

print(db.child("users").get().val())

print("\n")

print("VALORES APENAS DE TAIGO")
taigo = db.child("users").child("Taigo").get()
print(taigo.val())








