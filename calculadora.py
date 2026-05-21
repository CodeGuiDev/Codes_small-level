import math
import os

# ─────────────────────────────────────────
#  Utilitários
# ─────────────────────────────────────────

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_cabecalho():
    print("=" * 40)
    print("          🧮  CALCULADORA PYTHON")
    print("=" * 40)

def exibir_menu():
    print("""
  OPERAÇÕES BÁSICAS
  -----------------
  1. Adição           (+)
  2. Subtração        (-)
  3. Multiplicação    (*)
  4. Divisão          (/)
  5. Divisão inteira  (//)
  6. Módulo / Resto   (%)
  7. Potência         (^)

  OPERAÇÕES AVANÇADAS
  -------------------
  8.  Raiz quadrada
  9.  Raiz N-ésima
  10. Logaritmo (base 10)
  11. Logaritmo natural (ln)
  12. Logaritmo base N
  13. Seno
  14. Cosseno
  15. Tangente
  16. Fatorial

  OUTRAS
  ------
  17. Histórico de operações
  0.  Sair
""")

# ─────────────────────────────────────────
#  Leitura segura de entradas
# ─────────────────────────────────────────

def ler_numero(prompt="Digite um número: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um número válido.")

def ler_inteiro_positivo(prompt="Digite um número inteiro positivo: "):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                raise ValueError
            return n
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um inteiro positivo.")

# ─────────────────────────────────────────
#  Formatação de resultado
# ─────────────────────────────────────────

def formatar(valor):
    """Remove .0 de inteiros para exibição mais limpa."""
    if isinstance(valor, float) and valor.is_integer():
        return int(valor)
    if isinstance(valor, float):
        return round(valor, 10)
    return valor

# ─────────────────────────────────────────
#  Operações
# ─────────────────────────────────────────

def dois_operandos(operador):
    a = ler_numero("  Primeiro número : ")
    b = ler_numero("  Segundo número  : ")

    try:
        if operador == "+":
            res = a + b
            expr = f"{formatar(a)} + {formatar(b)}"
        elif operador == "-":
            res = a - b
            expr = f"{formatar(a)} - {formatar(b)}"
        elif operador == "*":
            res = a * b
            expr = f"{formatar(a)} × {formatar(b)}"
        elif operador == "/":
            if b == 0:
                raise ZeroDivisionError
            res = a / b
            expr = f"{formatar(a)} ÷ {formatar(b)}"
        elif operador == "//":
            if b == 0:
                raise ZeroDivisionError
            res = int(a // b)
            expr = f"{formatar(a)} // {formatar(b)}"
        elif operador == "%":
            if b == 0:
                raise ZeroDivisionError
            res = a % b
            expr = f"{formatar(a)} % {formatar(b)}"
        elif operador == "**":
            res = a ** b
            expr = f"{formatar(a)} ^ {formatar(b)}"
        else:
            return None
    except ZeroDivisionError:
        print("\n  ❌  Erro: divisão por zero!")
        return None

    return expr, formatar(res)

def raiz_quadrada():
    a = ler_numero("  Número: ")
    if a < 0:
        print("\n  ❌  Erro: raiz quadrada de número negativo.")
        return None
    res = math.sqrt(a)
    return f"√{formatar(a)}", formatar(res)

def raiz_n():
    a = ler_numero("  Número  : ")
    n = ler_numero("  Índice N: ")
    if n == 0:
        print("\n  ❌  Erro: índice zero.")
        return None
    if a < 0 and n % 2 == 0:
        print("\n  ❌  Erro: raiz de índice par de número negativo.")
        return None
    sinal = -1 if a < 0 else 1
    res = sinal * (abs(a) ** (1 / n))
    return f"{formatar(n)}√{formatar(a)}", formatar(res)

def logaritmo(base=10):
    a = ler_numero("  Número: ")
    if a <= 0:
        print("\n  ❌  Erro: logaritmo de número não-positivo.")
        return None
    if base == "e":
        res = math.log(a)
        return f"ln({formatar(a)})", formatar(res)
    res = math.log10(a) if base == 10 else math.log(a, base)
    return f"log{base}({formatar(a)})", formatar(res)

def logaritmo_base_n():
    base = ler_numero("  Base do logaritmo: ")
    if base <= 0 or base == 1:
        print("\n  ❌  Erro: base inválida.")
        return None
    return logaritmo(base)

def trigonometria(func_nome):
    graus = ler_numero("  Ângulo em graus: ")
    rad = math.radians(graus)
    if func_nome == "sen":
        res = math.sin(rad)
    elif func_nome == "cos":
        res = math.cos(rad)
    elif func_nome == "tan":
        if abs(math.cos(rad)) < 1e-10:
            print("\n  ❌  Erro: tangente indefinida nesse ângulo.")
            return None
        res = math.tan(rad)
    return f"{func_nome}({formatar(graus)}°)", formatar(res)

def fatorial():
    n = ler_inteiro_positivo("  Número inteiro não-negativo: ")
    if n > 20:
        print("  ℹ  Aviso: resultado muito grande (mostrado em notação científica).")
    res = math.factorial(n)
    return f"{n}!", res

# ─────────────────────────────────────────
#  Loop principal
# ─────────────────────────────────────────

def main():
    historico = []

    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu()

        opcao = input("  Escolha uma opção: ").strip()

        resultado = None

        if opcao == "0":
            print("\n  Até mais! 👋\n")
            break

        elif opcao == "1":
            resultado = dois_operandos("+")
        elif opcao == "2":
            resultado = dois_operandos("-")
        elif opcao == "3":
            resultado = dois_operandos("*")
        elif opcao == "4":
            resultado = dois_operandos("/")
        elif opcao == "5":
            resultado = dois_operandos("//")
        elif opcao == "6":
            resultado = dois_operandos("%")
        elif opcao == "7":
            resultado = dois_operandos("**")
        elif opcao == "8":
            resultado = raiz_quadrada()
        elif opcao == "9":
            resultado = raiz_n()
        elif opcao == "10":
            resultado = logaritmo(10)
        elif opcao == "11":
            resultado = logaritmo("e")
        elif opcao == "12":
            resultado = logaritmo_base_n()
        elif opcao == "13":
            resultado = trigonometria("sen")
        elif opcao == "14":
            resultado = trigonometria("cos")
        elif opcao == "15":
            resultado = trigonometria("tan")
        elif opcao == "16":
            resultado = fatorial()
        elif opcao == "17":
            limpar_tela()
            exibir_cabecalho()
            print("\n  📋  HISTÓRICO\n")
            if not historico:
                print("  (nenhuma operação realizada ainda)")
            else:
                for i, (expr, res) in enumerate(historico, 1):
                    print(f"  {i:>3}. {expr} = {res}")
            print()
            input("  Pressione Enter para voltar...")
            continue
        else:
            print("\n  ⚠  Opção inválida.\n")
            input("  Pressione Enter para continuar...")
            continue

        if resultado:
            expr, res = resultado
            historico.append((expr, res))
            print(f"\n  ✅  {expr} = {res}\n")

        input("  Pressione Enter para continuar...")

if __name__ == "__main__":
    main()