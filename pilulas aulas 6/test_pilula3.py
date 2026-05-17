def converter_nota_para_conceito(nota: float) -> str:
    if nota >= 9:
        return "conceito A"
    
    elif nota >= 7 and nota <= 8.9:
        return "conceito B"
    
    elif nota >= 5 and nota <= 6.9:
        return "conceito C"
    
    elif nota >= 3 and nota <= 4.9:
        return "conceito D"
    
    elif nota < 3:
        return "conceito F"
    
    else:
        return "nota inválida"
    
nota = float(input("Digite a nota: "))

conceito = converter_nota_para_conceito(nota)

print(f"resultado: {conceito}")


