import services
from utils import pedir_data, validar_status

#USUÁRIOS

def menu_usuarios():
    while True:
        print("\n=== USUÁRIOS ===")
        print("[1] Cadastrar")
        print("[2] Listar")
        print("[3] Buscar")
        print("[4] Atualizar")
        print("[5] Remover")
        print("[6] Remover TODOS")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                nome = input("Nome: ").strip()
                email = input("Email: ").strip()
                perfil = input("Perfil: ").strip()
                services.cadastrar_usuario(nome, email, perfil)
                print(" Usuário cadastrado.")

            elif op == "2":
                us = services.listar_usuarios()
                if not us:
                    print("Nenhum usuário.")
                else:
                    for i, u in enumerate(us, 1):
                        print(f"{i}. {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")

            elif op == "3":
                termo = input("Nome ou email: ").strip()
                encontrados = services.buscar_usuarios(termo)
                if not encontrados:
                    print("Nenhum encontrado.")
                else:
                    for u in encontrados:
                        print(f"- {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")

            elif op == "4":
                email = input("Email do usuário a atualizar: ").strip()
                print("[1] Nome [2] Email [3] Perfil")
                esc = input("Escolha: ").strip()
                campo_map = {"1": "Nome", "2": "Email", "3": "Perfil"}
                campo = campo_map.get(esc)
                if not campo:
                    print("Opção inválida.")
                else:
                    valor = input("Novo valor: ").strip()
                    if services.atualizar_usuario(email, campo, valor):
                        print("Atualizado.")
                    else:
                        print("Usuário não encontrado.")

            elif op == "5":
                email = input("Email para remover: ").strip()
                if services.remover_usuario(email):
                    print("Removido.")
                else:
                    print("Usuário não encontrado.")

            elif op == "6":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    services.remover_todos_usuarios()
                    print(" Todos removidos.")

            elif op == "0":
                break
            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

# PROJETOS

def menu_projetos():
    while True:
        print("\n=== PROJETOS ===")
        print("[1] Cadastrar")
        print("[2] Listar")
        print("[3] Buscar")
        print("[4] Atualizar")
        print("[5] Remover")
        print("[6] Remover TODOS")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                nome = input("Nome do projeto: ").strip()
                descricao = input("Descrição: ").strip()
                ini = pedir_data("Data início (DD/MM/AAAA): ")
                fim = pedir_data("Data fim (DD/MM/AAAA): ")
                services.cadastrar_projeto(nome, descricao, ini, fim)
                print(" Projeto cadastrado.")

            elif op == "2":
                ps = services.listar_projetos()
                if not ps:
                    print("Nenhum projeto.")
                else:
                    for p in ps:
                        print(f"- {p.get('nome')} | {p.get('descricao')} | {p.get('data_inicio')} → {p.get('data_fim')}")

            elif op == "3":
                nome = input("Nome do projeto: ").strip()
                encontrados = services.buscar_projeto(nome)
                if not encontrados:
                    print("Não encontrado.")
                else:
                    for p in encontrados:
                        print(f"- {p.get('nome')} | {p.get('descricao')}")

            elif op == "4":
                nome = input("Nome do projeto p/ atualizar: ").strip()
                print("[1] Nome [2] Descrição [3] Datas")
                esc = input("Escolha: ").strip()
                if esc == "1":
                    novo = input("Novo nome: ").strip()
                    services.atualizar_projeto(nome, "nome", novo)
                elif esc == "2":
                    nova = input("Nova descrição: ").strip()
                    services.atualizar_projeto(nome, "descricao", nova)
                elif esc == "3":
                    ini = pedir_data("Nova data início: ")
                    fim = pedir_data("Nova data fim: ")
                    services.atualizar_projeto(nome, "data_inicio", ini)
                    services.atualizar_projeto(nome, "data_fim", fim)
                else:
                    print("Opção inválida.")
                print("Atualizado (se existia).")

            elif op == "5":
                nome = input("Nome para remover: ").strip()
                if services.remover_projeto(nome):
                    print("Removido.")
                else:
                    print("Projeto não encontrado.")

            elif op == "6":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    services.remover_todos_projetos()
                    print(" Todos removidos.")

            elif op == "0":
                break
            else:
                print("Opção inválida.")

        except Exception as e:
            print("Erro:", e)

# TAREFAS

