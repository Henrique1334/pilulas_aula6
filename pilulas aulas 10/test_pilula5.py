def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:

    codigo_cupom = codigo_cupom.upper()

    if codigo_cupom == "CUPOM10":
        return 0.10

    elif codigo_cupom == "CUPOM25" and valor_compra > 100:
        return 0.25

    elif codigo_cupom == "DESCONTOVIP" and valor_compra > 500:
        return 0.35

    else:
        return 0.0


codigo = input("Digite o código do cupom: ")
valor = float(input("Digite o valor da compra: R$ "))

desconto = aplicar_cupom(codigo, valor)

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"Percentual de desconto: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")