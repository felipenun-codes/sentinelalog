import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


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


def ler_opcao():
    try:
        return int(input("\nEscolha uma opção: "))
    except ValueError:
        return -1


def opcao_em_construcao(nome):
    print(f"\n[{nome}] ainda não foi implementado.")
    pausar()


def main():
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = ler_opcao()

        if opcao == 0:
            print("Encerrando o SentinelaLog.")
            break
        elif 1 <= opcao <= 8:
            opcao_em_construcao(f"Opção {opcao}")
        else:
            print("\nOpção inválida.")
            pausar()


if __name__ == "__main__":
    main()