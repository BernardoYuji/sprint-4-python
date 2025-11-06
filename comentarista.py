import json

# Esse programa carrega o json de comentaristas e caso não exista, ele cria um novo
# Adiciona, Lista, Atualiza nome e exclui são as principais funções desse programa
# Interface para que o usuário consiga utilizar as funções criadas.

# Carrega o arquivo JSON
def carregar_comentaristas():
    try:
        with open("comentaristas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] #Retorna lista vazia caso o arquivo não exista
    except json.JSONDecodeError:
        print("Erro ao ler os dados do arquivo. Criando um novo...")
        return []

# Salva a lista de comentaristas no JSON
def salvar_comentaristas(comentaristas):
    with open("comentaristas.json", "w", encoding="utf-8") as arquivo:
        json.dump(comentaristas, arquivo, ensure_ascii=False, indent=4)


#--- Aqui começa o CRUD do programa ---

# Adiciona uma nova comentarista 
def adicionar_comentaristas(comentaristas):
    nome = input("Digite o nome da comentarista: ").strip()
    if nome:
        comentaristas.append(nome)
        salvar_comentaristas(comentaristas)
        print(f"✅ Comentarista '{nome}' adicionada com sucesso!\n")        
    else:
        print("⚠️ Nome inválido. Tente novamente.\n")

 # Lista todas as comentaristas
def listar_comentaristas(comentaristas):
    if not comentaristas:
        print("Nenhuma comentarista cadastrada.\n")
    else:
        print("\n📋 Lista de Comentaristas:")
        for i, nome in enumerate(comentaristas, 1):
            print(f"{i}. {nome}")
        print()


# Atualiza o nome da comentarista baseando no número da posição no JSON
def atualizar_comentaristas(comentaristas):
    listar_comentaristas(comentaristas)
    try:
        indice = int(input("Digite o número da comentarista que deseja atualizar: ")) - 1
        if 0 <= indice < len(comentaristas):
            novo_nome = input("Digite o novo nome: ").strip()
            if novo_nome:
                antigo = comentaristas[indice]
                comentaristas[indice] = novo_nome
                salvar_comentaristas(comentaristas)
                print(f"✅ Comentarista '{antigo}' atualizada para '{novo_nome}'.\n")
            else:
                print("⚠️ Nome inválido.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Exclui comentarista da lista
def excluir_comentaristas(comentaristas):
    listar_comentaristas(comentaristas)
    try:
        indice = int(input("Digite o número da comentarista que deseja excluir: "))-1
        if 0 <= indice <= len(comentaristas):
            removida = comentaristas.pop(indice)
            salvar_comentaristas(comentaristas)
            print(f"🗑️ Comentarista '{removida}' removida com sucesso.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Interface intuitiva para o usuário final
def menu():
    comentaristas = carregar_comentaristas()

# Lista das funções
    while True:
        print("=== ⚽ SISTEMA DE GESTÃO DE comentaristas ⚽ ===")
        print("1️⃣  Listar comentaristas")
        print("2️⃣  Adicionar comentaristas")
        print("3️⃣  Atualizar comentaristas")
        print("4️⃣  Excluir comentaristas")
        print("5️⃣  Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_comentaristas(comentaristas)
        elif opcao == "2":
            adicionar_comentaristas(comentaristas)
        elif opcao == "3":
            atualizar_comentaristas(comentaristas)
        elif opcao == "4":
            excluir_comentaristas(comentaristas)
        elif opcao == "5":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")

# Execução do arquivo
if __name__ == "__main__":
    menu()