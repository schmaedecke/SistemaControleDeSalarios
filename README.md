💼 Sistema de Folha de Pagamento
📄 Descrição
Este projeto tem como objetivo automatizar e simplificar o cálculo da folha de pagamento de uma empresa de tecnologia. O sistema permite gerenciar informações de funcionários, calcular salários finais considerando horas extras, adicionais e comissões, e gerar relatórios detalhados em formato CSV e gráficos interativos.

⚙️ Funcionalidades
Cadastro de dados básicos (nome, cargo, salário base)

Identificação de funcionários terceirizados

Cálculo automático de:

Vale-transporte

Horas extras

Adicionais de periculosidade ou insalubridade

Comissão sobre vendas

Exibição do salário final calculado

Validação e edição de dados inseridos

Geração de arquivo .csv com todas as informações

Relatórios gráficos:

Distribuição de pagamentos por cargo

Total de funcionários

Porcentagem de funcionários terceirizados

💡 Entradas e Saídas
Entradas
Nome

Cargo

Salário base

Horas extras

Total de vendas

Saídas
Salário final

Valor das horas extras

Valor de comissões

Arquivo .csv para download

Gráficos informativos

🧩 Arquitetura
O sistema foi desenvolvido de forma modular, dividido em quatro principais blocos:

Entrada de dados: captura e armazenamento das informações.

Exibição para conferência: apresentação das informações antes do processamento final, permitindo alterações.

Processamento: cálculos salariais e geração dos gráficos.

Saída: exibição dos resultados finais e disponibilização do arquivo .csv.

🗂️ Estruturas de dados
Estrutura Funcionario para armazenar todas as informações de cada colaborador.

📊 Funcionalidades analíticas
AmountPerRole(): distribuição do total de funcionários por cargo.

TotalAmountOfEmployees(): total geral de funcionários.

PercentageOfOutsourced(): porcentagem de funcionários terceirizados.

MostExpensiveRole(): cargo mais custoso em termos de folha.

TotalAmountOfPayment(): total pago em salários.

AverageBaseSalary(): média dos salários base.

AverageFinalSalary(): média dos salários finais.

EmployeesNeedingTransport(): número de funcionários que utilizam vale-transporte.

🚀 Como executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências (se houver).

Execute o sistema conforme as instruções do seu ambiente (por exemplo, rodando um script Python ou compilando um projeto em C#).

💬 Contribuição
Contribuições são bem-vindas!

Faça um fork

Crie uma branch com sua feature ou correção: git checkout -b feature/nova-feature

Commit suas alterações: git commit -m 'Adiciona nova feature'

Push para o branch: git push origin feature/nova-feature

Abra um Pull Request
