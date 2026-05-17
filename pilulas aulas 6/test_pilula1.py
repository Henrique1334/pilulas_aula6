def acao_semaforo(cor: str) -> str:
    if cor == "vermelho":
        return "Pare"
    
    elif cor == "amarelo":
        return "Atenção"
    
    elif cor == "verde":
        return "Siga"
    
    else:
        return "Cor inválida"

cor= input("Digite a cor do semáforo: ").lower()

resultado= acao_semaforo(cor)

print(f"motorista: {resultado}")