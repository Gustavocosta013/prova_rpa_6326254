

ENDPOINT_URL: str = "https://api.exemplo.com/v1"
PORTA: int = 443
TAXA_AMOSTRAGEM: float = 1.5
USA_HTTPS: bool = True


parametros = {
    "endpoint_url": ENDPOINT_URL,
    "porta": PORTA,
    "taxa_amostragem": TAXA_AMOSTRAGEM,
    "usa_https": USA_HTTPS
}

print("=== RELATÓRIO DE VALIDAÇÃO DE PARÂMETROS ===")
for chave, valor in parametros.items():
    print(f"Parâmetro: {chave:<15} | Valor: {valor:<30} | Tipo: {type(valor)}")