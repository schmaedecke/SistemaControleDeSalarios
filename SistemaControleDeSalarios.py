registrosFuncionarios = []
baseSalaries = []
amountOfEmployees = 0
outSourcedCompanies = []
amountOfOutSourcedEmployees = 0
valeTransportes = []

def CalcularHoraExtra(extraHours):
    valorHoraNormal = 15.0
    valorHoraExtra = valorHoraNormal * 1.5
    totalHoraExtra = valorHoraExtra * extraHours
    return totalHoraExtra

def CalcularSalario(baseSalary, transportationCost, valeAlimentacao, comission, horasExtra):
    return baseSalary + transportationCost + comission + horasExtra + valeAlimentacao

import random

def InserirFuncionariosPredefinidos():
    funcionarios = []
    cargos = [
        "Diretor", "Coordenador", "Recursos Humanos", "Marketing", "Vendas",
        "Financeiro", "Desenvolvedor", "Product Designer", "Limpeza"
    ]
    
    # Gerando 50 funcionários com dados variados
    for i in range(50):
        nome = f"Funcionário {i+1}"
        cargo = random.choice(cargos)
        salario_base = random.randint(1500, 5000)  # Salário entre 1500 e 5000
        vale_alimentacao = round(random.uniform(100, 500), 2)  # Vale alimentação entre 100 e 500
        vale_transporte = round(random.uniform(50, 300), 2)  # Vale transporte entre 50 e 300
        comissao = round(random.uniform(100, 500), 2)  # Comissão entre 100 e 500
        horas_extra = round(random.uniform(0, 50), 2)  # Horas extras entre 0 e 50 horas
        terceirizado = random.choice([True, False])  # 50% chance de ser terceirizado
        empresa_terceira = random.choice(["TechSol", "ConexãoCorp", "MarketingPro", "DevWorks", "CleanCorp"]) if terceirizado else None

        # Calcular salário total
        salario_total = salario_base + vale_alimentacao + vale_transporte + comissao + (horas_extra * 15)  # Hora extra a R$ 15

        funcionario = {
            "nome": nome,
            "cargo": cargo,
            "salario_base": salario_base,
            "vale_alimentacao": vale_alimentacao,
            "vale_transporte": vale_transporte,
            "comissao": comissao,
            "horas_extra": horas_extra,
            "salario_total": salario_total,
            "terceirizado": terceirizado,
            "empresa_terceira": empresa_terceira
        }
        
        funcionarios.append(funcionario)
    
    # Adicionando os funcionários na lista global de registros
    registrosFuncionarios.extend(funcionarios)
    
    print(f"{len(funcionarios)} funcionários predefinidos cadastrados com sucesso.")

def CadastrarSalario():
    global registrosFuncionarios
    global baseSalaries
    global amountOfEmployees
    global outSourcedCompanies
    global amountOfOutSourcedEmployees

    name = input("Nome do funcionário: ")
    role = int(input("Cargo: \n" \
    "1- Diretor \n" \
    "2- Coordenador \n" \
    "3- Recursos Humanos \n" \
    "4- Marketing \n" \
    "5- Vendas \n" \
    "6- Financeiro \n" \
    "7- Desenvolvedor \n" \
    "8- Product Designer \n" \
    "9- Limpeza \n" ))
    baseSalary = float(input("Salário: R$ "))
    baseSalaries.append(baseSalary)
    valeAlimentacao = float(input("Vale alimentação: R$ "))
    isOutSourced = (input("É funcionário terceirizado? (s/n): ")).strip().lower()
    transportCost = 0.0
    comission = 0.0
    totalHorasExtra = 0.0

    if isOutSourced == "s":
        amountOfOutSourcedEmployees += 1
        outSourcedCompany = input("Nome da empresa terceira: ")
        outSourcedCompanies.append(outSourcedCompany)
        usesTransport = (input("Utiliza transporte? (s/n) ")).strip().lower()
        if usesTransport == 's':
            transportCost = float(input("Vale transporte: R$"))
            valeTransportes.append(transportCost)
    elif isOutSourced == "n":
        hasExtraHours = (input("O colaborador possui horas extras? (s/n): ")).strip().lower()
        if hasExtraHours == 's':
            extraHours = float(input("Horas extra: "))
            totalHorasExtra = CalcularHoraExtra(extraHours)
            hasComission = (input("Possui comissão? (s/n): ")).strip().lower()
            if hasComission == 's':
                comission = float(input("Valor da comissão: R$ "))

    amountOfEmployees += 1
    print(f"\nResumo do cadastro:")
    print(f"Nome: {name}")
    print(f"Cargo: {role}")
    print(f"Salário base: R$ {baseSalary:.2f}")
    totalSalary = CalcularSalario(baseSalary, transportCost, valeAlimentacao, comission, totalHorasExtra)
    print(f"Salário total: R$ {totalSalary:.2f}")
    print(f"Total de funcionários cadastrados: {amountOfEmployees}")
    print(f"Total de funcionários terceirizados: {amountOfOutSourcedEmployees}")
    print(f"Empresas terceirizadas associadas: {', '.join(outSourcedCompanies)}")

    funcionario = {
    "nome": name,
    "cargo": role,
    "salario_base": baseSalary,
    "vale_alimentacao": valeAlimentacao,
    "vale_transporte": transportCost,
    "comissao": comission,
    "horas_extra": totalHorasExtra,
    "salario_total": totalSalary,
    "terceirizado": isOutSourced == "s",
    "empresa_terceira": outSourcedCompany if isOutSourced == "s" else None
    }

    
    registrosFuncionarios.append(funcionario)

