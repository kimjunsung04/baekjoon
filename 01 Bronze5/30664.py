while True:
    n = int(input())
    if n == 0:
        break

    if n % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
