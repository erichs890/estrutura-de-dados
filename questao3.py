def divisaoInteira(a, b, x=0):
    if a < b:
        return x
    else:
        return divisaoInteira(a - b, b, x + 1)

num1 = int(input("Diz um numero garinha:\n"))
num2 = int(input('Diz outro numero gatinha>\n'))
resultado = divisaoInteira(num1, num2)
print("Resultado da divisão inteira:", resultado)
