def calcular_salario():
    nome = input("Nome do colaborador: ")
    salario_base = float(input("Salário Base (R$):"))
    horas_extras = float(input("Total de Horas Extra: "))
    valor_hora = float(input("Valor da hora extra (R$): "))
    descontos = float(input("Total de descontos (R$): "))

    salario_bruto = salario_base + (horas_extras * valor_hora)
    salario_liquido = salario_bruto - descontos

    print("\n==== Folha de Pagamento ====")
    print(f"Funcionário: {nome}")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Horas extras: R$ {horas_extras * valor_hora:.2f}")
    print(f"Descontos: R$ {descontos:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

calcular_salario()   