# Importando a biblioteca colorama
from colorama import Fore, Style, init

# Iniciar colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Associando nível com cor
cores = {
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.GREEN,
    4: Fore.CYAN,
    5: Fore.BLUE
}

# Função para exibir a situação do reservatório
def mostrar_nivel(nivel):
    mensagem = niveis[nivel - 1]
    cor = cores.get(nivel, Fore.WHITE)

    print(cor + f"Nível {nivel}: {mensagem}")

# Simulação de monitoramento
print("=== Monitoramento do Reservatório ===\n")

for nivel in range(1, 6):
    mostrar_nivel(nivel)

# Reset final
print(Style.RESET_ALL)
