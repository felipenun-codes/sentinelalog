#  #  # SENTINELA.LOG #  #  #

#registroda = registro de acessos
#registrodus = registro de usuários
#registroaud = registro de ações

import os
os.system("cls")
from datetime import datetime
from agente import falar_com_agente

nomes_u =[]      
matriculas = []
perfis = []
def horariopermitido(perfil):         
    if perfil == "estudante":
        horariopermitido = "7h as 18h" 
    elif perfil == "professor":
        horariopermitido = "7h as 20h"
    elif perfil == "administrador":
        horariopermitido = "7h as 22h"
    return horariopermitido
def ran_horariopermitido(perfil):       
    if perfil == "administrador":
        return list(range(7,22))
    elif perfil == "professor":
        return list(range(7, 20))
    else:
        return list(range(7, 18))

maquinasda = []            
contador_falhas = 0       
ultimo_usuario = ""         
hora_do_bloqueio = []       
dia_do_bloqueio = []        
usuarios_bloqueados = []
block = False

def registrar_usuario():    #'registrodus.txt' registra as matriculas ja censuradas
    while True:
      perfil = input("digite o perfil do usuário a ser registrado ('estudante', 'professor' ou 'administrador'): ").lower()
      if perfil == "estudante" or perfil == "professor" or perfil == "administrador":
          nome = input("digite o nome do usuário: ")
          while True:  
            matricula = input("digite a matrícula do usuário: ")
            if len(matricula) == 6:
                break
            else:
                print("matricula inválida. digite uma matricula com 6 digitos.")
        
          perfis.append(perfil)
          nomes_u.append (nome)
          matriculas.append(matricula)
          registro_externo("ext_nomes_u.txt", nome)
          registro_externo("ext_perfis.txt", perfil)
          registro_externo("ext_matriculas.txt", matricula)
                        
          registrodus = open("registrodus.txt", "a", encoding="utf8")
          registrodus.write(nome + ", " + matricula[:2]+ "*"*((len(list(matricula)))-2) + ", " + perfil + ", " + horariopermitido(perfil) + " \n")
          registrodus.close() #esse registro cria um arquivo .txt com a matricula censurada
          break

      else:
         print("perfil inválido.")

def atualizar_registrodus():     #'regstrodus.txt' registra as matriculas ja censuradas
    registrodus = open("registrodus.txt", "w", encoding="utf8")
    for i in range(len(nomes_u)):
        registrodus.write(nomes_u[i] + ", " + matriculas[i][:2]+ "*"*((len(list(matriculas[i])))-2) + ", " + perfis[i] + ", " + horariopermitido(perfis[i]) + " \n")
    registrodus.close()

def visualizar_nomes_u():
    if len(nomes_u) > 0:
        print("\nUsuários registrados: ")
        for i in range(len(nomes_u)):
            print(f"{[i+1]}. {nomes_u[i]}")
    else: 
        print("[nenhum usuário registrado]")

def visualizar_registro_x(registro_txt : str):
    v_registro = open(registro_txt, "r", encoding="utf-8")
    print("\n", v_registro.read())
    v_registro.close()

def registrar_acesso(nome_usuario, resultado: str, risco: str):
    horario_de_acesso = datetime.now().replace(microsecond=0)
    nome = nome_usuario
    maquinadeacesso = input("Digite a maquina de acesso do usuário (ex: pessoal, lab01...): ") 
    maquinasda.append(maquinadeacesso) 
    registroda = open("registroda.txt", "a", encoding="utf-8")
    registroda.write(nome + ", " + str(horario_de_acesso) + ", " + maquinadeacesso + ", Resultado: " + resultado + " | Risco: " + risco + " \n")
    registroda.close()


def senha_acesso(senha_a: str, user_permitido, i_usuario):      #determina sucesso ou falha do acesso
    if user_permitido == nomes_u[i_usuario] and senha_a == "matricula":      #matricula como senha; utilizada para 'Gerenciar usuário'
        for i in range (4):
            senha = input(f"\ndigite a {senha_a} de {user_permitido}: ")
            if senha == matriculas[i_usuario] :
                return True
            else:
                print(f"matricula errada. tente novamente [{3-i} tentativas restantes] ")
        return False   
        
    elif user_permitido == "administrador":
        print("Somente administradores podem acessar essa área!")
        senha = input(f"digite a {senha_a} de {user_permitido}: ")
        if senha != "sentinela":        #senha obviamente provisoria
            return False
        elif senha == "sentinela":       #senha novamente provisoria
            return True

