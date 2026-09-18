import json
import os

ARQUIVO = "empresas.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def adicionar_peso(dados):
    nome = input("Nome da empresa: ").strip()
    peso = float (input("Insira o peso: "))
    dados[nome] = peso
    salvar_dados(dados)
    print(f"Peso {peso} salvo para {nome}!")

def multiplicar(dados):
    if not dados:
        print("Empresa não cadastrada")
        return
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print (f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha uma empresa: ")
    escolha = int(input().strip()) - 1

    nome = nomes[escolha]
    peso = dados[nome]
    quantidade = float(input("Quantidade: "))
    total = quantidade * peso
    print(f"Total: {total:.2f}")

def listar(dados):
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})")

def mudar_peso(dados):
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha a empresa que você quer mudar os dados: ")
    escolha = int(input().strip()) - 1

    peso = nomes[escolha]
    novo_peso = float(input("Insira o peso: "))
    dados[peso] = novo_peso
    salvar_dados(dados)
    print(f"Peso de {peso} atualizado para {novo_peso}!")

def remover_empresa(dados):
    nomes = list(dados.keys())
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome} (peso: {dados[nome]:.2f})")
    print("\nEscolha a empresa que você quer remover: ")
    escolha = int(input().strip()) - 1

    remocao = nomes[escolha]
    dados.pop(remocao)
    print({remocao}, " removido com sucesso.")

def menu():
    dados = carregar_dados()
    while True:
        print("1. Multiplicar peso")
        print("2. Adicionar empresa")
        print("3. Remover empresa")
        print("4. Lista de empresas")
        print("5. Mudar peso")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            multiplicar(dados)
        elif opcao == "2":
            adicionar_peso(dados)
        elif opcao == "3":
            remover_empresa(dados)
        elif opcao == "4":
            listar(dados)
        elif opcao == "5":
            mudar_peso(dados)


menu()
