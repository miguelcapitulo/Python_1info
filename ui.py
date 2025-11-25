import services
from utils import pedir_data, validar_status

#USUÁRIOS
def menu_usuarios():
    while True:
        print("\nMENU DE USUÁRIOS")
        print("[1] Cadastrar novo usuário")
        print("[2] Listar todos os usuários")
        print("[3] Buscar usuário por nome ou e-mail")
        print("[4] Atualizar dados de usuário")
        print("[5] Remover usuário")
        print("[6] Remover todos os usuários")
        print("[0] Voltar ao menu anterior")

        op = input("Escolha uma opção: ").strip()
        try:
            if op == "1":
                nome = input("Informe o nome do usuário: ").strip()
                email = input("Informe o e-mail: ").strip()
                perfil = input("Informe o perfil (adm/comum): ").strip()
                services.cadastrar_usuario(nome, email, perfil)
                print("Usuário cadastrado com sucesso.")
            elif op == "2":
                usuarios = services.listar_usuarios()
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                for u in usuarios:
                    print(f"Nome: {u.get('Nome')} | Email: {u.get('Email')} | Perfil: {u.get('Perfil')}")

            elif op == "3":
                termo = input("Digite um nome ou e-mail para buscar: ").strip()
                encontrados = services.buscar_usuarios(termo)
                if not encontrados:
                    print("Nenhum usuário encontrado.")
                for u in encontrados:
                    print(f"Nome: {u.get('Nome')} | Email: {u.get('Email')} | Perfil: {u.get('Perfil')}")

            elif op == "4":
                email = input("Informe o e-mail do usuário a ser atualizado: ").strip()
                print("[1] Nome | [2] Email | [3] Perfil")
                campo = {"1": "Nome", "2": "Email", "3": "Perfil"}.get(input("Escolha o campo: ").strip())
                if campo:
                    valor = input("Informe o novo valor: ").strip()
                    services.atualizar_usuario(email, campo, valor)
                    print("Dados atualizados.")

            elif op == "5":
                email = input("Informe o e-mail do usuário a ser removido: ").strip()
                services.remover_usuario(email)
                print("Usuário removido.")

            elif op == "6":
                if input("Tem certeza que deseja remover TODOS os usuários? (s/n): ").lower() == "s":
                    services.remover_todos_usuarios()
                    print("Todos os usuários foram removidos.")

            elif op == "0":
                break
            
            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

#PROJETOS
def menu_projetos():
    while True:
        print("\nMENU DE PROJETOS")
        print("[1] Cadastrar projeto")
        print("[2] Listar projetos")
        print("[3] Buscar projeto")
        print("[4] Atualizar projeto")
        print("[5] Remover projeto")
        print("[6] Remover todos os projetos")
        print("[0] Voltar ao menu anterior")

        op = input("Escolha uma opção: ").strip()
        try:
            if op == "1":
                nome = input("Informe o nome do projeto: ")
                descricao = input("Informe uma breve descrição: ")
                ini = pedir_data("Informe a data de início (DD/MM/AAAA): ")
                fim = pedir_data("Informe a data de término (DD/MM/AAAA): ")
                services.cadastrar_projeto(nome, descricao, ini, fim)
                print("Projeto cadastrado com sucesso.")

            elif op == "2":
                projetos = services.listar_projetos()
                if not projetos:
                    print("Nenhum projeto cadastrado.")
                for p in projetos:
                    print(f"Nome: {p.get('nome')} | Descrição: {p.get('descricao')} | "
                          f"Período: {p.get('data_inicio')} até {p.get('data_fim')}")

            elif op == "3":
                nome = input("Digite o nome do projeto para buscar: ").strip()
                encontrados = services.buscar_projeto(nome)
                if not encontrados:
                    print("Nenhum projeto encontrado.")
                for p in encontrados:
                    print(f"Nome: {p.get('nome')} | Descrição: {p.get('descricao')}")

            elif op == "4":
                nome = input("Informe o nome do projeto a ser atualizado: ")
                print("[1] Nome | [2] Descrição | [3] Datas")
                escolha = input("Escolha o campo a ser atualizado: ")

                if escolha == "1":
                    services.atualizar_projeto(nome, "nome", input("Novo nome: "))
                elif escolha == "2":
                    services.atualizar_projeto(nome, "descricao", input("Nova descrição: "))
                elif escolha == "3":
                    ini = pedir_data("Nova data de início: ")
                    fim = pedir_data("Nova data de término: ")
                    services.atualizar_projeto(nome, "data_inicio", ini)
                    services.atualizar_projeto(nome, "data_fim", fim)
                print("Projeto atualizado.")

            elif op == "5":
                services.remover_projeto(input("Informe o nome do projeto a ser removido: "))
                print("Projeto removido.")

            elif op == "6":
                if input("Tem certeza que deseja remover TODOS os projetos? (s/n): ").lower() == "s":
                    services.remover_todos_projetos()
                    print("Todos os projetos foram removidos.")

            elif op == "0":
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

