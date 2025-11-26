# ui.py
import services
from utils import pedir_data, validar_status

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
                print("Usuário cadastrado com sucesso.")
            elif op == "2":
                usuarios = services.listar_usuarios()
                if not usuarios:
                    print("Não há usuários cadastrados.")
                else:
                    for i, u in enumerate(usuarios, 1):
                        print(f"{i}. {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")
            elif op == "3":
                termo = input("Digite nome ou email para busca: ").strip()
                encontrados = services.buscar_usuarios(termo)
                if not encontrados:
                    print("Nenhum usuário encontrado.")
                else:
                    for u in encontrados:
                        print(f"- {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")
            elif op == "4":
                email = input("Email do usuário a atualizar: ").strip()
                print("[1] Nome [2] Email [3] Perfil")
                esc = input("Escolha campo: ").strip()
                campo = {"1": "Nome", "2": "Email", "3": "Perfil"}.get(esc)
                if campo:
                    valor = input("Novo valor: ").strip()
                    updated = services.atualizar_usuario(email, campo, valor)
                    print("Atualizado." if updated else "Usuário não encontrado.")
                else:
                    print("Opção inválida.")
            elif op == "5":
                email = input("Email para remover: ").strip()
                removed = services.remover_usuario(email)
                print("Removido." if removed else "Usuário não encontrado.")
            elif op == "6":
                if input("Tem certeza que deseja remover todos os usuários? (s/n): ").strip().lower() == "s":
                    services.remover_todos_usuarios()
                    print("Todos os usuários foram removidos.")
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

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
                print("Projeto cadastrado com sucesso.")
            elif op == "2":
                projetos = services.listar_projetos()
                if not projetos:
                    print("Não há projetos cadastrados.")
                else:
                    for p in projetos:
                        print(f"- {p.get('nome')} | {p.get('descricao')} | {p.get('data_inicio')} → {p.get('data_fim')}")
            elif op == "3":
                nome = input("Nome do projeto para buscar: ").strip()
                encontrados = services.buscar_projeto(nome)
                if not encontrados:
                    print("Projeto não encontrado.")
                else:
                    for p in encontrados:
                        print(f"- {p.get('nome')} | {p.get('descricao')}")
            elif op == "4":
                nome = input("Nome do projeto a atualizar: ").strip()
                print("[1] Nome [2] Descrição [3] Datas")
                esc = input("Escolha: ").strip()
                if esc == "1":
                    novo = input("Novo nome: ").strip()
                    services.atualizar_projeto(nome, "nome", novo)
                elif esc == "2":
                    nova = input("Nova descrição: ").strip()
                    services.atualizar_projeto(nome, "descricao", nova)
                elif esc == "3":
                    ini = pedir_data("Nova data início (DD/MM/AAAA): ")
                    fim = pedir_data("Nova data fim (DD/MM/AAAA): ")
                    services.atualizar_projeto(nome, "data_inicio", ini)
                    services.atualizar_projeto(nome, "data_fim", fim)
                else:
                    print("Opção inválida.")
            elif op == "5":
                nome = input("Nome do projeto a remover: ").strip()
                removed = services.remover_projeto(nome)
                print("Removido." if removed else "Projeto não encontrado.")
            elif op == "6":
                if input("Tem certeza que deseja remover todos os projetos? (s/n): ").strip().lower() == "s":
                    services.remover_todos_projetos()
                    print("Todos os projetos foram removidos.")
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

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
                    print("Status inválido. Use pendente, andamento ou concluída.")
                prazo = pedir_data("Prazo (DD/MM/AAAA): ")
                services.cadastrar_tarefa(titulo, projeto, responsavel, status, prazo)
                print("Tarefa cadastrada com sucesso.")
            elif op == "2":
                tarefas = services.listar_tarefas()
                if not tarefas:
                    print("Não há tarefas cadastradas.")
                else:
                    for i, t in enumerate(tarefas, 1):
                        print(f"{i}. {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "3":
                proj = input("Nome do projeto: ").strip()
                res = services.buscar_tarefas_por_projeto(proj)
                for t in res:
                    print(f"- {t.get('titulo')} | Responsável: {t.get('responsavel')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "4":
                resp = input("Nome do responsável: ").strip()
                res = services.buscar_tarefas_por_responsavel(resp)
                for t in res:
                    print(f"- {t.get('titulo')} | Projeto: {t.get('projeto')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "5":
                st = input("Status (pendente/andamento/concluída): ").strip().lower()
                res = services.buscar_tarefas_por_status(st)
                for t in res:
                    print(f"- {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Prazo: {t.get('prazo')}")
            elif op == "6":
                titulo = input("Título para atualizar: ").strip()
                print("[1] Título [2] Projeto [3] Responsável [4] Status [5] Prazo")
                esc = input("Escolha: ").strip()
                campo_map = {"1": "titulo", "2": "projeto", "3": "responsavel", "4": "status", "5": "prazo"}
                campo = campo_map.get(esc)
                if campo:
                    if campo == "prazo":
                        valor = pedir_data("Novo prazo (DD/MM/AAAA): ")
                    else:
                        valor = input("Novo valor: ").strip()
                    services.atualizar_tarefa(titulo, campo, valor)
                    print("Atualização aplicada (se a tarefa existe).")
                else:
                    print("Opção inválida.")
            elif op == "7":
                titulo = input("Título para concluir: ").strip()
                ok = services.concluir_tarefa(titulo)
                print("Tarefa marcada como concluída." if ok else "Tarefa não encontrada.")
            elif op == "8":
                titulo = input("Título para reabrir: ").strip()
                ok = services.reabrir_tarefa(titulo)
                print("Tarefa reaberta (pendente)." if ok else "Tarefa não encontrada.")
            elif op == "9":
                titulo = input("Título para remover: ").strip()
                ok = services.remover_tarefa(titulo)
                print("Removida." if ok else "Tarefa não encontrada.")
            elif op == "10":
                if input("Tem certeza que deseja remover todas as tarefas? (s/n): ").strip().lower() == "s":
                    services.remover_todas_tarefas()
                    print("Todas as tarefas foram removidas.")
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("[1] Resumo por projeto (total / por status / % concluídas)")
        print("[2] Produtividade por usuário (tarefas concluídas no período)")
        print("[3] Atrasos (tarefas com prazo vencido e status pendente/andamento)")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                resumo = services.report_summary_by_project()
                if not resumo:
                    print("Não há dados para exibir.")
                else:
                    for r in resumo:
                        print(f"\nProjeto: {r['projeto']}")
                        print(f"  Total de tarefas: {r['total']}")
                        print("  Tarefas por status:")
                        for s, c in r['por_status'].items():
                            print(f"    - {s}: {c}")
                        print(f"  Percentual concluídas: {r['pct_concluidas']:.1f}%")
            elif op == "2":
                inicio = pedir_data("Data início (DD/MM/AAAA): ")
                fim = pedir_data("Data fim (DD/MM/AAAA): ")
                prod = services.productivity_by_user(inicio, fim)
                if not prod:
                    print("Nenhuma tarefa concluída nesse período.")
                else:
                    print("Produtividade por usuário (tarefas concluídas no período):")
                    for user, count in prod.items():
                        print(f"- {user}: {count} tarefa(s) concluída(s)")
            elif op == "3":
                atrasos = services.overdue_tasks()
                if not atrasos:
                    print("Nenhuma tarefa atrasada (prazo vencido e status pendente/andamento).")
                else:
                    print("Tarefas atrasadas (prazo vencido e status pendente/andamento):")
                    for t in atrasos:
                        print(f"- {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Prazo: {t.get('prazo')} | Status: {t.get('status')}")
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)

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
            break
        else:
            print("Opção inválida.")