def registrar_operacao(operacao: str, i_usuario, r_usuario):   #registro de auditoria
    horario_de_acesso = datetime.now().replace(microsecond=0)
    if i_usuario == "None":
        registroaud = open("registroaud.txt", "a", encoding="utf8")
        registroaud.write("Ação: " + str(operacao) + "| Usuário responsável: " + str(r_usuario) + ", " + str(horario_de_acesso) + " \n")
        registroaud.close()       
    else:
        for i in range(len(nomes_u)):
            if i == i_usuario:
                registroaud = open("registroaud.txt", "a", encoding="utf8")
                registroaud.write("Ação: " + str(operacao) + "| Usuário afetado: " + nomes_u[i_usuario] + "| Usuário responsável: " + str(r_usuario) + ", " + str(horario_de_acesso) + " \n")
                registroaud.close()

def mostrar_menu():
    print("=== SentinelaLog ===")
    print("1. Visualizar usuários")
    print("2. Gerenciar usuários")
    print("3. Registrar usuário")
    print("4. Consultar acessos")
    print("5. Alertas de máquinas compartilhadas")
    print("6. Relatório de segurança")
    print("7. Consultar log de auditoria")
    print("8. Acionar detector de força bruta")
    print("9. Perguntar à IA (em breve)")
    print("0. Sair")

def registro_externo(registro_ext: str, armazenavel):        #'ext_nomes_u.txt'; 'ext_matriculas.txt'; 'ext_perfis.txt'; "ext_cont_falhas.txt"; "ext_usuarios_bloqueados.txt";
    if os.path.isfile(registro_ext):
        registroexterno = open(registro_ext, "a", encoding="utf8")
        registroexterno.write("," + armazenavel)       #"," será o parâmetro do 'split()'
    else:
        registroexterno = open(registro_ext, "a", encoding="utf8")
        registroexterno.write(armazenavel)
    registroexterno.close()

def externo_interno(registro_ext: str):
    registroexterno = open(registro_ext, "r", encoding="utf8")
    lista = (registroexterno.read()).split(",")             #não sei se preciso retornar essa lista. ela já existe externamente e já está recebendo dados do arquivo, então acho que não?
    registroexterno.close()
    return lista

def contar_falhas():
    global contador_falhas
    contador_falhas +=1
    registro_externo("ext_cont_falhas.txt", "1")      #sim, eu sei que '1' será escrito e lido como string, as falhas serão readicionadas com (len( .txt).split(","))

if os.path.isfile("ext_nomes_u.txt"):
    nomes_u = externo_interno("ext_nomes_u.txt")
    matriculas = externo_interno("ext_matriculas.txt")
    perfis = externo_interno("ext_perfis.txt")
    if os.path.isfile("ext_cont_falhas.txt"):
        contador_falhas = len(externo_interno("ext_cont_falhas.txt"))
    if os.path.isfile("ext_usuarios_bloqueados.txt"):
        usuarios_bloqueados = externo_interno("ext_usuarios_bloqueados.txt")
    nomes_u = externo_interno("ext_nomes_u.txt")


