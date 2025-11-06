import json
import os

# Le arquivo JSON e caso não exista, ele cria um novo
# Cria time, salvando dados como jogadoras, jogos, vitorias, derrotas, empate e pontos
# Cadastra novas jogadoras e salva dados como nome, posição, time, gols, assistências e cartões
# Lista as jogadoras que ja estão cadastradas
# Possibilidade de atualizar os dados de uma jogadoras específica
# Possibilidade de excluir uma jogadora cadastrada
# Registrar e atualizar dados dos times
# Interface para usuário utilizar


# --- Arquivos JSON para persistência ---
ARQUIVO_TIMES = "times.json"
ARQUIVO_JOGADORAS = "jogadoras.json"

# --- Funções de persistência ---
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Erro ao ler {arquivo}, criando novo arquivo...")
            return {}
    return {}

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# --- Carregar dados existentes ---
times = carregar_dados(ARQUIVO_TIMES)
estatisticas_jogadoras = carregar_dados(ARQUIVO_JOGADORAS)

# --- Funções CRUD ---

def criar_time(time):
    """Garante que o time exista"""
    if time not in times:
        times[time] = {
            "jogadoras": {f"jogadora{i}": "" for i in range(1, 9)},
            "jogos": 0,
            "vitoria": 0,
            "empate": 0,
            "derrota": 0,
            "pontos": 0
        }
        salvar_dados(ARQUIVO_TIMES, times)
    return times[time]

def cadastrar_jogadora():
    nome = input("Nome da jogadora: ").strip()
    time = input("Time: ").strip()
    posicao = input("Posição: ").strip()
    
    criar_time(time)
    
    # Encontrar primeira vaga livre
    for vaga in times[time]["jogadoras"]:
        if times[time]["jogadoras"][vaga] == "":
            times[time]["jogadoras"][vaga] = nome
            salvar_dados(ARQUIVO_TIMES, times)
            print(f"✅ {nome} cadastrada no {time}, vaga {vaga} ({posicao})")
            
            # Estatísticas iniciais
            gols = int(input("Gols: "))
            assistencias = int(input("Assistências: "))
            cartoes_amarelo = int(input("Cartões amarelos: "))
            cartoes_vermelho = int(input("Cartões vermelhos: "))
            estatisticas_jogadoras[nome] = {
                "time": time,
                "posição": posicao,
                "gols": gols,
                "assistencias": assistencias,
                "cartoes_amarelo": cartoes_amarelo,
                "cartoes_vermelho": cartoes_vermelho
            }
            salvar_dados(ARQUIVO_JOGADORAS, estatisticas_jogadoras)
            return
    print("⚠️ Todas as posições já estão preenchidas nesse time.")

def listar_jogadoras():
    if not estatisticas_jogadoras:
        print("Nenhuma jogadora cadastrada.")
        return
    print("\n=== Jogadoras Cadastradas ===")
    for nome, stats in sorted(estatisticas_jogadoras.items()):
        print(f"{nome} - Time: {stats['time']}, Posição: {stats['posição']}, "
              f"Gols: {stats['gols']}, Assistências: {stats['assistencias']}, "
              f"Amarelos: {stats['cartoes_amarelo']}, Vermelhos: {stats['cartoes_vermelho']}")

def atualizar_estatisticas():
    nome = input("Nome da jogadora que deseja atualizar: ").strip()
    if nome not in estatisticas_jogadoras:
        print("⚠️ Jogadora não encontrada.")
        return
    stats = estatisticas_jogadoras[nome]
    print(f"Atualizando {nome} - Time: {stats['time']}, Posição: {stats['posição']}")
    try:
        stats['gols'] = int(input(f"Gols ({stats['gols']}): ") or stats['gols'])
        stats['assistencias'] = int(input(f"Assistências ({stats['assistencias']}): ") or stats['assistencias'])
        stats['cartoes_amarelo'] = int(input(f"Cartões amarelos ({stats['cartoes_amarelo']}): ") or stats['cartoes_amarelo'])
        stats['cartoes_vermelho'] = int(input(f"Cartões vermelhos ({stats['cartoes_vermelho']}): ") or stats['cartoes_vermelho'])
        salvar_dados(ARQUIVO_JOGADORAS, estatisticas_jogadoras)
        print("✅ Estatísticas atualizadas.")
    except ValueError:
        print("⚠️ Entrada inválida, tente novamente.")

