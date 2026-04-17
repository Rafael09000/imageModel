def calcular_estatisticas(numeros: list[int]) -> tuple[int, float, int, int]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros: Lista de números inteiros.
        
    Returns:
        Tupla contendo (total, média, máximo, mínimo).
    """
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return total, media, maximo, minimo


def main() -> None:
    """Função principal para executar o programa."""
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maximo, minimo = calcular_estatisticas(numeros)
    
    print(f"Total: {total}")
    print(f"Média: {media:.2f}")
    print(f"Maior: {maximo}")
    print(f"Menor: {minimo}")


if __name__ == "__main__":
    main()