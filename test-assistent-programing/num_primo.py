def is_prime(n):
    """Verifica se um número é primo.

    Args:
        n (int): Número inteiro a ser testado.

    Returns:
        bool: True se o número for primo; False caso contrário.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    import sys
    try:
        num = int(sys.argv[1])
    except (IndexError, ValueError):
        num = int(input("Digite um número: "))
    print(f"{num} é primo? {is_prime(num)}")