def excluir_jogadora():
    nome = input("Nome da jogadora que deseja excluir: ").strip()
    if nome not in estatisticas_jogadoras:
        print("⚠️ Jogadora não encontrada.")
        return
    time = estatisticas_jogadoras[nome]["time"]
    # Remover da vaga do time
    for vaga, nome_vaga in times[time]["jogadoras"].items():
        if nome_vaga == nome:
            times[time]["jogadoras"][vaga] = ""
            break
    # Remover estatísticas
    del estatisticas_jogadoras[nome]
    salvar_dados(ARQUIVO_TIMES, times)
    salvar_dados(ARQUIVO_JOGADORAS, estatisticas_jogadoras)
    print(f"✅ Jogadora {nome} removida com sucesso.")

def registrar_resultado():
    time = input("Time: ").strip()
    if time not in times:
        print("⚠️ Time não encontrado.")
        return
    print("Resultado do jogo:")
    print("1. Vitória")
    print("2. Empate")
    print("3. Derrota")
    opcao = input("Escolha: ").strip()
    criar_time(time)
    times[time]["jogos"] += 1
    if opcao == "1":
        times[time]["vitoria"] += 1
        times[time]["pontos"] += 3
    elif opcao == "2":
        times[time]["empate"] += 1
        times[time]["pontos"] += 1
    elif opcao == "3":
        times[time]["derrota"] += 1
    else:
        print("⚠️ Opção inválida.")
        return
    salvar_dados(ARQUIVO_TIMES, times)
    print(f"✅ Resultado registrado para o time {time}.")

def mostrar_top_gols():
    if not estatisticas_jogadoras:
        print("Nenhuma jogadora cadastrada.")
        return
    top = sorted(estatisticas_jogadoras.items(), key=lambda x: x[1]["gols"], reverse=True)[:5]
    print("\n=== Top 5 Jogadoras com mais gols ===")
    for i, (nome, stats) in enumerate(top, 1):
        print(f"{i}. {nome} - {stats['gols']} gols")

# --- Função para editar times ---
def editar_time():
    time = input("Nome do time que deseja editar: ").strip()
    if time not in times:
        print("⚠️ Time não encontrado.")
        return

    print(f"\nEditando time: {time}")
    print("1. Alterar nome do time")
    print("2. Redefinir estatísticas do time")
    print("3. Alterar jogadoras do time")
    opcao = input("Escolha a opção: ").strip()

    if opcao == "1":
        novo_nome = input("Novo nome do time: ").strip()
        if novo_nome in times:
            print("⚠️ Esse nome já existe.")
            return
        times[novo_nome] = times.pop(time)
        # Atualizar o time nas jogadoras
        for nome, stats in estatisticas_jogadoras.items():
            if stats["time"] == time:
                stats["time"] = novo_nome
        salvar_dados(ARQUIVO_TIMES, times)
        salvar_dados(ARQUIVO_JOGADORAS, estatisticas_jogadoras)
        print(f"✅ Time renomeado para {novo_nome}.")
    
    elif opcao == "2":
        times[time]["jogos"] = 0
        times[time]["vitoria"] = 0
        times[time]["empate"] = 0
        times[time]["derrota"] = 0
        times[time]["pontos"] = 0
        salvar_dados(ARQUIVO_TIMES, times)
        print(f"✅ Estatísticas do time {time} redefinidas.")
    
    elif opcao == "3":
        print(f"Jogadoras do time {time}:")
        for vaga, nome_jogadora in times[time]["jogadoras"].items():
            print(f"{vaga}: {nome_jogadora}")
        vaga = input("Digite a vaga que deseja alterar (ex: jogadora1): ").strip()
        if vaga not in times[time]["jogadoras"]:
            print("⚠️ Vaga inválida.")
            return
        novo_nome = input("Nome da nova jogadora (deixe vazio para remover): ").strip()
        times[time]["jogadoras"][vaga] = novo_nome
        salvar_dados(ARQUIVO_TIMES, times)
        print(f"✅ Vaga {vaga} atualizada para '{novo_nome}'.")
    
    else:
        print("⚠️ Opção inválida.")

# --- Atualizar menu ---
def menu():
    while True:
        print("\n=== Gerenciamento de Jogadoras e Times ===")
        print("1. Cadastrar jogadora")
        print("2. Listar jogadoras")
        print("3. Atualizar estatísticas")
        print("4. Excluir jogadora")
        print("5. Registrar resultado do time")
        print("6. Mostrar top 5 gols")
        print("7. Editar time")
        print("8. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_jogadora()
        elif opcao == "2":
            listar_jogadoras()
        elif opcao == "3":
            atualizar_estatisticas()
        elif opcao == "4":
            excluir_jogadora()
        elif opcao == "5":
            registrar_resultado()
        elif opcao == "6":
            mostrar_top_gols()
        elif opcao == "7":
            editar_time()
        elif opcao == "8":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# --- Rodar menu ---
if __name__ == "__main__":
    menu()
