# SENTINELA.LOG


#O sistema deve permitir adicionar, visualizar, editar e excluir usuários, com informações como:
#nome, matrícula, perfil (estudante, professor, administrador), horário permitido de acesso (por
#exemplo, das 7h às 18h) e observações.
#O sistema deve também registrar e consultar acessos, com: usuário, data e hora, máquina de
#origem e resultado (sucesso ou falha). Um registro de acesso não pode ser editado depois,
#pensem por quê.
#Ao listar os usuários, as matrículas não devem aparecer por completo na tela. Mostre apenas
#parte delas — por exemplo, os dois primeiros caracteres seguidos de asteriscos. Deve existir uma
#opção específica para revelar uma matrícula.


#registroda = registro de acessos
#registrodus = registro de usuários
#registroaud = registro de ações

#import os
#os.system("cls")
from datetime import datetime

nomes_u =[]
matriculas = []
matriculascen = [] #matriculas censuradas
def censurar_matricula():
    for i in range (len(matriculas)):
        matriculascen.append((matriculas[i])[:2] + "*"*(len(matriculas)-2))
perfis = []
horariopermitidos = []
def horariopermitido(perfil):
    if perfil == "estudante":
        horariopermitido = "7h às 18h" 
    elif perfil == "professor":
        horariopermitido = "7h às 20h"
    elif perfil == "administrador":
        horariopermitido = "7h às 22h"
    return horariopermitido
maquinasda = []

def registrar_usuario():
    while True:
      perfil = input("digite o perfil do usuário a ser registrado ('estudante', 'professor' ou 'administrador'): ")
      if perfil == "estudante" or perfil == "professor" or perfil == "administrador":
          perfis.append(perfil)
          nome = input("digite o nome do usuário: ")
          nomes_u.append (nome)
          matricula = input("digite a matrícula do usuário: ")
          matriculas.append(matricula)
          horariopermitidos.append(horariopermitido(perfil))
                        
          registrodus = open("registrodus.txt", "a")
          registrodus.write(nome + ", " + matricula[:2]+ "*"*((len(list(matricula)))-2) + ", " + perfil + ", " + horariopermitido(perfil) + " \n")
          registrodus.close() #esse registro cria um arquivo .txt com a matricula censurada
          break

      else:
         print("perfil inválido.")

def registrar_acesso(nome_usuario):
    registroda = open("registroda.txt", "a")
    horario_de_acesso = datetime.now()
    nome = nome_usuario
    maquinadeacesso = input("digite a maquina de acesso do usuário: ") 
    maquinasda.append(maquinadeacesso) 
    while True:
           resultado = input("digite o resultado do acesso: ")
           if resultado == "sucesso" or resultado == "falha":
                registroda = open("registroda.txt", "a")
                registroda.write(nome + ", " + str(horario_de_acesso) + ", " + maquinadeacesso + ", " + resultado + " \n")
                registroda.close()
                break
           else:
                print("resultado inválido. digite novamente. ")

def pausar(): 
    input("\nPressione Enter para continuar...")


def mostrar_menu():
    print("=== SentinelaLog ===")
    print("1. Gerenciar usuários")
    print("2. Registrar acesso")
    print("3. Consultar acessos")
    print("4. Alertas de máquinas compartilhadas")
    print("5. Relatório de segurança")
    print("6. Consultar log de auditoria")
    print("7. Funcionalidade extra")
    print("8. Perguntar à IA (em breve)")
    print("0. Sair")


while True:
    print("qual usuário está tentando acessar o programa? ")
    if (len(nomes_u)) > 0:
        print("usuários registrados: ")
        for i in range(len(nomes_u)):
            print(f"{[i+1]}. {nomes_u[i]}")
    usuarioacesso = int(input("digite o número do usuário que deseja acessar o pro grama (ou digite 0, caso deseje registrar um novo usuário): "))

    if usuarioacesso <= (len(nomes_u)):
        if usuarioacesso == 0:
            registrar_usuario()
            nome_usuario = nomes_u[(len(nomes_u)-1)]
            registrar_acesso(nome_usuario)
        else:
            nome_usuario = nomes_u[i-1]
            registrar_acesso(nome_usuario)
    else:
        print("usuario invalido.")
        break
  
    mostrar_menu()
    comando =  int(input("digite de '0' a '8' para selecionar um comando: "))

    if comando == 1:
        #Gerenciar usuários
        print("dps")

    elif comando == 2:
        #Registrar acesso
        registrar_usuario()

    elif comando == 3:
        #Consultar acessos

        #esse metodo le as matriculas censuradas
        registrodus = open("registrodus.txt", "r", encoding="utf8")
        print(registrodus.read())
        registrodus.close() 

    elif comando == 4:
        #Alertas de máquinas compartilhadas
        print("dps")

    elif comando == 5:
        #Relatório de segurança
        print("dps")

    elif comando == 6:
        #Consultar log de auditoria
        print("dps")

    elif comando == 7:
        #Funcionalidade extra
        print("dps")

    elif comando == 8:
        #Perguntar à IA (em breve)
        print("dps")

    elif comando == 0:
        break

    else:
        print("Comando inválido. Tente novamente")
