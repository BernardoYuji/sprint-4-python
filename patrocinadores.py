import json

# Esse programa carrega o json de árbitras e caso não exista, ele cria um novo
# Adiciona, Lista, Atualiza nome e exclui são as principais funções desse programa
# Interface para que o usuário consiga utilizar as funções criadas.

# Função que carrega o JSON dos patrocinadores
# Caso não exista, ele cria um JSON novo
def carregar_patrocinadores():
    try:
        with open("patrocinadores.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Criando um novo...")


# Salva os dados dos patrocinadores em um JSON
def salvar_patrocinadores(patrocinadores):
    with open("patrocinadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(patrocinadores, arquivo, ensure_ascii=False, indent=4)

# Adiciona novos patrocinadores ao JSON
def adicionar_patrocinadores(patrocinadores):
    nome = input("Digite o nome do Patrocinador: ").strip()
    if nome:
        patrocinadores.append(nome)
        salvar_patrocinadores(patrocinadores)
        print(f"✅ Patrocinador '{nome}' adicionada com sucesso!\n")
    else:
        print("⚠️ Nome inválido. Tente novamente.\n")

# Lista todas as Patrocinadors
def listar_patrocinadores(patrocinadores):
    if not patrocinadores:
        print("📭 Nenhuma Patrocinador cadastrada.\n")
    else:
        print("\n📋 Lista de Patrocinadores:")
        for i, nome in enumerate(patrocinadores, 1):
            print(f"{i}. {nome}")
        print()

# Atualiza o nome da Patrocinador baseado no número da posição no JSON
def atualizar_arbitra(patrocinadores):
    listar_patrocinadores(patrocinadores)
    try:
        indice = int(input("Digite o número da Patrocinador que deseja atualizar: ")) - 1
        if 0 <= indice < len(patrocinadores):
            novo_nome = input("Digite o novo nome: ").strip()
            if novo_nome:
                antigo = patrocinadores[indice]
                patrocinadores[indice] = novo_nome
                salvar_patrocinadores(patrocinadores)
                print(f"✅ Patrocinador '{antigo}' atualizada para '{novo_nome}'.\n")
            else:
                print("⚠️ Nome inválido.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Exclui Patrocinador da lista
def excluir_arbitra(patrocinadores):
    listar_patrocinadores(patrocinadores)
    try:
        indice = int(input("Digite o número da Patrocinador que deseja excluir: ")) - 1
        if 0 <= indice < len(patrocinadores):
            removida = patrocinadores.pop(indice)
            salvar_patrocinadores(patrocinadores)
            print(f"🗑️ Patrocinador '{removida}' removida com sucesso.\n")
        else:
            print("⚠️ Número inválido.\n")
    except ValueError:
        print("⚠️ Digite um número válido.\n")

# Interface intuitiva para o usuário final
def menu():
    patrocinadores = carregar_patrocinadores()
    
# Lista de funções
    while True:
        print("=== ⚽ SISTEMA DE GESTÃO DE PatrocinadorS ⚽ ===")
        print("1️⃣  Listar patrocinadores")
        print("2️⃣  Adicionar patrocinadores")
        print("3️⃣  Atualizar patrocinadores")
        print("4️⃣  Excluir patrocinadores")
        print("5️⃣  Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_patrocinadores(patrocinadores)
        elif opcao == "2":
            adicionar_patrocinadores(patrocinadores)
        elif opcao == "3":
            atualizar_arbitra(patrocinadores)
        elif opcao == "4":
            excluir_arbitra(patrocinadores)
        elif opcao == "5":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")

# Execução do programa
if __name__ == "__main__":
    menu()
