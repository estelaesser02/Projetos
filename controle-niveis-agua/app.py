
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e as situações do reservatório
niveis_agua = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"}
]


# Função que define a cor conforme o nível da água
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibe as situações do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for agua in niveis_agua:
    cor = definir_cor(agua["nivel"])
    mensagem = f"Nível {agua['nivel']}: {agua['situacao']}"
    print(cor + mensagem + Style.RESET_ALL)