def GeneralInfo():
    global registrosFuncionarios
    global baseSalaries
    global amountOfEmployees
    global outSourcedCompanies
    global amountOfOutSourcedEmployees
    global valeTransportes

    print("\n======= TABELA DE FUNCIONÁRIOS =======")
    print(f"{'Nome':<20} {'Cargo':<15} {'Salário Base':<15} {'Vale Alimentação':<20} {'Vale Transporte':<20} {'Comissão':<20} {'Horas Extras':<20} {'Salário Total':<20} {'Terceirizado':<20} {'Empresa Terceira':<20}")
    
    for funcionario in registrosFuncionarios:
        print(f"{funcionario['nome']:<20} {funcionario['cargo']:<15} R$ {funcionario['salario_base']:<15.2f} R$ {funcionario['vale_alimentacao']:<20.2f} R$ {funcionario['vale_transporte']:<20.2f} R$ {funcionario['comissao']:<15.2f}  R$ {funcionario['horas_extra']:<15.2f} R$ {funcionario['salario_total']:<15.2f} {str(funcionario['terceirizado']):<15} {funcionario['empresa_terceira'] if funcionario['empresa_terceira'] else 'N/A':<20}")
    
    print(f"\nTotal de funcionários cadastrados: {amountOfEmployees}")
    print(f"Total de funcionários terceirizados: {amountOfOutSourcedEmployees}")
    print(f"Empresas terceirizadas associadas: {', '.join(outSourcedCompanies)}")

def GerarGraficos():
    import matplotlib.pyplot as plt

    global registrosFuncionarios
    global baseSalaries
    global amountOfEmployees
    global outSourcedCompanies
    global amountOfOutSourcedEmployees
    global valeTransportes

    if not registrosFuncionarios:
        print("Nenhum funcionário cadastrado para gerar gráficos.")
        return

    # Gráfico de salários
    nomes = [funcionario['nome'] for funcionario in registrosFuncionarios]
    salarios = [funcionario['salario_total'] for funcionario in registrosFuncionarios]

    plt.figure(figsize=(15, 10))
    plt.bar(nomes, salarios, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title('Salários dos Funcionários')
    plt.grid(axis='x')
    plt.show()

    efetivos = sum(1 for f in registrosFuncionarios if not f["terceirizado"])
    terceirizados = sum(1 for f in registrosFuncionarios if f["terceirizado"])

    labels = ['Efetivos', 'Terceirizados']
    sizes = [efetivos, terceirizados]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'orange'])
    plt.title('Distribuição de Funcionários Efetivos vs Terceirizados')
    plt.axis('equal')
    plt.show()

    nomes = [f["nome"] for f in registrosFuncionarios]
    salarios_base = [f["salario_base"] for f in registrosFuncionarios]
    vale_alimentacao = [f["vale_alimentacao"] for f in registrosFuncionarios]
    comissao = [f["comissao"] for f in registrosFuncionarios]

    plt.bar(nomes, salarios_base, label='Salário Base')
    plt.bar(nomes, vale_alimentacao, bottom=salarios_base, label='Vale Alimentação')
    plt.bar(nomes, comissao, label='Comissão')

    plt.xlabel('Funcionários')
    plt.ylabel('Valor (R$)')
    plt.title('Composição do Salário Total por Funcionário')
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.show()

def main():
    while True:
        try:
            menu = int(input("======= MENU INICIAL =======\n" \
                "1- Cadastrar salário \n"\
                "2- Gerar tabela\n" \
                "3- Informaçãoes gerais \n"
                "4- Dados pré-definidos \n" \
                "5- Sair\n"))

            if menu == 1:
                CadastrarSalario()
            elif menu == 2:
                GeneralInfo()
            elif menu == 3:
                GerarGraficos()
            elif menu == 4:
                InserirFuncionariosPredefinidos()                
            elif menu == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
     main()
