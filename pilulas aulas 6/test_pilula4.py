def calcular_bonus(salario_base: float, avaliacao: str) -> float:
    if salario_base < 0:
        return 0.0

    if avaliacao == "excelente":
        return salario_base * 0.20

    elif avaliacao == "bom":
        return salario_base * 0.10

    elif avaliacao == "regular":
        return salario_base * 0.02

    else:
        return 0.0

salario = float(input("Digite o salário base do funcionário: "))

avaliacao = input("Digite a avaliação do funcionário: ")

bonus = calcular_bonus(salario, avaliacao)

print(f"bônus: R$ {bonus:.2f}")