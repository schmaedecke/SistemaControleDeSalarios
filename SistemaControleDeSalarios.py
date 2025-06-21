def CalcularHoraExtra(extraHours):
    valorHoraNormal = 15.0
    valorHoraExtra = valorHoraNormal * 1.5
    totalHoraExtra = valorHoraExtra * extraHours
    return totalHoraExtra

def CalcularSalario(baseSalary, transportationCost, valeAlimentacao, comission, horasExtra):
    return baseSalary + transportationCost + comission + horasExtra + valeAlimentacao

def CadastrarSalario():
    amountOfEmployees = 0
    outSourcedCompanies = []
    amountOfOutSourcedEmployees = 0
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
    "9- Limpeza "))
    baseSalary = float(input("Salário: R$"))
    valeAlimentacao = float(input("Vale alimentação: R$ "))
    isOutSourced = (input("É funcionário terceirizado? (s/n): ")).strip().lower()
    transportCost = 0.0
    comission = 0.0
    horasExtra = 0.0

    if isOutSourced == "s":
        amountOfOutSourcedEmployees += 1
        outSourcedCompany = input("Nome da empresa terceira: ")
        outSourcedCompanies.append(outSourcedCompany)
        usesTransport = (input("Utiliza transporte? (s/n) ")).strip().lower()
        if usesTransport == 's':
            transportCost = float(input("Vale transporte: R$"))
    elif isOutSourced == "n":
        hasExtraHours = (input("O colaborador possui horas extras? (s/n): ")).strip().lower()
        if hasExtraHours == 's':
            extraHours = float(input("Horas extra: "))
            horasExtra = CalcularHoraExtra(extraHours)
        hasComission = (input("Possui comissão? (s/n): ")).strip().lower()
        if hasComission == 's':
            comission = float(input("Valor da comissão: R$ "))

    amountOfEmployees += 1
    print(f"\nResumo do cadastro:")
    print(f"Nome: {name}")
    print(f"Cargo: {role}")
    print(f"Salário base: R$ {baseSalary:.2f}")
    print(f"Total de funcionários cadastrados: {amountOfEmployees}")
    print(f"Total de funcionários terceirizados: {amountOfOutSourcedEmployees}")
    print(f"Empresas terceirizadas associadas: {', '.join(outSourcedCompanies)}")
    totalSalary = CalcularSalario(baseSalary, transportCost, valeAlimentacao, comission, horasExtra)
    print(f"Salário total: R$ {totalSalary:.2f}")

   

def main():
    while True:
        try:
            menu = int(input("======= MENU INICIAL =======\n" \
                            "1- Cadastrar salário \n"\
                            "2- Gerar tabela\n" \
                            "3- Informaçãoes gerais"))

            if menu == 1:
                CadastrarSalario()
            # elif menu == 2:
            #     GerarCsv()
            # elif menu == 3:
            #     GeneralInfo()
            elif menu == 4:
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()