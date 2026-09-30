from mod_estoque import cadastrar_item, calcular_valor_estoque, listar_itens_em_falta


def main():
    estoque = []

    estoque.append(cadastrar_item("Sensor Ultrassônico", 15, 25.50))
    estoque.append(cadastrar_item("Motor DC", 3, 42.00))
    estoque.append(cadastrar_item("Placa Microcontroladora", 2, 110.00))

    valor_total = calcular_valor_estoque(estoque)
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

    limite_minimo = 5
    itens_faltantes = listar_itens_em_falta(estoque, limite_minimo)

    print(f"\nItens em falta (menos de {limite_minimo} unidades):")
    for item in itens_faltantes:
        print(f"- {item['nome']}: {item['quantidade']} unid. (R$ {item['preco_unitario']:.2f} cada)")


if __name__ == "__main__":
    main()