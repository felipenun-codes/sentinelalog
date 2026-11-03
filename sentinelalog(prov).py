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

nomes_u =[]       #listas usadas para atualizar e manter o registrodus.txt
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
contador_falhas = 0         #contador de falhas associado a um usuário específico
ultimo_usuario = ""         #variavel para manutenção 
hora_do_bloqueio = 0        # utilizado para travar o sistema

def registrar_usuario():    #'registrodu.txt' registra as matriculas ja censuradas
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

def atualizar_registrodus():     #'regstrodus.txt' registra as matriculas ja censuradas
    registrodus = open("registrodus.txt", "w")
    for i in range(len(nomes_u)):
        registrodus.write(nomes_u[i] + ", " + matriculas[i][:2]+ "*"*((len(list(matriculas[i])))-2) + ", " + perfis[i] + ", " + horariopermitido(perfis[i]) + " \n")
    registrodus.close()

def visualizar_nomes_u():
    if len(nomes_u) > 0:
        print("\nUsuários registrados: ")
        for i in range(len(nomes_u)):
            print(f"{[i+1]}. {nomes_u[i]}")

def visualizar_registro_x(registro_txt : str):
    v_registro = open(registro_txt, "r", encoding="utf8")
    print(v_registro.read())
    v_registro.close()

def registrar_acesso(nome_usuario, resultado: str, risco: str):
    horario_de_acesso = datetime.now().replace(microsecond=0)
    nome = nome_usuario
    maquinadeacesso = input("digite a maquina de acesso do usuário: ") 
    maquinasda.append(maquinadeacesso) 
    registroda = open("registroda.txt", "a")
    registroda.write(nome + ", " + str(horario_de_acesso) + ", " + maquinadeacesso + ", Resultado: " + resultado + " | Risco: " + risco + " \n")
    registroda.close()


def senha_acesso(senha_a: str, user_permitido, i_usuario):      #determina sucesso ou falha do acesso
    senha = input(f"digite a {senha_a} de {user_permitido}: ")
    if user_permitido == nomes_u[i_usuario] and senha_a == "matricula":
        for i in range (4):
            if senha == matriculas[i_usuario]:
                return True
            else:
                print(f"matricula errada. tente novamente [{3-i} tentativas restantes] ")
                if 3 - i < 1:
                    return False   

def registrar_operacao(operacao: str, i_usuario, r_usuario):   #registro de auditoria
    horario_de_acesso = datetime.now().replace(microsecond=0)
    if i_usuario == "None":
        registroaud = open("registroaud.txt", "a")
        registroaud.write("Ação: " + str(operacao) + "| Usuário responsável: " + str(r_usuario) + ", " + str(horario_de_acesso))
        registroaud.close()       
    else:
        for i in range(nomes_u):
            if i == i_usuario:
                registroaud = open("registroaud.txt", "a")
                registroaud.write("Ação: " + str(operacao) + "| Usuário afetado: " + nomes_u[i_usuario] + "| Usuário responsável: " + str(r_usuario) + ", " + str(horario_de_acesso))
                registroaud.close()


def pausar(): 
    input("\nPressione Enter para continuar...")


def mostrar_menu():
    print("=== SentinelaLog ===")
    print("1. Visualizar usuários")
    print("2. Gerenciar usuários")
    print("3. Registrar usuário")
    print("4. Consultar acessos")
    print("5. Alertas de máquinas compartilhadas")
    print("6. Relatório de segurança")
    print("7. Consultar log de auditoria")
    print("8. Funcionalidade extra")
    print("9. Perguntar à IA (em breve)")
    print("0. Sair")


