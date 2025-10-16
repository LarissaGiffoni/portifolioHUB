# calculadora.py
# 🎯 Objetivo: Programa simples para somar despesas mensais e calcular o total.

print("💰 Calculadora de Despesas Mensais")
print("----------------------------------")

# Lista para armazenar as despesas
despesas = []

while True:
    valor = input("Digite o valor da despesa (ou 'fim' para encerrar): ")
    if valor.lower() == 'fim':
        break
    try:
        valor = float(valor)
        despesas.append(valor)
    except ValueError:
        print("Por favor, digite um número válido.")

# Exibir o resultado
total = sum(despesas)
print("----------------------------------")
print(f"Você registrou {len(despesas)} despesas.")
print(f"Total gasto no mês: R$ {total:.2f}")

# Mostrar média, se quiser
if despesas:
    media = total / len(despesas)
    print(f"Média por despesa: R$ {media:.2f}")

print("----------------------------------")
print("Programa finalizado. Até a próxima! 👋")
