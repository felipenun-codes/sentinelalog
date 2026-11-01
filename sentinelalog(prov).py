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
perfis = []
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
                        
          registrodus = open("registrodus.txt", "a")
          registrodus.write(nome + ", " + matricula[:2]+ "*"*((len(list(matricula)))-2) + ", " + perfil + ", " + horariopermitido(perfil) + " \n")
          registrodus.close() #esse registro cria um arquivo .txt com a matricula censurada
          break

      else:
         print("perfil inválido.")

def atualizar_registrodus():
    registrodus = open("registrodus.txt", "w")
    for i in range(len(nomes_u)):
        registrodus.write(nomes_u[i] + ", " + matriculas[i][:2]+ "*"*((len(list(matriculas[i])))-2) + ", " + perfis[i] + ", " + horariopermitido(perfis[i]) + " \n")
    registrodus.close()

def visualizar_nomes_u():
    if len(nomes_u) > 0:
        print("\nUsuários registrados: ")
        for i in range(len(nomes_u)):
            print(f"{[i+1]}. {nomes_u[i]}")

def registrar_acesso(nome_usuario):
    horario_de_acesso = datetime.now().replace(microsecond=0)
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

def registrar_operacao(operacao: str, i_usuario):   #registro de auditoria
    horario_de_acesso = datetime.now().replace(microsecond=0)
    for i in range(nomes_u):
        if i == i_usuario:
            registroaud = open("registroaud.txt", "a")
            registroaud.write("Ação: " + str(operacao) + "| Usuário afetado: " + nomes_u[i_usuario] + ", " + str(horario_de_acesso))
            registroaud.close()

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


#MENU:
while True:
    print("qual usuário está tentando acessar o programa? ")
    visualizar_nomes_u()
    usuarioacesso = int(input("digite o número do usuário que deseja acessar o pro grama (ou digite 0, caso deseje registrar um novo usuário): "))

    if usuarioacesso <= (len(nomes_u)):
        if usuarioacesso == 0:
            registrar_usuario()
            nome_usuario = nomes_u[(len(nomes_u)-1)]
            registrar_acesso(nome_usuario)
        else:
            nome_usuario = nomes_u[usuarioacesso-1]
            registrar_acesso(nome_usuario)
    else:
        print("usuario invalido.")
        break
  
    mostrar_menu()
    comando =  int(input("digite de '0' a '8' para selecionar um comando: "))

    if comando == 1:
        #Gerenciar usuários
        print("que ação deseja realizar? ")
        operacao = int(input("1. editar dados de um usuário \n2. excluir usuário \n3. visualizar matricula de um usuário (requer permissão de administrador)"))
        if operacao == 1 or operacao == 2 or operacao == 3:
            visualizar_nomes_u()
            usuario_e = (int(input("digite o numero do usuário afetado: ")))-1
            if usuario_e+1 <= len(nomes_u):
                if operacao == 1:
                    print(nomes_u[usuario_e] + ", " + matriculas[usuario_e][:2]+ "*"*((len(list(matriculas[usuario_e])))-2) + ", " + perfis[usuario_e])
                    editardado = input("qual dado deseja editar? ('nome', 'matrícula' ou 'perfil')")
                    if editardado == "nome":
                        registrar_operacao("editar dados: (mudança de nome)", usuario_e)
                        nome_novo = input("digite o nome novo do usuário: ")
                        nomes_u[usuario_e] = nome_novo
                        atualizar_registrodus()
                    elif editardado == "matricula":
                        registrar_operacao("editar dados: (mudança de matricula)", usuario_e)
                        matricula_nova = input("digite a nova matricula: ")
                        matriculas[usuario_e] = matricula_nova
                        atualizar_registrodus()
                    elif editardado == "perfil":
                        registrar_operacao("editar dados: (mudança de perfil)", usuario_e)
                        perfil_novo = input("digite o perfil novo do usuário: ")
                        perfis[usuario_e] = perfil_novo
                        atualizar_registrodus()
                elif operacao == 2:
                    registrar_operacao("excluir usuário", usuario_e)
                    nomes_u.pop(usuario_e)
                    matriculas.pop(usuario_e)
                    perfis.pop(usuario_e)
                    atualizar_registrodus()
                elif operacao == 3:
                    #TODO: visualizar matricula do usuario (pedindo alguma senha ou coisa do tipo para permitir)
                    print()
                else:
                    print("operação inválida.")
                    break
            elif usuario_e < 0 or usuario_e+1 > len(nomes_u):
                print("usuário inválido.") 
                break           
                    
        else:
            print("ação inválida.")
            break

    elif comando == 2:
        #Registrar usuário
        registrar_usuario()
        registrar_operacao("registro de usuário", (len(nomes_u)-1))

    elif comando == 3:
        #Consultar acessos

        #esse metodo lê as matriculas censuradas
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
