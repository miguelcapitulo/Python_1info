import services
from utils import pedir_data, validar_status

# USUÁRIOS
def menu_usuarios():
    while True:
        print("\n=== USUÁRIOS ===")
        print("[1] Cadastrar")
        print("[2] Listar")
        print("[3] Buscar por nome ou e-mail")
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
                    print("Nenhum usuário cadastrado.")
                else:
                    for i, u in enumerate(usuarios, 1):
                        print(f"{i}. Nome: {u.get('Nome')} | Email: {u.get('Email')} | Perfil: {u.get('Perfil')}")
            elif op == "3":
                termo = input("Nome ou email para buscar: ").strip()
                achados = services.buscar_usuarios(termo)
                if not achados:
                    print("Nenhum usuário encontrado.")
                else:
                    for u in achados:
                        print(f"- Nome: {u.get('Nome')} | Email: {u.get('Email')} | Perfil: {u.get('Perfil')}")
            elif op == "4":
                email = input("Email do usuário a atualizar: ").strip()
                print("Campos: [1] Nome  [2] Email  [3] Perfil")
                esc = input("Escolha campo: ").strip()
                campo = {"1": "Nome", "2": "Email", "3": "Perfil"}.get(esc)
                if not campo:
                    print("Opção inválida.")
                else:
                    valor = input("Novo valor: ").strip()
                    if services.atualizar_usuario(email, campo, valor):
                        print("Usuário atualizado.")
                    else:
                        print("Usuário não encontrado.")
            elif op == "5":
                email = input("Email para remover: ").strip()
                if services.remover_usuario(email):
                    print("Usuário removido.")
                else:
                    print("Usuário não encontrado.")
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

# PROJETOS
def menu_projetos():
    while True:
        print("\n=== PROJETOS ===")
        print("[1] Cadastrar projeto")
        print("[2] Listar projetos")
        print("[3] Buscar projeto")
        print("[4] Atualizar projeto")
        print("[5] Remover projeto")
        print("[6] Remover TODOS")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                nome = input("Nome do projeto: ").strip()
                descricao = input("Descrição: ").strip()
                ini = pedir_data("Data de início (DD/MM/AAAA): ")
                fim = pedir_data("Data final (DD/MM/AAAA): ")
                services.cadastrar_projeto(nome, descricao, ini, fim)
                print("Projeto cadastrado.")
            elif op == "2":
                projetos = services.listar_projetos()
                if not projetos:
                    print("Nenhum projeto cadastrado.")
                else:
                    for p in projetos:
                        print(f"- Nome: {p.get('nome')} | Descrição: {p.get('descricao')} | Início: {p.get('data_inicio')} | Fim: {p.get('data_fim')}")
            elif op == "3":
                termo = input("Nome do projeto para buscar: ").strip()
                achados = services.buscar_projeto(termo)
                if not achados:
                    print("Nenhum projeto encontrado.")
                else:
                    for p in achados:
                        print(f"- Nome: {p.get('nome')} | Descrição: {p.get('descricao')} | Início: {p.get('data_inicio')} | Fim: {p.get('data_fim')}")
            elif op == "4":
                nome = input("Nome do projeto para atualizar: ").strip()
                print("Campos: [1] Nome  [2] Descrição  [3] Data início  [4] Data fim")
                esc = input("Escolha campo: ").strip()
                if esc == "1":
                    novo = input("Novo nome: ").strip()
                    services.atualizar_projeto(nome, "nome", novo)
                    print("Atualizado.")
                elif esc == "2":
                    nova = input("Nova descrição: ").strip()
                    services.atualizar_projeto(nome, "descricao", nova)
                    print("Atualizado.")
                elif esc == "3":
                    ini = pedir_data("Nova data de início (DD/MM/AAAA): ")
                    services.atualizar_projeto(nome, "data_inicio", ini)
                    print("Atualizado.")
                elif esc == "4":
                    fim = pedir_data("Nova data final (DD/MM/AAAA): ")
                    services.atualizar_projeto(nome, "data_fim", fim)
                    print("Atualizado.")
                else:
                    print("Opção inválida.")
            elif op == "5":
                nome = input("Nome do projeto para remover: ").strip()
                if services.remover_projeto(nome):
                    print("Projeto removido.")
                else:
                    print("Projeto não encontrado.")
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

