import json
import os

ARQUIVO = "dados.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def criar_item():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    dados = carregar_dados()
    novo_id = len(dados) + 1
    dados.append({"id": novo_id, "nome": nome, "idade": idade})
    salvar_dados(dados)
    print("Item criado com sucesso!\n")

def listar_itens():
    dados = carregar_dados()
    if not dados:
        print("Nenhum item encontrado.\n")
    else:
        for item in dados:
            print(item)
        print()

def atualizar_item():
    id = int(input("Digite o ID do item a atualizar: "))
    dados = carregar_dados()
    for item in dados:
        if item["id"] == id:
            novo_nome = input("Novo nome (ou Enter para manter): ")
            nova_idade = input("Nova idade (ou Enter para manter): ")
            if novo_nome:
                item["nome"] = novo_nome
            if nova_idade:
                item["idade"] = nova_idade
            salvar_dados(dados)
            print("Item atualizado com sucesso!\n")
            return
    print("Item não encontrado.\n")

def deletar_item():
    id = int(input("Digite o ID do item a deletar: "))
    dados = carregar_dados()
    dados = [item for item in dados if item["id"] != id]
    salvar_dados(dados)
    print("Item deletado com sucesso!\n")

def menu():
    while True:
        print("=== MENU CRUD ===")
        print("1 - Criar item")
        print("2 - Listar itens")
        print("3 - Atualizar item")
        print("4 - Deletar item")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_item()
        elif opcao == "2":
            listar_itens()
        elif opcao == "3":
            atualizar_item()
        elif opcao == "4":
            deletar_item()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()
