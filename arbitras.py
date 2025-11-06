import json
   
# Esse programa carrega o json de árbitras e caso não exista, ele cria um novo
# Adiciona, Lista, Atualiza nome e exclui são as principais funções desse programa
# Interface para que o usuário consiga utilizar as funções criadas.


#Carrega o arquivo JSON.
def carregar_arbitras():
    try:
        with open("arbitras.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []  # Retorna lista vazia caso o arquivo não exista
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Criando um novo...")
        return []

#Salva a lista de árbitras no JSON
def salvar_arbitras(arbitras):
    with open("arbitras.json", "w", encoding="utf-8") as arquivo:
        json.dump(arbitras, arquivo, ensure_ascii=False, indent=4)

# --- Aqui começa o CRUD do programa ---

# Adiciona uma nova árbitra
def adicionar_arbitra(arbitras):
    nome = input("Digite o nome da árbitra: ").strip()
    if nome:
        arbitras.append(nome)
        salvar_arbitras(arbitras)
        print(f"✅ Árbitra '{nome}' adicionada com sucesso!\n")
    else:
        print("⚠️ Nome inválido. Tente novamente.\n")

# Lista todas as árbitras
def listar_arbitras(arbitras):
    if not arbitras:
        print("📭 Nenhuma árbitra cadastrada.\n")
    else:
        print("\n📋 Lista de Árbitras:")
        for i, nome in enumerate(arbitras, 1):
            print(f"{i}. {nome}")
        print()

# Atualiza o nome da árbitra baseado no número da posição no JSON
def atualizar_arbitra(arbitras):
    listar_arbitras(arbitras)
    try:
        indice = int(input("Digite o número da árbitra que deseja atualizar: ")) - 1
        if 0 <= indice < len(arbitras):
            novo_nome = input("Digite o novo nome: ").strip()
            if novo_nome:
                antigo = arbitras[indice]
                arbitras[indice] = novo_nome
                salvar_arbitras(arbitras)
                print(f"✅ Árbitra '{antigo}' atualizada para '{novo_nome}'.\n")
            else:
                print("⚠️ Nome inválido.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Exclui árbitra da lista
def excluir_arbitra(arbitras):
    listar_arbitras(arbitras)
    try:
        indice = int(input("Digite o número da árbitra que deseja excluir: ")) - 1
        if 0 <= indice < len(arbitras):
            removida = arbitras.pop(indice)
            salvar_arbitras(arbitras)
            print(f"🗑️ Árbitra '{removida}' removida com sucesso.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Interface intuitiva para o usuário final
def menu():
    arbitras = carregar_arbitras()
    
# Lista de funções
    while True:
        print("=== ⚽ SISTEMA DE GESTÃO DE ÁRBITRAS ⚽ ===")
        print("1️⃣  Listar árbitras")
        print("2️⃣  Adicionar árbitra")
        print("3️⃣  Atualizar árbitra")
        print("4️⃣  Excluir árbitra")
        print("5️⃣  Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_arbitras(arbitras)
        elif opcao == "2":
            adicionar_arbitra(arbitras)
        elif opcao == "3":
            atualizar_arbitra(arbitras)
        elif opcao == "4":
            excluir_arbitra(arbitras)
        elif opcao == "5":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")

# Execução do programa
if __name__ == "__main__":
    menu()