def menu_tarefas():
    while True:
        print("\n=== TAREFAS ===")
        print("[1] Cadastrar")
        print("[2] Listar todas")
        print("[3] Listar por projeto")
        print("[4] Listar por responsável")
        print("[5] Listar por status")
        print("[6] Atualizar")
        print("[7] Concluir")
        print("[8] Reabrir")
        print("[9] Remover")
        print("[10] Remover TODAS")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                titulo = input("Título: ").strip()
                projeto = input("Projeto (nome): ").strip()
                responsavel = input("Responsável (nome): ").strip()
                while True:
                    status = input("Status (pendente/andamento/concluída): ").strip().lower()
                    if validar_status(status):
                        break
                    print("Status inválido.")
                prazo = pedir_data("Prazo (DD/MM/AAAA): ")
                services.cadastrar_tarefa(titulo, projeto, responsavel, status, prazo)
                print("Tarefa cadastrada.")

            elif op == "2":
                ts = services.listar_tarefas()
                for i, t in enumerate(ts, 1):
                    print(f"{i}. {t.get('titulo')} | {t.get('projeto')} | {t.get('responsavel')} | {t.get('status')} | {t.get('prazo')}")

            elif op == "3":
                proj = input("Nome do projeto: ").strip()
                for t in services.buscar_tarefas_por_projeto(proj):
                    print(f"- {t.get('titulo')} | {t.get('responsavel')} | {t.get('status')}")

            elif op == "4":
                resp = input("Nome do responsável: ").strip()
                for t in services.buscar_tarefas_por_responsavel(resp):
                    print(f"- {t.get('titulo')} | {t.get('projeto')} | {t.get('status')}")

            elif op == "5":
                st = input("Status: ").strip().lower()
                for t in services.buscar_tarefas_por_status(st):
                    print(f"- {t.get('titulo')} | {t.get('projeto')} | {t.get('responsavel')}")

            elif op == "6":
                titulo = input("Título p/ atualizar: ").strip()
                print("[1] Título [2] Projeto [3] Responsável [4] Status [5] Prazo")
                esc = input("Escolha: ").strip()
                campo_map = {"1": "titulo", "2": "projeto", "3": "responsavel", "4": "status", "5": "prazo"}
                campo = campo_map.get(esc)
                if campo:
                    valor = pedir_data("Novo prazo: ") if campo == "prazo" else input("Novo valor: ").strip()
                    services.atualizar_tarefa(titulo, campo, valor)
                    print("Atualizado (se existe).")
                else:
                    print("Opção inválida.")

            elif op == "7":
                titulo = input("Título p/ concluir: ").strip()
                print("Concluída." if services.concluir_tarefa(titulo) else "Não encontrada.")

            elif op == "8":
                titulo = input("Título p/ reabrir: ").strip()
                print("Reaberta." if services.reabrir_tarefa(titulo) else "Não encontrada.")

            elif op == "9":
                titulo = input("Título p/ remover: ").strip()
                print("Removida." if services.remover_tarefa(titulo) else "Não encontrada.")

            elif op == "10":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    services.remover_todas_tarefas()
                    print(" Todas removidas.")

            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)
            
# RELATÓRIOS

def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("[1] Resumo por projeto")
        print("[2] Produtividade por usuário")
        print("[3] Atrasos")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                resumo = services.report_summary_by_project()
                for r in resumo:
                    print(f"\nProjeto: {r['projeto']}")
                    print(f"  Total tarefas: {r['total']}")
                    for s, c in r['por_status'].items():
                        print(f"    - {s}: {c}")
                    print(f"  % concluídas: {r['pct_concluidas']:.1f}%")

            elif op == "2":
                inicio = pedir_data("Data início (DD/MM/AAAA): ")
                fim = pedir_data("Data fim (DD/MM/AAAA): ")
                prod = services.productivity_by_user(inicio, fim)
                for user, count in prod.items():
                    print(f"- {user}: {count} tarefas concluídas")

            elif op == "3":
                atrasos = services.overdue_tasks()
                for t in atrasos:
                    print(f"- {t['titulo']} | Projeto: {t['projeto']} | Resp: {t['responsavel']} | Prazo: {t['prazo']} | Status: {t['status']}")

            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

# MENU PRINCIPAL

def menu_main():
    while True:
        print("\n===== SISTEMA =====")
        print("[1] Usuários")
        print("[2] Projetos")
        print("[3] Tarefas")
        print("[4] Relatórios")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            menu_usuarios()
        elif op == "2":
            menu_projetos()
        elif op == "3":
            menu_tarefas()
        elif op == "4":
            menu_relatorios()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")