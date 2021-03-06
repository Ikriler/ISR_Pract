def Calculator():
    try:
        operations = ["+", "-", "/", "*", "//", "**", "%", "comb", "Copysign", "ldexp", "Hypot", "PPar", "SPar"]
        a, b = (float(input("Введите число: ")) for i in range(2))
        print("Список операций:")
        for i in range(len(operations)):
            print(operations[i], end=" ")
        operation = input("\nВведите операцию: ")
        match operation:
            case "+":
                print("a + b = ", a + b)
            case "-":
                print("a - b = ", a - b)
            case "/":   
                print("a / b = ", a / b)
            case "*":
                print("a * b = ", a * b)
            case "//":
                print("a // b = ", a // b)
            case "**":
                print("a ** b = ", a ** b)
            case "%":
                print(f"a % b", a % b)
            case "comb":
                print("a comb b = ", math.comb(int(a), int(b)))
            case "Copysign":
                print("a Copysign b = ", math.copysign(a, b))
            case "ldexp":
                print("ldexp(a,b) = ", math.ldexp(int(a), int(b)))
            case "Hypot":
                print("Fabs(a,b) = ", math.hypot(a, b))
            case "PPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: (a + b + d) * 4
                print("PPar(a,b,c) = ", f(a, b, d))
            case "SPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: ((a * b) + (a * d) + (d * b)) * 2
                print("SPar(a,b,d) = ", f(a, b, d))
    except Exception:
        print("Ошибка ввода данных")

Calculator()