#TAREFAS
def menu_tarefas():
    while True:
        print("\nMENU DE TAREFAS")
        print("[1] Cadastrar tarefa")
        print("[2] Listar todas as tarefas")
        print("[3] Listar por projeto")
        print("[4] Listar por responsável")
        print("[5] Listar por status")
        print("[6] Atualizar tarefa")
        print("[7] Marcar como concluída")
        print("[8] Reabrir tarefa")
        print("[9] Remover tarefa")
        print("[10] Remover todas as tarefas")
        print("[0] Voltar ao menu anterior")

        op = input("Escolha uma opção: ").strip()
        try:
            if op == "1":
                titulo = input("Título da tarefa: ")
                projeto = input("Nome do projeto: ")
                responsavel = input("Nome do responsável: ")
                while True:
                    status = input("Status (pendente, andamento, concluída): ").lower()
                    if validar_status(status):
                        break
                    print("Status inválido. Tente novamente.")
                prazo = pedir_data("Prazo (DD/MM/AAAA): ")
                services.cadastrar_tarefa(titulo, projeto, responsavel, status, prazo)
                print("Tarefa cadastrada com sucesso.")

            elif op == "2":
                tarefas = services.listar_tarefas()
                if not tarefas:
                    print("Nenhuma tarefa cadastrada.")
                for t in tarefas:
                    print(f"{t.get('titulo')} | Projeto: {t.get('projeto')} | "
                          f"Responsável: {t.get('responsavel')} | Status: {t.get('status')} | "
                          f"Prazo: {t.get('prazo')}")

            elif op == "3":
                projeto = input("Nome do projeto: ")
                for t in services.buscar_tarefas_por_projeto(projeto):
                    print(f"{t.get('titulo')} | Responsável: {t.get('responsavel')}")

            elif op == "4":
                resp = input("Nome do responsável: ")
                for t in services.buscar_tarefas_por_responsavel(resp):
                    print(f"{t.get('titulo')} | Projeto: {t.get('projeto')}")

            elif op == "5":
                status = input("Informe o status: ")
                for t in services.buscar_tarefas_por_status(status):
                    print(f"{t.get('titulo')} | Projeto: {t.get('projeto')}")

            elif op == "6":
                titulo = input("Título da tarefa a ser atualizada: ")
                print("[1] Título | [2] Projeto | [3] Responsável | [4] Status | [5] Prazo")
                campo = {"1": "titulo", "2": "projeto", "3": "responsavel", "4": "status", "5": "prazo"} \
                    .get(input("Escolha o campo: "))
                if campo:
                    valor = pedir_data("Novo prazo: ") if campo == "prazo" else input("Novo valor: ")
                    services.atualizar_tarefa(titulo, campo, valor)
                    print("Tarefa atualizada.")

            elif op == "7":
                services.concluir_tarefa(input("Título da tarefa: "))
                print("Tarefa marcada como concluída.")

            elif op == "8":
                services.reabrir_tarefa(input("Título da tarefa: "))
                print("Tarefa reaberta.")

            elif op == "9":
                services.remover_tarefa(input("Título da tarefa: "))
                print("Tarefa removida.")

            elif op == "10":
                if input("Tem certeza que deseja remover TODAS as tarefas? (s/n): ").lower() == "s":
                    services.remover_todas_tarefas()
                    print("Todas as tarefas foram removidas.")

            elif op == "0":
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

#RELATÓRIOS
def menu_relatorios():
    while True:
        print("\n=== MENU DE RELATÓRIOS ===")
        print("[1] Resumo por projeto")
        print("[2] Produtividade por usuário")
        print("[3] Tarefas atrasadas")
        print("[0] Voltar ao menu anterior")

        op = input("Escolha uma opção: ").strip()
        try:
            if op == "1":
                relatorios = services.report_summary_by_project()
                if not relatorios:
                    print("Nenhum projeto encontrado ou sem tarefas cadastradas.")
                for r in relatorios:
                    print(f"\nProjeto: {r['projeto']}")
                    print(f"Total de tarefas: {r['total']}")
                    for s, c in r['por_status'].items():
                        print(f"  - {s}: {c}")
                    print(f"Percentual de concluídas: {r['pct_concluidas']:.1f}%")

            elif op == "2":
                inicio = pedir_data("Informe a data de início (DD/MM/AAAA): ")
                fim = pedir_data("Informe a data de término (DD/MM/AAAA): ")
                produtividades = services.productivity_by_user(inicio, fim)
                if not produtividades:
                    print("Nenhuma tarefa concluída no período informado.")
                for usuario, total in produtividades.items():
                    print(f"{usuario}: {total} tarefa(s) concluída(s)")

            elif op == "3":
                atrasadas = services.overdue_tasks()
                if not atrasadas:
                    print("Nenhuma tarefa atrasada encontrada.")
                for t in atrasadas:
                    print(f"{t.get('titulo')} | Projeto: {t.get('projeto')} | "
                          f"Responsável: {t.get('responsavel')} | Prazo: {t.get('prazo')} | "
                          f"Status: {t.get('status')}")

            elif op == "0":
                break

            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

#MENU PRINCIPAL
def menu_main():
    while True:
        print("\nSISTEMA DE GERENCIAMENTO")
        print("[1] Usuários")
        print("[2] Projetos")
        print("[3] Tarefas")
        print("[4] Relatórios")
        print("[0] Sair")

        op = input("Escolha uma opção: ").strip()

        if op == "1":
            menu_usuarios()
        elif op == "2":
            menu_projetos()
        elif op == "3":
            menu_tarefas()
        elif op == "4":
            menu_relatorios()
        elif op == "0":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida.")