#MENU:
while True:
    print("qual usuário está tentando acessar o programa? ")
    visualizar_nomes_u()
    usuarioacesso = int(input("digite o número do usuário que deseja acessar o pro grama (ou digite 0, caso deseje registrar um novo usuário): "))

    if usuarioacesso <= (len(nomes_u)):   #'nome_usuario' será o registrado como responsável pela ação x no registro de auditoria
        if usuarioacesso == 0:
            registrar_usuario()
            nome_usuario = nomes_u[(len(nomes_u)-1)]
        else:
            nome_usuario = nomes_u[usuarioacesso-1]
    else:
        print("usuario invalido.")
        break

    if nome_usuario == ultimo_usuario and datetime.now().hour <= hora_do_bloqueio + 2:
        print(f"O acesso desse usuário está bloqueado. Tente novamente às {hora_do_bloqueio + 2}h.")
        break

    if nome_usuario != ultimo_usuario:
        contador_falhas = 0
        ultimo_usuario = nome_usuario
    elif nome_usuario == ultimo_usuario and contador_falhas > 5:        #esse método deixa uma brecha na identificação de falhas. um sujeito mal intencionado pode mudar usuários para resetar o contador_falhas. como proposta de solução, poderíamos implementar algo com datetime para limitar acesso por determinado período de tempo  
        print("SentinelaLog identificou várias tentativas de acesso sucessivas que resultaram em falha. Acesso bloqueado.")
        registrar_acesso(nome_usuario, "falha", "crítico")
        hora_do_bloqueio = datetime.now().hour
        break
    ultimo_usuario = nome_usuario
  
    mostrar_menu()
    comando =  int(input("digite de '0' a '8' para selecionar um comando: "))

    if comando == 1:
        #esse metodo não mostra as matriculas
        visualizar_registro_x("registrodus.txt")
        registrar_operacao("vizualizar registro de usuários", "None", nome_usuario)

    elif comando == 2:
        #Gerenciar usuários
        print("que ação deseja realizar? ")
        operacao = int(input("1. editar dados de um usuário \n2. excluir usuário \n3. visualizar matricula de um usuário (requer permissão de administrador)"))
        if operacao == 1 or operacao == 2 or operacao == 3:
            visualizar_nomes_u()
            usuario_e = (int(input("digite o numero do usuário afetado: ")))-1
            if usuario_e+1 <= len(nomes_u):
                if senha_acesso("matricula", nomes_u[usuario_e], usuario_e):       #requer a matricula para mudar qualquer dado do usuário
                    if operacao == 1:
                        registrar_acesso(nome_usuario, "sucesso", "normal")
                        print(nomes_u[usuario_e] + ", " + matriculas[usuario_e][:2]+ "*"*((len(list(matriculas[usuario_e])))-2) + ", " + perfis[usuario_e])
                        editardado = input("qual dado deseja editar? ('nome', 'matrícula' ou 'perfil')")
                        if editardado == "nome":
                            registrar_operacao("editar dados: (mudança de nome)", usuario_e, nome_usuario)
                            nome_novo = input("digite o nome novo do usuário: ")
                            nomes_u[usuario_e] = nome_novo
                            atualizar_registrodus()
                        elif editardado == "matricula":
                            registrar_operacao("editar dados: (mudança de matricula)", usuario_e, nome_usuario)
                            matricula_nova = input("digite a nova matricula: ")
                            matriculas[usuario_e] = matricula_nova
                            atualizar_registrodus()
                        elif editardado == "perfil":
                            registrar_operacao("editar dados: (mudança de perfil)", usuario_e, nome_usuario)
                            perfil_novo = input("digite o perfil novo do usuário: ")
                            perfis[usuario_e] = perfil_novo
                            atualizar_registrodus()
                    elif operacao == 2:
                        registrar_acesso(nome_usuario, "sucesso", "normal")
                        registrar_operacao("excluir usuário", usuario_e, nome_usuario)
                        nomes_u.pop(usuario_e)
                        matriculas.pop(usuario_e)
                        perfis.pop(usuario_e)
                        atualizar_registrodus()
                    elif operacao == 3:
                        registrar_acesso(nome_usuario, "sucesso", "normal")
                        #TODO: visualizar matricula do usuario (pedindo alguma senha ou coisa do tipo para permitir)
                        print()
                    else:
                        if contador_falhas >= 3:            #VALORES DECIDIDOS ARBITRARIAMENTE
                            contador_falhas =+1
                            registrar_acesso(nome_usuario, "falha", "suspeito")
                        else:
                            contador_falhas =+1
                            registrar_acesso(nome_usuario, "falha", "normal")                                                    
                        print("operação inválida.")
                        break
                elif not senha_acesso("matricula", nomes_u[usuario_e], usuario_e):
                    registrar_acesso(nome_usuario, "falha", "suspeito")     #falhas repetidas da matricula == acesso suspeito registrado
                    contador_falhas =+1
            elif usuario_e < 0 or usuario_e+1 > len(nomes_u):
                print("usuário inválido.") 
                break           

    elif comando == 3:
        #Registrar usuário
        registrar_acesso(nome_usuario, "sucesso", "normal")     #não acho q seja necessario implementar senha pra isso
        registrar_usuario()
        registrar_operacao("registro de usuário", (len(nomes_u)-1), nome_usuario)

    elif comando == 4:
        #Consultar acessos
        registrar_acesso(nome_usuario, "sucesso", "normal")         #podemos implementar senha es quiserem    
        visualizar_registro_x("registroda.txt")
        registrar_operacao("consultar acessos", "None", nome_usuario )

    elif comando == 5:
        #Alertas de máquinas compartilhadas
        print("dps")

    elif comando == 6:
        #Relatório de segurança
        print("dps")

    elif comando == 7:
        #Consultar log de auditoria
        registrar_acesso(nome_usuario, "sucesso", "normal")        #podemos implementar senha se quiserem
        visualizar_registro_x("registroaud.txt")
        registrar_operacao("consultar auditoria", "None", nome_usuario)

    elif comando == 8:
        #Funcionalidade extra
        print("dps")

    elif comando == 9:
        #Perguntar à IA (em breve)
        print("dps")

    elif comando == 0:
        break

    else:
        print("Comando inválido. Tente novamente")
