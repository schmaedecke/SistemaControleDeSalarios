registrosFuncionarios = []
baseSalaries = []
amountOfEmployees = 0
outSourcedCompanies = []
amountOfOutSourcedEmployees = 0
valeTransportes = []

from enum import Enum

class Cargo(Enum):
    DIRETOR = 1
    COORDENADOR = 2
    RECURSOS_HUMANOS = 3
    MARKETING = 4
    VENDAS = 5
    FINANCEIRO = 6
    DESENVOLVEDOR = 7
    PRODUCT_DESIGNER = 8
    LIMPEZA = 9

    @staticmethod
    def obter_nome_por_valor(valor):
        for cargo in Cargo:
            if cargo.value == valor:
                return cargo.name.replace("_", " ").title()
        return "Cargo inválido" 

def CalcularHoraExtra(extraHours):
    valorHoraNormal = 15.0
    valorHoraExtra = valorHoraNormal * 1.5
    totalHoraExtra = valorHoraExtra * extraHours
    return totalHoraExtra

def CalcularSalario(baseSalary, transportationCost, valeAlimentacao, comission, horasExtra):
    return baseSalary + transportationCost + comission + horasExtra + valeAlimentacao

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
    cargo_nome = Cargo.obter_nome_por_valor(role)
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
    print(f"Cargo: {cargo_nome}")
    print(f"Salário base: R$ {baseSalary:.2f}")
    totalSalary = CalcularSalario(baseSalary, transportCost, valeAlimentacao, comission, totalHorasExtra)
    print(f"Salário total: R$ {totalSalary:.2f}")
    print(f"Total de funcionários cadastrados: {amountOfEmployees}")
    print(f"Total de funcionários terceirizados: {amountOfOutSourcedEmployees}")
    print(f"Empresas terceirizadas associadas: {', '.join(outSourcedCompanies)}")

    funcionario = {
    "nome": name,
    "cargo": cargo_nome,
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

def gerarArquivoCsv():
    import csv

    global registrosFuncionarios

    if not registrosFuncionarios:
        print("Nenhum funcionário cadastrado para gerar o CSV.")
        return

    with open('funcionarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Cargo', 'Salário Base', 'Vale Alimentação', 'Vale Transporte', 'Comissão', 'Horas Extras', 'Salário Total', 'Terceirizado', 'Empresa Terceira'])
        
        for funcionario in registrosFuncionarios:
            writer.writerow([
                funcionario['nome'],
                funcionario['cargo'],
                funcionario['salario_base'],
                funcionario['vale_alimentacao'],
            ])

def main():
    while True:
        try:
            menu = int(input("======= MENU INICIAL =======\n" \
                "1- Cadastrar salário \n"\
                "2- Dados gerais\n" \
                "3- Gerar gráficos \n"
                "4- Gerar CSV\n" \
                "5- Sair \n" \
                "Escolha uma opção (1-5): "))       

            if menu == 1:
                CadastrarSalario()
            elif menu == 2:
                GeneralInfo()
            elif menu == 3:
                GerarGraficos()   
            elif menu == 4:
                gerarCSV = input("Deseja gerar um arquivo CSV com os dados? (s/n): ").strip().lower()
                if gerarCSV == 's': 
                    gerarArquivoCsv()   
                    print("Arquivo 'funcionarios.csv' salvo com sucesso.")       
            elif menu == 5:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
     main()