# TAREFAS
def menu_tarefas():
    while True:
        print("\n=== TAREFAS ===")
        print("[1] Cadastrar tarefa")
        print("[2] Listar todas as tarefas")
        print("[3] Listar tarefas por projeto")
        print("[4] Listar tarefas por responsável")
        print("[5] Listar tarefas por status")
        print("[6] Atualizar tarefa")
        print("[7] Concluir tarefa")
        print("[8] Reabrir tarefa")
        print("[9] Remover tarefa")
        print("[10] Remover TODAS as tarefas")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                titulo = input("Título da tarefa: ").strip()
                projeto = input("Nome do projeto vinculado: ").strip()
                responsavel = input("Nome do responsável: ").strip()
                while True:
                    status = input("Status (pendente / andamento / concluída): ").strip().lower()
                    if validar_status(status):
                        status = status.strip().lower()
                        break
                    print("Status inválido. Use pendente, andamento ou concluída.")
                prazo = pedir_data("Prazo (DD/MM/AAAA): ")
                services.cadastrar_tarefa(titulo, projeto, responsavel, status, prazo)
                print("Tarefa cadastrada.")
            elif op == "2":
                tarefas = services.listar_tarefas()
                if not tarefas:
                    print("Nenhuma tarefa cadastrada.")
                else:
                    for i, t in enumerate(tarefas, 1):
                        print(f"{i}. Título: {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "3":
                proj = input("Nome do projeto: ").strip()
                for t in services.buscar_tarefas_por_projeto(proj):
                    print(f"- Título: {t.get('titulo')} | Responsável: {t.get('responsavel')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "4":
                resp = input("Nome do responsável: ").strip()
                for t in services.buscar_tarefas_por_responsavel(resp):
                    print(f"- Título: {t.get('titulo')} | Projeto: {t.get('projeto')} | Status: {t.get('status')} | Prazo: {t.get('prazo')}")
            elif op == "5":
                st = input("Status (pendente / andamento / concluída): ").strip().lower()
                for t in services.buscar_tarefas_por_status(st):
                    print(f"- Título: {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Prazo: {t.get('prazo')}")
            elif op == "6":
                titulo = input("Título da tarefa para atualizar: ").strip()
                print("Campos: [1] Título  [2] Projeto  [3] Responsável  [4] Status  [5] Prazo")
                esc = input("Escolha campo: ").strip()
                campo = {"1":"titulo","2":"projeto","3":"responsavel","4":"status","5":"prazo"}.get(esc)
                if not campo:
                    print("Opção inválida.")
                else:
                    if campo == "titulo":
                        valor = input("Novo título: ").strip()
                    elif campo == "projeto":
                        valor = input("Novo projeto: ").strip()
                    elif campo == "responsavel":
                        valor = input("Novo responsável: ").strip()
                    elif campo == "status":
                        while True:
                            valor = input("Novo status (pendente / andamento / concluída): ").strip().lower()
                            if validar_status(valor):
                                break
                            print("Status inválido. Use pendente, andamento ou concluída.")
                    elif campo == "prazo":
                        valor = pedir_data("Novo prazo (DD/MM/AAAA): ")
                    services.atualizar_tarefa(titulo, campo, valor)
                    print("Tarefa atualizada (se existia).")
            elif op == "7":
                titulo = input("Título para concluir: ").strip()
                if services.concluir_tarefa(titulo):
                    print("Tarefa marcada como concluída.")
                else:
                    print("Tarefa não encontrada.")
            elif op == "8":
                titulo = input("Título para reabrir: ").strip()
                if services.reabrir_tarefa(titulo):
                    print("Tarefa reaberta (status pendente).")
                else:
                    print("Tarefa não encontrada.")
            elif op == "9":
                titulo = input("Título para remover: ").strip()
                if services.remover_tarefa(titulo):
                    print("Tarefa removida.")
                else:
                    print("Tarefa não encontrada.")
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

# RELATÓRIOS
def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("[1] Resumo por projeto: total de tarefas / por status / % concluídas")
        print("[2] Produtividade por usuário: tarefas concluídas no período")
        print("[3] Atrasos: tarefas com prazo vencido e não concluídas (pendente / andamento)")
        print("[0] Voltar")
        op = input("Escolha: ").strip()
        try:
            if op == "1":
                resumo = services.report_summary_by_project()
                if not resumo:
                    print("Nenhum projeto/tarefa para exibir.")
                else:
                    for r in resumo:
                        print(f"\nProjeto: {r['projeto']}")
                        print(f"  Total de tarefas: {r['total']}")
                        print(f"  Distribuição por status:")
                        for sname, cnt in r['por_status'].items():
                            print(f"    - {sname}: {cnt}")
                        print(f"  Percentual concluídas: {r['pct_concluidas']:.1f}%")
            elif op == "2":
                inicio = pedir_data("Data início do período (DD/MM/AAAA): ")
                fim = pedir_data("Data fim do período (DD/MM/AAAA): ")
                prod = services.productivity_by_user(inicio, fim)
                if not prod:
                    print("Nenhuma tarefa concluída nesse período.")
                else:
                    for user, count in prod.items():
                        print(f"- {user}: {count} tarefas concluídas")
            elif op == "3":
                atrasos = services.overdue_tasks()
                if not atrasos:
                    print("Nenhuma tarefa atrasada (prazo vencido e status pendente/andamento).")
                else:
                    for t in atrasos:
                        print(f"- Título: {t.get('titulo')} | Projeto: {t.get('projeto')} | Responsável: {t.get('responsavel')} | Prazo: {t.get('prazo')} | Status: {t.get('status')}")
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
            break
        else:
            print("Opção inválida.")