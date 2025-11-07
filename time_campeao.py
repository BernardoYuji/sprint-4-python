import json
import os

# Importa o JSON dos times para montar a tabela
ARQUIVO_TIMES = "times.json"

# Carrega os dados do JSON dos times para a construção da tabela
def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Erro ao ler {arquivo}.")
            return {}
    else:
        print("⚠️ Arquivo de times não encontrado.")
        return {}

# Função que monta e mostra a tabela de classificação do campeonato
def mostrar_tabela_classificacao():
    times = carregar_dados(ARQUIVO_TIMES)

    if not times:
        print("⚠️ Nenhum time encontrado para montar a tabela.")
        return

    # Ordena por pontos e vitórias 
    tabela = sorted(times.items(), key=lambda x: (x[1]['pontos'], x[1]['vitoria']), reverse=True)

    print("\n=== 🏆 TABELA DE CLASSIFICAÇÃO 🏆 ===")
    print(f"{'Pos':<4}{'Time':<20}{'J':<4}{'V':<4}{'E':<4}{'D':<4}{'Pts':<5}")
    print("-" * 50)

    for pos, (time, dados) in enumerate(tabela, start=1):
        print(f"{pos:<4}{time:<20}{dados['jogos']:<4}{dados['vitoria']:<4}{dados['empate']:<4}{dados['derrota']:<4}{dados['pontos']:<5}")

    print("-" * 50)
    print(f"🏅 Campeão provisório: {tabela[0][0]} ({tabela[0][1]['pontos']} pontos)")

if __name__ == "__main__":
    mostrar_tabela_classificacao()
