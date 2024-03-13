def potencia_de_2(n):
    if n == 0:
        return 1
    else:
        return 2 * potencia_de_2(n - 1)

# Exemplo de uso
n = 5
resultado = potencia_de_2(n)
print("2 elevado a", n, "é igual a:", resultado)
