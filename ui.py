# ui.py
from services import (
    listar_usuarios, cadastrar_usuario, buscar_usuarios, atualizar_usuario,
    remover_usuario, remover_todos_usuarios,
    listar_projetos, cadastrar_projeto, buscar_projeto, atualizar_projeto, remover_projeto, remover_todos_projetos,
    listar_tarefas, cadastrar_tarefa, buscar_tarefas_por_projeto, buscar_tarefas_por_responsavel, buscar_tarefas_por_status,
    atualizar_tarefa, concluir_tarefa, reabrir_tarefa, remover_tarefa, remover_todas_tarefas
)
from utils import pedir_data, validar_status
import sys

def pause():
    input("\nEnter para continuar...")

# -------- Usuários --------
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
                cadastrar_usuario(nome, email, perfil)
                print("✔ Usuário cadastrado.")
                pause()
            elif op == "2":
                us = listar_usuarios()
                if not us:
                    print("Nenhum usuário.")
                else:
                    for i,u in enumerate(us,1):
                        print(f"{i}. {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")
                pause()
            elif op == "3":
                termo = input("Nome ou email: ").strip()
                encontrados = buscar_usuarios(termo)
                if not encontrados:
                    print("Nenhum encontrado.")
                else:
                    for u in encontrados:
                        print(f"- {u.get('Nome')} | {u.get('Email')} | {u.get('Perfil')}")
                pause()
            elif op == "4":
                email = input("Email do usuário a atualizar: ").strip()
                print("[1] Nome [2] Email [3] Perfil")
                esc = input("Escolha: ").strip()
                campo_map = {"1":"Nome","2":"Email","3":"Perfil"}
                campo = campo_map.get(esc)
                if not campo:
                    print("Opção inválida.")
                else:
                    valor = input("Novo valor(pendente, andamento ou concluído): ").strip()
                    if atualizar_usuario(email, campo, valor):
                        print("✔ Atualizado.")
                    else:
                        print("Usuário não encontrado.")
                pause()
            elif op == "5":
                email = input("Email para remover: ").strip()
                if remover_usuario(email):
                    print("✔ Removido.")
                else:
                    print("Usuário não encontrado.")
                pause()
            elif op == "6":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    remover_todos_usuarios()
                    print("✔ Todos removidos.")
                pause()
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)
            pause()

# -------- Projetos --------
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
                cadastrar_projeto(nome, descricao, ini, fim)
                print("✔ Projeto cadastrado.")
                pause()
            elif op == "2":
                ps = listar_projetos()
                if not ps:
                    print("Nenhum projeto.")
                else:
                    for p in ps:
                        print(f"- {p.get('nome')} | {p.get('descricao')} | {p.get('data_inicio')} → {p.get('data_fim')}")
                pause()
            elif op == "3":
                nome = input("Nome do projeto: ").strip()
                encontrados = buscar_projeto(nome)
                if not encontrados:
                    print("Não encontrado.")
                else:
                    for p in encontrados:
                        print(f"- {p.get('nome')} | {p.get('descricao')}")
                pause()
            elif op == "4":
                nome = input("Nome do projeto p/ atualizar: ").strip()
                print("[1] Nome [2] Descrição [3] Datas")
                esc = input("Escolha: ").strip()
                if esc == "1":
                    novo = input("Novo nome: ").strip()
                    atualizar_projeto(nome, "nome", novo)
                elif esc == "2":
                    nova = input("Nova descrição: ").strip()
                    atualizar_projeto(nome, "descricao", nova)
                elif esc == "3":
                    ini = pedir_data("Nova data início: ")
                    fim = pedir_data("Nova data fim: ")
                    atualizar_projeto(nome, "data_inicio", ini)
                    atualizar_projeto(nome, "data_fim", fim)
                else:
                    print("Opção inválida.")
                print("✔ Atualizado (se existia).")
                pause()
            elif op == "5":
                nome = input("Nome para remover: ").strip()
                if remover_projeto(nome):
                    print("✔ Removido.")
                else:
                    print("Projeto não encontrado.")
                pause()
            elif op == "6":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    remover_todos_projetos()
                    print("✔ Todos removidos.")
                pause()
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)
            pause()

# -------- Tarefas --------
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
                cadastrar_tarefa(titulo, projeto, responsavel, status, prazo)
                print("✔ Tarefa cadastrada.")
                pause()
            elif op == "2":
                ts = listar_tarefas()
                if not ts:
                    print("Nenhuma tarefa.")
                else:
                    for i,t in enumerate(ts,1):
                        print(f"{i}. {t.get('titulo')} | {t.get('projeto')} | {t.get('responsavel')} | {t.get('status')} | {t.get('prazo')}")
                pause()
            elif op == "3":
                proj = input("Nome do projeto: ").strip()
                res = buscar_tarefas_por_projeto(proj)
                if not res:
                    print("Nenhuma encontrada.")
                else:
                    for t in res:
                        print(f"- {t.get('titulo')} | {t.get('responsavel')} | {t.get('status')}")
                pause()
            elif op == "4":
                resp = input("Nome do responsável: ").strip()
                res = buscar_tarefas_por_responsavel(resp)
                if not res:
                    print("Nenhuma encontrada.")
                else:
                    for t in res:
                        print(f"- {t.get('titulo')} | {t.get('projeto')} | {t.get('status')}")
                pause()
            elif op == "5":
                st = input("Status: ").strip().lower()
                res = buscar_tarefas_por_status(st)
                if not res:
                    print("Nenhuma encontrada.")
                else:
                    for t in res:
                        print(f"- {t.get('titulo')} | {t.get('projeto')} | {t.get('responsavel')}")
                pause()
            elif op == "6":
                titulo = input("Título p/ atualizar: ").strip()
                print("[1] Título [2] Projeto [3] Responsável [4] Status [5] Prazo")
                esc = input("Escolha: ").strip()
                campo_map = {"1":"titulo","2":"projeto","3":"responsavel","4":"status","5":"prazo"}
                campo = campo_map.get(esc)
                if not campo:
                    print("Opção inválida.")
                else:
                    if campo == "prazo":
                        valor = pedir_data("Novo prazo: ")
                    else:
                        valor = input("Novo valor (pendente, andamento ou concluido): ").strip()
                    atualizar_tarefa(titulo, campo, valor)
                    print("✔ Atualizado (se existe).")
                pause()
            elif op == "7":
                titulo = input("Título p/ concluir: ").strip()
                if concluir_tarefa(titulo):
                    print("✔ Concluída.")
                else:
                    print("Não encontrada.")
                pause()
            elif op == "8":
                titulo = input("Título p/ reabrir: ").strip()
                if reabrir_tarefa(titulo):
                    print("✔ Reaberta.")
                else:
                    print("Não encontrada.")
                pause()
            elif op == "9":
                titulo = input("Título p/ remover: ").strip()
                if remover_tarefa(titulo):
                    print("✔ Removida.")
                else:
                    print("Não encontrada.")
                pause()
            elif op == "10":
                if input("Tem certeza? (s/n): ").strip().lower() == "s":
                    remover_todas_tarefas()
                    print("✔ Todas removidas.")
                pause()
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)
            pause()

# -------- Menu principal integrando tudo --------
def menu_main():
    while True:
        print("\n===== SISTEMA =====")
        print("[1] Usuários")
        print("[2] Projetos")
        print("[3] Tarefas")
        print("[0] Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            menu_usuarios()
        elif op == "2":
            menu_projetos()
        elif op == "3":
            menu_tarefas()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")