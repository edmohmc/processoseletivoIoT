"""
Monitor de Estoque Kanban Inteligente
ESP32 + HX711
"""
from machine import Pin
from hx711 import HX711
import time

# =====================================================
# Configuração do hardware
# =====================================================

# Pinos definidos no diagram.json
PIN_DT = 5
PIN_SCK = 18

hx = HX711(
    dout=Pin(PIN_DT),
    pd_sck=Pin(PIN_SCK)
)

# Limites do sistema (gramas)
PESO_CAIXA_CHEIA = 5000
LIMITE_CRITICO = 150
PESO_ERRO = 0

# =====================================================
# Inicialização do sensor HX711
# =====================================================

hx = HX711(
    dout=Pin(PIN_DT),
    pd_sck=Pin(PIN_SCK)
)

# Caso a biblioteca possua função de tara, executa-a
try:
    hx.tare()
except Exception:
    pass

# Mensagem obrigatória do projeto
print("Sistema Kanban Inicializado")

# =====================================================
# Variáveis de controle
# =====================================================

reposicao_disparada = False
ultima_mensagem = ""

# =====================================================
# Função para leitura do peso
# =====================================================

def ler_peso():
    """
    Realiza a leitura do HX711.
    Caso ocorra algum erro, retorna zero.
    """

    try:
        peso = int(hx.read())

        if peso < 0:
            peso = 0

        return peso

    except Exception:
        return 0

# =====================================================
# Loop principal
# =====================================================

while True:

    peso = ler_peso()

    # -------------------------------------------------
    # Falha de leitura ou caixa ausente
    # -------------------------------------------------
    if peso == PESO_ERRO:

        mensagem = "ALERTA: Caixa ausente ou erro de calibração no sensor HX711!"

        if mensagem != ultima_mensagem:
            print(mensagem)
            ultima_mensagem = mensagem

    # -------------------------------------------------
    # Estoque crítico
    # -------------------------------------------------
    elif peso <= LIMITE_CRITICO:

        if not reposicao_disparada:
            print("Evento de reposição disparado! Caixa vazia detectada.")
            reposicao_disparada = True
            ultima_mensagem = "reposicao"

    # -------------------------------------------------
    # Caixa reabastecida
    # -------------------------------------------------
    elif reposicao_disparada and peso >= PESO_CAIXA_CHEIA:

        print("Abastecimento concluído. Caixa cheia.")
        reposicao_disparada = False
        ultima_mensagem = "abastecimento"

    # -------------------------------------------------
    # Funcionamento normal
    # -------------------------------------------------
    else:

        mensagem = f"Status: Estoque Regular ({peso}g)"

        if mensagem != ultima_mensagem:
            print(mensagem)
            ultima_mensagem = mensagem

    # Pequeno atraso para evitar uso excessivo da CPU
    time.sleep_ms(100)