def ler_maquinas_bloqueadas():       #recebe o perfil do usuario, a hora de acesso, a maquina de origem e o resultado do acesso, devolvendo o nivel de risco (normal,suspeito ou critico) e a lista de motivos.
    if not os.path.exists("maquinas_bloqueadas.txt"):     #se nao existir o arquivo, retorna uma lista vazia
        return []
    maquinas = []            
    with open("maquinas_bloqueadas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().lower()          
            if linha:                              #deixar claro que não adiciona linhas vazias
                maquinas.append(linha)
    return maquinas                                     #retorna a lista de máquinas bloqueadas

def maquina_esta_bloqueada(maquina): 
    return maquina.lower() in ler_maquinas_bloqueadas()   #verifica se a máquina está na lista de máquinas bloqueadas, retornando True ou False

    
          #verifica se a máquina está na lista de máquinas bloqueadas


    ### DEVE SER IMPLEMENTADA EM REGISTRAR ACESSO
def classificar_acesso(perfil,hora,maquina,resultado):        #recebe o perfil do usuario, a hora de acesso, a maquina de origem e o resultado do acesso, devolvendo o nivel de risco (normal,suspeito ou crítico) e a lista de motivos.
    pontos = 0
    motivos = []
    resultado = resultado.lower()
    maquina = maquina.lower()
      
    if resultado == "falha":                                 #se o resultado do acesso for falha, adiciona 1 ponto de risco e registra o motivo
        pontos += 1
        motivos.append("Falha de acesso")
    if maquina_esta_bloqueada(maquina):                 #se a máquina estiver na lista de máquinas bloqueadas, adiciona 3 pontos de risco e registra o motivo
        pontos += 3
        motivos.append("Máquina bloqueada")
    if hora in range(1, 6):                                  #se a hora estiver entre 1h e 6h ,(que no caso seria a madrugada) adiciona 4 pontos de risco e registra o motivo
        pontos += 4
        motivos.append("Acesso de madrugada (1h-5h)")
    elif hora not in ran_horariopermitido(perfil):            #se a hora estiver fora do horário permitido para o perfil do usuário, adiciona 2 pontos de risco e registra o motivo
        pontos += 2
        motivos.append("Acesso fora do horário permitido")
    if pontos <=2:
        nivel_risco = "normal"
    elif pontos >= 3 and pontos <= 6:
        nivel_risco = "suspeito"
    else:
        nivel_risco = "crítico"
    return nivel_risco, motivos

def analisar_acessos_registrados():
    if not os.path.exists("registroda.txt"):
        print("Nenhum acesso registrado.")
        return []

    acessos = []

    with open("registroda.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            parte = linha.split(", ")

            if len(parte) < 4:
                continue

            try:
                str_horario_acesso = parte[1].strip()
                data_acesso = datetime.strptime(str_horario_acesso, "%Y-%m-%d %H:%M:%S")
                hora_acesso = data_acesso.hour

            except ValueError:
                print(f"Formato de data inválido na linha: {linha}")
                continue

            str_nome_acesso = parte[0]
            str_maquina_acesso = parte[2]

            pedacos = parte[3].split(" | ")

            try:
                primeiro = pedacos[0]
                valor = primeiro.split(": ")[1]
                risco = pedacos[1].split(": ")[1]

            except IndexError:
                print(f"Formato de registro inválido na linha: {linha}")
                continue

            acesso = [
                str_nome_acesso,
                hora_acesso,
                str_maquina_acesso,
                valor,
                risco
            ]

            acessos.append(acesso)

    return acessos
            

def mostrar_classificacao_acessos(nivel, motivos):
    print("Nível: ", nivel.upper())
    print("Motivos: ")
    if not motivos:
        print("Nenhum sinal de risco foi encontrado.")
    for motivo in motivos:
        print("-", motivo) 

def avisar_maquina_bloqueada(maquina):
    if maquina_esta_bloqueada(maquina):
        print(f"ALERTA: A máquina '{maquina}' está bloqueada. O acesso a partir desta máquina é considerado de alto risco.")


def detectar_maquinas_compartilhadas(lista_fichas):
    maquinas = []
    usuarios = []

    for ficha in lista_fichas:
        nome_ficha = ficha[0]
        maquina_ficha = ficha[2]

        if maquina_ficha not in maquinas:
            maquinas.append(maquina_ficha)
            usuarios.append([nome_ficha])

        else:
            indice = maquinas.index(maquina_ficha)

            if nome_ficha not in usuarios[indice]:
                usuarios[indice].append(nome_ficha)

    encontrou = False

    for i in range(len(maquinas)):
        usuarios_da_maquina = usuarios[i]

        if len(usuarios_da_maquina) > 1:
            print(f"ALERTA: A máquina '{maquinas[i]}' está sendo utilizada por múltiplos usuários: {', '.join(usuarios_da_maquina)}. Isso pode indicar compartilhamento de máquinas ou uso não autorizado.")

            encontrou = True

    if not encontrou:
        print("Nenhuma máquina compartilhada foi detectada.")

def relatorio_seguranca(lista_fichas):
    if len(lista_fichas) == 0:                       
        print("Nenhum acesso registrado ainda. Não há dados para o relatório.")
        return
    if os.path.exists("acessos_permitidos.txt"):         #apaga os arquivos antigos para não duplicar os conteúdos
        os.remove("acessos_permitidos.txt")
    if os.path.exists("acessos_negados.txt"):
        os.remove("acessos_negados.txt")
    usuario_negados = []
    permitidos = 0                                   
    negados = 0 
    total_acessos = len(lista_fichas)
    print("Total de acessos:", total_acessos)

    for ficha in lista_fichas:                          
        nome = ficha[0]                                  
        hora = ficha[1]
        maquina = ficha[2]
        resultado = ficha[3]
        acessos_permitidos = open("acessos_permitidos.txt", "a", encoding="utf-8")
        acessos_negados = open("acessos_negados.txt", "a", encoding="utf-8")
        if resultado == "sucesso":                       
            acessos_permitidos.write("Nome:" + nome + " | Máquina:" + maquina + " | Horário:" + str(hora) + " \n")
        elif resultado == "falha":
            usuario_negados.append(nome)                 
            acessos_negados.write("Nome:" + nome + " | Máquina:" + maquina + " | Horário:" + str(hora) + " \n")
        acessos_negados.close()
        acessos_permitidos.close()

    verificados = []                                     
    ranking = []
    for usuario in usuario_negados:
        if usuario not in verificados:
            verificados.append(usuario)
            qntd = usuario_negados.count(usuario)
            ranking.append([qntd, usuario])
    ranking.sort()
    ranking.reverse()

    f_rank = open("ranking_negados.txt", "w", encoding="utf-8")
    for i in ranking:
        f_rank.write("Usuário:" + i[1] + " | Acessos negados:" + str(i[0]) + "\n")
    f_rank.close()

    # --- horários com mais movimento e acessos de risco ---
    contagem_horas = [0] * 24          # posição 0 = 0h, posição 1 = 1h, ... posição 23 = 23h
    suspeitos = 0
    criticos = 0

    for ficha in lista_fichas:
        hora = ficha[1]
        risco = ficha[4].lower()
        contagem_horas[hora] += 1      #soma 1 no contador daquela hora
        if risco == "suspeito":
            suspeitos += 1
        elif risco == "crítico" or risco == "critico":
            criticos += 1

    maior = max(contagem_horas)       
     
    print("\nAcessos permitidos:", permitidos)
    print("Acessos negados:", negados)

    print("\nUsuário(s) com mais falhas:")
    if len(ranking) == 0:
        print("Nenhum usuário apresentou falhas.")
    else:
        maior_falhas = ranking[0][0]           # o ranking está em ordem decrescente, então o primeiro é o maior
        for i in ranking:
            if i[0] == maior_falhas:           # se houver empate, mostra todos
                print(f"- {i[1]}: {i[0]} falha(s)") 

    print("\nHorário(s) com mais movimento:")
    for h in range(24):
        if contagem_horas[h] == maior:     
            print(f"- {h}h às {h+1}h:com {maior} acesso(s), sendo o horário de maior acesso")
    print("\nAcessos suspeitos:", suspeitos)
    print("Acessos críticos:", criticos)

    f_horarios = open("horarios_movimento.txt", "w", encoding="utf-8")
    f_horarios.write("Acessos por horário:\n")
    for h in range(24):
        if contagem_horas[h] > 0:
            f_horarios.write(str(h) + "h às " + str(h+1) + "h: " + str(contagem_horas[h]) + " acesso(s)\n")

    f_horarios.write("\nHorário(s) com mais movimento:\n")
    for h in range(24):
        if contagem_horas[h] == maior:
            f_horarios.write(str(h) + "h às " + str(h+1) + "h: " + str(maior) + " acesso(s)\n")
    f_horarios.close()

def detectar_forca_bruta(lista_fichas):
    if len(lista_fichas) == 0:
        print("Nenhum acesso registrado para análise.")
        return

    usuarios_rastreados = []
    falhas_consecutivas = []
    alertas_emitidos = []

    for ficha in lista_fichas:
        nome = ficha[0]
        resultado = ficha[3].lower()

        if nome not in usuarios_rastreados:
            usuarios_rastreados.append(nome)
            falhas_consecutivas.append(0)

        idx = usuarios_rastreados.index(nome)

        if resultado == "falha":
            falhas_consecutivas[idx] += 1
            if falhas_consecutivas[idx] >= 3 and nome not in alertas_emitidos:
                alertas_emitidos.append(nome)
        elif resultado == "sucesso":
            falhas_consecutivas[idx] = 0

    print("\n=== Detector de Força Bruta (Análise Histórica do Log) ===")
    if len(alertas_emitidos) > 0:
        for usuario in alertas_emitidos:
            print(f"ALERTA DE FORÇA BRUTA: O usuário '{usuario}' registrou 3 ou mais falhas consecutivas no histórico de acessos (mesmo que intercaladas com outros usuários).")
    else:
	    print("Nenhuma sequência de 3 ou mais falhas seguidas por usuário foi detectada no log.")

def ia():
    while True:
                arquivo = "registrodus.txt"
                arquivo2 = "registroda.txt"
                sistema = "SentinelaLog"
                pergunta = input("\nCaso deseje sair, digite 'sair'.\nCaso contrário faça sua pergunta para a IA > ").strip()
                if pergunta.lower() == "sair":
                    break
                falar_com_agente(arquivo, arquivo2, pergunta, sistema)

def fim_ou_reinicio():
    global reinicio
    while True:
        escolha = input("\nO que você deseja fazer agora?\n1. Reiniciar o programa\n2. Encerrar o programa\n\nDigite uma opção: ")
        if escolha == "1":
            reinicio = True
            break
        elif escolha == "2":
            print("\nEncerrando o programa. Até logo!")
            reinicio = False
            break
        else:
            print("\nOpção inválida.")
    

        

#MENU:
while True:
    block = False
    print("Qual usuário está tentando selecionar o programa? ")
    visualizar_nomes_u()
    usuarioacesso = int(input("Digite o número do usuário que deseja acessar o programa (ou digite 0, caso deseje registrar um novo usuário): "))

    if usuarioacesso <= (len(nomes_u)):
        if usuarioacesso == 0:
            registrar_usuario()
            nome_usuario = nomes_u[(len(nomes_u)-1)]
        else:
            nome_usuario = nomes_u[usuarioacesso-1]
            if not senha_acesso("matricula", nome_usuario, usuarioacesso-1):
                    registrar_acesso(nome_usuario, "falha", "suspeito")
                    print("\nMatrícula incorreta. Acesso negado.")
                    continue
    else:
        print("\nUsuário invalido.\n\n")
        continue

    for i in range (len(nomes_u)):          
        if nome_usuario == nomes_u[i]:
            if datetime.now().hour not in (ran_horariopermitido(perfis[i])):
                registrar_acesso(nome_usuario, "falha", "suspeito")
                print("\nFora do horário de acesso permitido. Acesso negado.\n ")
                block = True
            break

    if len(usuarios_bloqueados) >= 1:
        for i in range (len(usuarios_bloqueados)):
            if nome_usuario == usuarios_bloqueados[i] and (datetime.now().hour >= (hora_do_bloqueio[i]+2) or datetime.now().day > dia_do_bloqueio[i]):
                usuarios_bloqueados.pop(i)
                hora_do_bloqueio.pop(i)
                dia_do_bloqueio.pop(i)
            elif nome_usuario == usuarios_bloqueados[i] and datetime.now().hour < (hora_do_bloqueio[i]+2):
                print("O acesso desse usuário está bloqueado. Tente novamente mais tarde.")
                registrar_acesso(nome_usuario, "falha", "bloqueado pelo sistema")
                block = True
    if block:
        break


    if nome_usuario != ultimo_usuario:
        contador_falhas = 0
        if os.path.isfile("ext_cont_falhas.txt"):          #deleta arquivo de armazenamento de falhas
            os.remove("ext_cont_falhas.txt")
        ultimo_usuario = nome_usuario
    elif nome_usuario == ultimo_usuario and contador_falhas > 5:  
        print("SentinelaLog identificou várias tentativas de acesso sucessivas que resultaram em falha. Acesso bloqueado.")
        registrar_acesso(nome_usuario, "falha", "crítico")
        usuarios_bloqueados.append(nome_usuario)
        hora_do_bloqueio.append(datetime.now().hour)
        dia_do_bloqueio.append(datetime.now().day)
        registro_externo("ext_usuarios_bloqueados.txt",nome_usuario)
        continue
    ultimo_usuario = nome_usuario
  
    mostrar_menu()
    comando =  int(input("digite de '0' a '8' para selecionar um comando: "))

    if comando == 1:
        #esse metodo não mostra as matriculas
        registrar_acesso(nome_usuario, "sucesso","normal")
        visualizar_registro_x("registrodus.txt")
        registrar_operacao("vizualizar registro de usuários", "None", nome_usuario)
        

    elif comando == 2:
        #Gerenciar usuários
        print("Que ação deseja realizar? ")
        operacao = int(input("1. editar dados de um usuário \n2. excluir usuário \n3. visualizar matricula de um usuário (requer permissão de administrador)"))
        if operacao == 1 or operacao == 2 or operacao == 3:
            visualizar_nomes_u()
            usuario_e = (int(input("digite o numero do usuário afetado: ")))-1         
            if operacao == 3:
                if senha_acesso("senha", "administrador", usuario_e):
                    print(f"{nomes_u[usuario_e]}, Matrícula: {matriculas[usuario_e]}")
                    registrar_acesso(nome_usuario, "sucesso", "normal")
                    registrar_operacao("visualizar matrícula", usuario_e, nome_usuario)
                else:
                    print("senha incorreta. ")
                    registrar_acesso(nome_usuario, "falha", "suspeito")
                    contar_falhas()
            elif usuario_e+1 <= len(nomes_u):
                if senha_acesso("matricula", nomes_u[usuario_e], usuario_e):       #requer a matricula para mudar qualquer dado do usuário
                    if operacao == 1:
                        registrar_acesso(nome_usuario, "sucesso", "normal")
                        print(nomes_u[usuario_e] + ", " + matriculas[usuario_e][:2]+ "*"*((len(list(matriculas[usuario_e])))-2) + ", " + perfis[usuario_e])
                        editardado = input("qual dado deseja editar? ('nome', 'matrícula' ou 'perfil')").lower()
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
                    else:
                        if contador_falhas >= 3:         
                           contar_falhas()
                           registrar_acesso(nome_usuario, "falha", "suspeito")
                        else:
                            contar_falhas()
                            registrar_acesso(nome_usuario, "falha", "normal")                                                    
                            print("operação inválida.")
                            continue
                else:
                    registrar_acesso(nome_usuario, "falha", "suspeito")     #falhas repetidas da matricula == acesso suspeito registrado
                    contar_falhas()
            else:
                print("usuário inválido.") 
                registrar_acesso(nome_usuario, "falha", "normal")
                contar_falhas
                continue        

    elif comando == 3:
        #Registrar usuário
        registrar_acesso(nome_usuario, "sucesso", "normal")  
        registrar_usuario()
        registrar_operacao("registro de usuário", nomes_u[(len(nomes_u)-1)], nome_usuario)

    elif comando == 4:
        #Consultar acessos
        registrar_acesso(nome_usuario, "sucesso", "normal")          
        visualizar_registro_x("registroda.txt")
        registrar_operacao("consultar acessos", "None", nome_usuario )

    elif comando == 5:
        #Alerta de Máquinas Compartilhadas
        registrar_acesso(nome_usuario, "sucesso", "normal")
        acessos = analisar_acessos_registrados()
        detectar_maquinas_compartilhadas(acessos)
        registrar_operacao("consultar máquinas compartilhadas", "None", nome_usuario)

        
    elif comando == 6:
            #Relatório de segurança
            if not senha_acesso("senha","administrador",usuarioacesso-1):
                print("\nsenha incorreta")
                registrar_acesso(nome_usuario, "falha", "suspeito")
                break
            acessos = analisar_acessos_registrados()
            relatorio_seguranca(acessos)
            # Indentado corretamente dentro do comando 6:
            registrar_operacao(
                "consultar relatório de segurança",
                "None",
                nome_usuario
            )

    elif comando == 7:
        # Consultar log de auditoria
        registrar_acesso(nome_usuario, "sucesso", "normal")
        visualizar_registro_x("registroaud.txt")
        registrar_operacao("consultar auditoria", "None", nome_usuario)
            
    elif comando == 8:
        # Funcionalidade extra
        registrar_acesso(nome_usuario, "sucesso", "normal")
        acessos = analisar_acessos_registrados()  # 1. Carrega os dados do arquivo
        detectar_forca_bruta(acessos)             # 2. Passa os dados para a detecção
        registrar_operacao("consultar detecção de força bruta", "None", nome_usuario) # Funcionalidade extra

    elif comando == 9:
        registrar_acesso(nome_usuario, "sucesso", "normal")
        registrar_operacao("consultar agente IA", "None", nome_usuario)
        ia()

    elif comando == 0:
        break
        

    else:
        print("Comando inválido. Tente novamente")

    fim_ou_reinicio()
    if reinicio:
        continue
    elif reinicio == False:
        break
