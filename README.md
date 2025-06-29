# 💼 Sistema de Folha de Pagamento

## 📄 Descrição

Este projeto tem como objetivo automatizar e simplificar o cálculo da folha de pagamento de uma empresa de tecnologia. O sistema permite gerenciar informações de funcionários, calcular salários finais considerando horas extras, adicionais e comissões, e gerar relatórios detalhados em formato CSV e gráficos interativos.

---

## ⚙️ Funcionalidades

- Cadastro de dados básicos (nome, cargo, salário base)
- Identificação de funcionários terceirizados
- Cálculo automático de:
  - Vale-transporte
  - Horas extras
  - Adicionais de periculosidade ou insalubridade
  - Comissão sobre vendas
- Exibição do salário final calculado
- Validação e edição de dados inseridos
- Geração de arquivo `.csv` com todas as informações
- Relatórios gráficos:
  - Distribuição de pagamentos por cargo
  - Total de funcionários
  - Porcentagem de funcionários terceirizados

---

## 💡 Entradas e Saídas

### Entradas

- Nome
- Cargo
- Salário base
- Horas extras
- Total de vendas

### Saídas

- Salário final
- Valor das horas extras
- Valor de comissões
- Arquivo `.csv` para download
- Gráficos informativos

---

## 🧩 Arquitetura

O sistema foi desenvolvido de forma modular, dividido em quatro principais blocos:

1. **Entrada de dados:** captura e armazenamento das informações.
2. **Exibição para conferência:** apresentação das informações antes do processamento final, permitindo alterações.
3. **Processamento:** cálculos salariais e geração dos gráficos.
4. **Saída:** exibição dos resultados finais e disponibilização do arquivo `.csv`.

---

## 🗂️ Estruturas de dados

- Estrutura `Funcionario` para armazenar todas as informações de cada colaborador.

---

## 📊 Funcionalidades analíticas

- `AmountPerRole()` — Distribuição do total de funcionários por cargo
- `TotalAmountOfEmployees()` — Total geral de funcionários
- `PercentageOfOutsourced()` — Porcentagem de funcionários terceirizados
- `MostExpensiveRole()` — Cargo mais custoso em termos de folha
- `TotalAmountOfPayment()` — Total pago em salários
- `AverageBaseSalary()` — Média dos salários base
- `AverageFinalSalary()` — Média dos salários finais
- `EmployeesNeedingTransport()` — Número de funcionários que utilizam vale-transporte

---


